import pickle

## Funciones de lectura de datos & resultados

def relay21(LIS_File_Path, IDreles):
    IDreles = IDreles.split(':')
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    barrido_rel = {}

    for rel in IDreles:
        ZaR = [] ; ZaX = [] ; ZbR = [] ; ZbX = [] ; ZcR = [] ; ZcX = [] ## Impedancias
        trip = [] ; ZoneA = [] ; ZoneB = [] ; ZoneC = [] ; time = [] ## Operaciones
        for lin in response:
            if "BEGIN WRITE @W1RELAY21P " + rel in lin:
                relay_data = response[response.index(lin) + 1].split()
                
                ZaR.append(float(relay_data[0])) ; ZaX.append(float(relay_data[1]))
                ZbR.append(float(relay_data[2])) ; ZbX.append(float(relay_data[3]))
                ZcR.append(float(relay_data[4])) ; ZcX.append(float(relay_data[5]))
                ZoneA.append(float(relay_data[7])) ; ZoneB.append(float(relay_data[8])) ; ZoneC.append(float(relay_data[9]))
                trip.append(float(relay_data[6])) ; time.append(float(relay_data[10]))

        relDict = {"ZaR": ZaR, "ZaX": ZaX, "ZbR": ZbR, "ZbX": ZbX, "ZcR": ZcR, "ZcX": ZcX, "trip": trip, "ZoneA": ZoneA, "ZoneB": ZoneB, "ZoneC": ZoneC, "time": time}
        barrido_rel["Rel21_" + rel] = relDict
        del relDict

    lis.close()
    return barrido_rel


def relay87(LIS_File_Path, IDreles):
    IDreles = IDreles.split(':')
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    barrido_rel = {}

    for rel in IDreles:
        IresA = [] ; IresB = [] ; IresC = [] ; IdifA = [] ; IdifB = [] ; IdifC = [] ; trip = [] ; time = []
        for lin in response:
            if "BEGIN WRITE @W1RELAY87L " + rel in lin:
                relay_data = response[response.index(lin) + 1].split()

                IresA.append(float(relay_data[0])) ; IresB.append(float(relay_data[2])) ; IresC.append(float(relay_data[4]))
                IdifA.append(float(relay_data[1])) ; IdifB.append(float(relay_data[3])) ; IdifC.append(float(relay_data[5]))
                trip.append(float(relay_data[6])) ; time.append(float(relay_data[7]))

        relDict = {"IresA": IresA, "IresB": IresB, "IresC": IresC, "IdifA": IdifA, "IdifB": IdifB, "IdifC": IdifC, "trip": trip, "time": time}
        barrido_rel["Rel87_" + rel] = relDict
        del relDict

    lis.close()
    return barrido_rel


def LCD87I1(LIS_File_Path, IDreles):
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    barrido_rel = {}
    for k in range(len(IDreles)):
        IreA = []
        IimA = []
        IreB = []
        IimB = []
        IreC = []
        IimC = []
        time = []
        for l in range(len(response)):
            if "BEGIN WRITE @W1RELAY87LI1 " + str(IDreles[k]) in (response[l]):
                relay_data = response[l + 1].split()

                IreA.append(float(relay_data[0]))
                IreB.append(float(relay_data[2]))
                IreC.append(float(relay_data[4]))
                IimA.append(float(relay_data[1]))
                IimB.append(float(relay_data[3]))
                IimC.append(float(relay_data[5]))
                time.append(float(relay_data[6]))

        relDict = {"IreA": IreA, "IreB": IreB, "IreC": IreC, "IimA": IimA, "IimB": IimB, "IimC": IimC, "time": time}
        barrido_rel["LCD87I1_" + str(IDreles[k])] = relDict
        del relDict

    lis.close()
    return barrido_rel


def LCD87I2(LIS_File_Path, IDreles):
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    barrido_rel = {}
    for k in range(len(IDreles)):
        IreA = []
        IimA = []
        IreB = []
        IimB = []
        IreC = []
        IimC = []
        time = []
        for l in range(len(response)):
            if "BEGIN WRITE @W1RELAY87LI2 " + str(IDreles[k]) in (response[l]):
                relay_data = response[l + 1].split()

                IreA.append(float(relay_data[0]))
                IreB.append(float(relay_data[2]))
                IreC.append(float(relay_data[4]))
                IimA.append(float(relay_data[1]))
                IimB.append(float(relay_data[3]))
                IimC.append(float(relay_data[5]))
                time.append(float(relay_data[6]))

        relDict = {"IreA": IreA, "IreB": IreB, "IreC": IreC, "IimA": IimA, "IimB": IimB, "IimC": IimC, "time": time}
        barrido_rel["LCD87I2_" + str(IDreles[k])] = relDict
        del relDict

    lis.close()
    return barrido_rel


def GenericPH_012(LIS_File_Path, IDmeas):
    IDmeas = IDmeas.split(':')
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    datos = {}

    for abc in IDmeas:
        reSecO = [] ; reSec1 = [] ; reSec2 = [] ; imSecO = [] ; imSec1 = [] ; imSec2 = [] ; time = []
        for l in range(len(response)):
            if "BEGIN WRITE @ABC2SEQ " + abc in (response[l]):
                lin_data = response[l + 1].split()
                
                reSecO.append(float(lin_data[0])) ; reSec1.append(float(lin_data[1])) ; reSec2.append(float(lin_data[2])) ; imSecO.append(float(lin_data[3]))
                imSec1.append(float(lin_data[4])) ; imSec2.append(float(lin_data[5])) ; time.append(float(lin_data[6]))

        diccionario = {"reSecO": reSecO, "reSec1": reSec1, "reSec2": reSec2, "imSecO": imSecO, "imSec1": imSec1, "imSec2": imSec2, "time": time}
        datos["PHmeas_" + abc] = diccionario
        del diccionario

    lis.close()
    return datos



