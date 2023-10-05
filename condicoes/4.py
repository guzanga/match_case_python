animais = str(input("digite um animal da fazenda"))

match animais:
    case "ovelha":
        print("é ovelha")
    case "galinha":
        print("é galinha")
    case "vaca":
        print("é vaca")
        
    case _:
        print("animal desconhecido")