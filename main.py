import library as l#Importas la libreria  para poder utilizar sus aplicaciones y le pones el nombre de l

def main():
    menu = l.match_menu()#llama a la funcion 'match_menu' que lo que hace es generar un menu con dos opciones
    match menu:
        case 1:# en el caso que elijas la opcion '1' cojeras el primer case
            l.read_csv()
        case 2:
            l.write_csv()

if __name__ == "__main__":
    main()