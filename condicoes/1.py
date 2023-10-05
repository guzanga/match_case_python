inp = int(input("digite um numero de um a três"))

match inp:
    case 1:
        print("amarelo")

    case 2:
        print("azul")
        
    case 3:
        print("verde")
    
    case _:
        print("sem cor")