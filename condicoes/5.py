login = str(input("digite o seu login "))
senha = str(input("digite a sua senha "))

match login, senha:
    case ("admin", "admin_pass"):
        print("bem-vindo meu lindo")
        
    case ("user", "user_pass"):
        print("bem-vindo meu amigão")
        
    case ("guest", _):
        print("bem-vindo meu parça")
        
    case (_, _):
        print("desconhecido")
    
        