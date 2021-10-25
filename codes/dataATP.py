import os
import sys
import json
import utils


""" 
Para ejecutar ATP en consola se configura el Working 
directory para que esté en el path del solver de ATP.
"""


def executeATP(caso,nodos,impedancias,ATP_file,ATP_tmp,lis_tmp,tpbig_dir):
    
    nodo_dict = {}
    for nodo in nodos:
        utils.posiciones(ATP_file, ATP_tmp, caso['PosicionNodos'],caso['NodoReplace'], nodo)
        
        distance_dict = {}; PHseq_dict = {}; diferential_dict = {}; PHabc_dict = {}
        
        for imped in impedancias:
            utils.impedancias(ATP_tmp, caso['PosicionImpedancias'], imped, [caso['NodoA'],caso['NodoB']])
            
            wd_nativo = os.getcwd()
            try: os.chdir(tpbig_dir)
            except OSError: sys.exit("ATP consola")
            comandoEX = "tpbigi64.exe DISK " + ATP_tmp + " s -r"
            os.system(comandoEX)
            try: os.chdir(wd_nativo)
            except OSError: sys.exit("Paila")

            if caso['Funcion21'] == 'Si': distance_dict[imped[3]] = utils.relay21(lis_tmp, caso['ID21'])
            if caso['PH_012'] == 'Si': PHseq_dict[imped[3]] = utils.GenericPH_012(lis_tmp, caso['IDPH012'])
            if caso['Funcion87'] == 'Si': diferential_dict[imped[3]] = utils.relay87(lis_tmp, caso['ID87'])
            if caso['PH_abc'] == 'Si': PHabc_dict[imped[3]] = utils.GenericPH_abc(lis_tmp, caso['IDPHabc'])

        aux_dict = {}
        if caso['Funcion21'] == 'Si': aux_dict['R21'] = distance_dict
        if caso['PH_012'] == 'Si': aux_dict['PH012'] = PHseq_dict
        if caso['Funcion87'] == 'Si':aux_dict['R87'] = diferential_dict
        if caso['PH_abc'] == 'Si': aux_dict['PHabc'] = PHabc_dict
        
        nodo_dict[nodo] = aux_dict

        os.remove(ATP_tmp)
        os.remove(lis_tmp)

        intel_files = os.listdir(tpbig_dir)
        for file in intel_files:
            if file.endswith(".tmp"):
                TMP_Remove = os.path.join(tpbig_dir, file)
                os.remove(TMP_Remove)
    
    return nodo_dict



def runATP(caso,controles,nodos,impedancias,atpfiles_dir,tpbig_dir):

    ATP_tmp = atpfiles_dir + "Temporal_N.atp"
    lis_tmp = atpfiles_dir + "Temporal_N.lis"
    dbg_tmp = atpfiles_dir + "Temporal_N.dbg"
    pl4_tmp = atpfiles_dir + "Temporal_N.dbg"
    
    ATPfile_Origin = atpfiles_dir + caso['Archivos'] + ".atp"

    if os.path.exists(ATP_tmp): os.remove(ATP_tmp)
    if os.path.exists(lis_tmp): os.remove(lis_tmp)
    if os.path.exists(dbg_tmp): os.remove(dbg_tmp)
    if os.path.exists(pl4_tmp): os.remove(pl4_tmp)

    if caso['Tipo'] == 'IBG':
        
        for control in controles:
            utils.IBGconf_controls(ATPfile_Origin, caso['PosicionIBG'], control)
            resu = executeATP(caso,nodos,impedancias,ATPfile_Origin,ATP_tmp,lis_tmp,tpbig_dir)
            
            nombreS = caso['DireccionResultados'] + caso['Nombre'] + control[2] + '.json'
            with open(nombreS, 'w') as outfile: json.dump(resu, outfile)

    elif caso['Tipo'] == 'SYN':
        resu = executeATP(caso,nodos,impedancias,ATPfile_Origin,ATP_tmp,lis_tmp,tpbig_dir)
        nombreS = caso['DireccionResultados'] + caso['Nombre'] + '.json'
        with open(nombreS, 'w') as outfile: json.dump(resu, outfile)

    else:
        sys.exit("Tipo de simulacion IBG o SYN no valida")