def GenericPH_abc(LIS_File_Path, IDmeas):
    IDmeas = IDmeas.split(':')
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    datos = {}
    
    for meter in IDmeas:
        re_PhA = [] ; re_PhB = [] ; re_PhC = [] ; im_PhA = [] ; im_PhB = [] ; im_PhC = [] ; time = []
        for l in range(len(response)):
            if "BEGIN WRITE @PHWRI " + meter in (response[l]):
                lin_data = response[l + 1].split()
                
                re_PhA.append(float(lin_data[0])) ; re_PhB.append(float(lin_data[1])) ; re_PhC.append(float(lin_data[2]))
                im_PhA.append(float(lin_data[3])) ; im_PhB.append(float(lin_data[4])) ; im_PhC.append(float(lin_data[5]))
                time.append(float(lin_data[6]))

        diccionario = {"re_PhA": re_PhA, "re_PhB": re_PhB, "re_PhC": re_PhC, "im_PhA": im_PhA, "im_PhB": im_PhB, "im_PhC": im_PhC, "time": time}
        datos["PHmeas_" + meter] = diccionario
        del diccionario

    lis.close()
    return datos



def FRT(LIS_File_Path, IDFRT):
    lis = open(LIS_File_Path, "r")
    response = lis.readlines()
    barrido_FRT = {}

    for k in range(len(IDFRT)):
        C52 = []
        time = []
        for l in range(len(response)):
            if "BEGIN WRITE @VSC01 " + str(IDFRT[k]) in (response[l]):
                relay_data = response[l + 1].split()
                C52.append(relay_data[0])
                time.append(float(relay_data[1]))

        FRTDict = {"C52": C52,"time": time}
        barrido_FRT["FRT_" + str(IDFRT[k])] = FRTDict
        del FRTDict

    lis.close()
    return barrido_FRT


## Funciones de modificación para ejecución archivos.ATP

def posiciones(ATP_File_Path, ATP_File_PathN, Pos_Number, replace, node):
    Pos_Number = Pos_Number.split(':')
    f1 = open(ATP_File_Path, "r")
    F1 = f1.readlines()
    f1.close()

    f2 = open(ATP_File_PathN, "w")
    lc = 1
    for line in F1:
        if lc == int(Pos_Number[0]) or lc == int(Pos_Number[1]) or lc == int(Pos_Number[2]):
            f2.write(line.replace(replace, node))
            print((line.replace(replace, node)))
        else:
            f2.write(line)
        lc = lc + 1
    f2.close()
    return 1


def IBGconf_controls(ATP_File_Path, IBG_positions, controls):
    IBG_positions = IBG_positions.split(':')
    f1 = open(ATP_File_Path, "r")
    F1 = f1.readlines()
    f1.close()

    f1 = open(ATP_File_Path, "w")
    lc = 1
    for line in F1:
        if lc == int(IBG_positions[0]):
            f1.write("  Kp:=     " + controls[0] + "\n")
        elif lc == int(IBG_positions[1]):
            f1.write("  Kq:=     " + controls[1] + "\n")
        else:
            f1.write(line)

        lc = lc + 1
    f1.close()


def impedancias(ATP_File_PathN, Imp_Number, Zfalla, nodos):
    Imp_Number = Imp_Number.split(':')
    f1 = open(ATP_File_PathN, "r")
    F1 = f1.readlines()
    f1.close()

    f2 = open(ATP_File_PathN, "w")
    lc = 1
    for line in F1:
        if lc == int(Imp_Number[0]):
            if Zfalla[4] == "Gr":
                imp = "  " + nodos[0] + "A                    " + Zfalla[0] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)
            elif Zfalla[4] == "Iso":
                imp = "  " + nodos[0] + "A" + nodos[1] + "               " + Zfalla[0] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)

        elif lc == int(Imp_Number[1]):
            if Zfalla[4] == "Gr":
                imp = "  " + nodos[0] + "B                    " + Zfalla[1] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)
            elif Zfalla[4] == "Iso":
                imp = "  " + nodos[0] + "B" + nodos[1] + "               " + Zfalla[1] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)

        elif lc == int(Imp_Number[2]):
            if Zfalla[4] == "Gr":
                imp = "  " + nodos[0] + "C                    " + Zfalla[2] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)
            elif Zfalla[4] == "Iso":
                imp = "  " + nodos[0] + "C" + nodos[1] + "               " + Zfalla[2] + \
                      "                                               0\n"
                print(imp)
                f2.write(imp)
            "               "
        else:
            f2.write(line)
        lc = lc + 1

    f2.close()


def graphics(positions_list):
    for i in range(2):
        plt.plot(positions_list[0].Impedance[0].Relay[i].ZaR, positions_list[0].Impedance[0].Relay[i].ZaX, '-r',
                 label='Phase A')
        plt.plot(positions_list[0].Impedance[0].Relay[i].ZbR, positions_list[0].Impedance[0].Relay[i].ZbX, '-g',
                 label='Phase B')
        plt.plot(positions_list[0].Impedance[0].Relay[i].ZcR, positions_list[0].Impedance[0].Relay[i].ZcX, '-b',
                 label='Phase C')
        plt.legend()
        plt.title("Figure" + str(i))
        plt.xlabel('R[Ohm]')
        plt.ylabel('X[Ohm]')
        plt.show()


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_object(filename):
    with open(filename, 'rb'):
        data = pickle.load(input)
        return data
