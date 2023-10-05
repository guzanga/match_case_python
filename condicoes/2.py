cor =  str(input("fale um cor"))

match cor:
    case "verde":
        print("é verde")
        
    case "azul":
        print("é azul")
        
    case "vermelho":
        print("é vermelho")
        
    case _:
        print("com não identificada")