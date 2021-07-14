import pandas as pd
import dataATP


configuracion = pd.read_csv('archivoConfiguracion.csv')
tpbig_dir = 'C:/ATP/atpintel' ## ruta ejecutable ATP
atpfiles_dir = "C:/ATP/ATPdata/work/DeployCode/" ## ruta archivos .ATP

 # list of the nodes in which there would be short circuit
nodos = ["SC_P1", "SC_P2", "SC_P3", "SC_P4", "SC_P5", "SC_A1", "SC_A2","SC_A3", "SC_A4"] 
# IBG control strategy - 4 characters
controles = [['0.00','0.00','IBAL']]  
# List of short circuit impedances (Iso - Gr) & 4 characters
impedancias = [['  .1', '1.E7', '1.E7', 'Ag_.1', 'Gr'],
               ['  1.', '1.E7', '1.E7', 'Ag_1 ', 'Gr']]

for index, row in configuracion.iterrows():
    dataATP.runATP(row,controles,nodos,impedancias,atpfiles_dir,tpbig_dir)



'''
## Para Generar diferentes combinaciones de Kp & Kq

Kp = ["-1.0","-0.8","-0.6","-0.4","-0.2","0.00","0.20","0.40","0.60","0.80","1.00"]
Kq = ["-1.0","-0.8","-0.6","-0.4","-0.2","0.00","0.20","0.40","0.60","0.80","1.00"]

controls = []
index = 0
for i in range(len(Kp)):
    for j in range(len(Kq)):
        index =+ 1
        controls.append((Kp[i], Kq[j],"C" + str(index) + "(Kp" + Kp[i] + "Kq" + Kq[j] + ")"))
'''
