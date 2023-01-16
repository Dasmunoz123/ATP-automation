import pandas as pd
import dataATP
import sys


configuracion = pd.read_excel(sys.argv[1])

tpbig_dir = 'C:/ATP/atpintel' ## ruta ejecutable ATP
atpfiles_dir = "C:/ATP/ATPdata/work/GCM_adaptative_1509/" ## ruta archivos .ATP

if __name__ == '__main__':

    # list of the nodes in which there would be short circuit
    nodos = [
        "SC_P2", "SC_P3", "SC_P4", "SC_P5",
        "SC_A1", "SC_A2", "SC_A3","SC_A4", "SC_A5",
        "SC_L1", "SC_L2", "SC_L3", "SC_L4", "SC_L5",
        "SC_C1"] 

    # IBG control strategy - 4 characters
    controles = [['0.00','0.00','IBAL']]  

    # List of short circuit impedances (Iso - Gr) & 4 characters
    impedancias =[
                ['  1.', '1.E7', '1.E7', 'Ag_1 ', 'Gr'],
                ['  3.', '1.E7', '1.E7', 'Ag_3 ', 'Gr'],
                ['  6.', '1.E7', '1.E7', 'Ag_6 ', 'Gr'],
                [' 10.', '1.E7', '1.E7', 'Ag_10', 'Gr'],
                [' 15.', '1.E7', '1.E7', 'Ag_15', 'Gr'],
                [' 20.', '1.E7', '1.E7', 'Ag_20', 'Gr'],
                
                ['  .5', '  .5', '1.E7', 'ABg_1 ', 'Gr'],
                [' 1.5', ' 1.5', '1.E7', 'ABg_3 ', 'Gr'],
                [' 3.0', ' 3.0', '1.E7', 'ABg_6 ', 'Gr'],
                ['  5.', '  5.', '1.E7', 'ABg_10', 'Gr'],
                [' 7.5', ' 7.5', '1.E7', 'ABg_15', 'Gr'],
                [' 10.', ' 10.', '1.E7', 'ABg_20', 'Gr'],
                
                ['  .5', '  .5', '1.E7', 'AB_1 ', 'Iso'],
                [' 1.5', ' 1.5', '1.E7', 'AB_3 ', 'Iso'],
                [' 3.0', ' 3.0', '1.E7', 'AB_6 ', 'Iso'],
                ['  5.', '  5.', '1.E7', 'AB_10', 'Iso'],
                [' 7.5', ' 7.5', '1.E7', 'AB_15', 'Iso'],
                [' 10.', ' 10.', '1.E7', 'AB_20', 'Iso'],
                
                ['  1.', '  1.', '  1.', 'ABC_1 ', 'Iso'],
                ['  3.', '  3.', '  3.', 'ABC_3 ', 'Iso'],
                ['  6.', '  6.', '  6.', 'ABC_6 ', 'Iso'],
                [' 10.', ' 10.', ' 10.', 'ABC_10', 'Iso'],
                [' 15.', ' 15.', ' 15.', 'ABC_15', 'Iso'],
                [' 20.', ' 20.', ' 20.', 'ABC_20', 'Iso']
                ]

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
