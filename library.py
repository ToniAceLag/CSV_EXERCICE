

import literales as lit
import csv

def match_menu():
    num = int(input(lit.MSG_DOS))
    return num

def write_csv():
    with open('files/'+valid_csvname(), 'a', encoding='utf-8',
              newline='') as csvfile:  #abre el archivo en modo append y lo codifica a 'utf-8'por si acaso el archivo
        fieldnames = ['any', 'codi', 'literal', 'homes_0_14_anys', 'homes_15_65_anys', 'homes__65_anys_a_mes_anys',
                      'dones_0_14_anys', 'dones_15_64_anys', 'dones_65_a_mes_anys',
                      'total_1','total_2','total_3']  # una lista de key's de diccionario
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        regs = int(input(lit.INP_MSG))  # numero de lineas que quieras añadir
        for i in range(regs):  # donde pondras lo que quieres en la linea
            any = int(input(lit.MSG_TRES))
            codi_com = int(input(lit.MSG_QUAT))
            literal = input(lit.MSG_CINC)
            h_0_14 = int(input(lit.MSG_SEIS))
            h_15_64 = int(input(lit.MSG_SIET))
            h_65_mas = int(input(lit.MSG_OCHO))
            d_0_14 = int(input(lit.MSG_NUEV))
            d_15_64 = int(input(lit.MSG_DIEZ))
            d_64_mas = int(input(lit.MSG_ONCE))
            total_un = h_0_14 + d_0_14
            total_du = h_15_64 + d_15_64
            total_tri = h_65_mas + d_64_mas
            writeCSV.writerow(
                {'any':any, 'codi':codi_com, 'literal':literal, 'homes_0_14_anys':h_0_14, 'homes_15_65_anys':h_15_64, 'homes__65_anys_a_mes_anys':h_65_mas,
                      'dones_0_14_anys':d_0_14, 'dones_15_64_anys':d_15_64, 'dones_65_a_mes_anys':d_15_64,
                      'total_1':total_un,'total_2':total_du,'total_3':total_tri})  # la parte que añade al fichero lo que has añadido anterior mente en el for

def read_csv():
    with open('files/'+valid_csvname()) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        print(lit.MSG_UNO)
        csvfile.readline()
        sum_h = 0
        sum_d = 0
        for row in readCSV:
            sum_h = sum_h+int(row[3])
            sum_d =sum_d+int(row[6])
            print(f'\t |{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}|{row[8]}|{row[9]}|{row[10]}|')
        print("Aquest es el numero total de homes de 0 a 14 anys",sum_h,"y aquest el total de dones de 0 a 14 anys",sum_d)
def valid_csvname():
    csv_name = input(lit.TXT_INPUT)
    if csv_name.count(lit.CSV_COUNT) != 1:
        csv_name = csv_name + lit.CSV
    return csv_name