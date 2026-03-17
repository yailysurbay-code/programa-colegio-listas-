import re
import random
colegio="ADSO.COM"
contraseña_cor="3174404"
usuario_cor="adso123"
i=1
con2=0
con1=0
#definiciones de rol
while True:
    while True:
        try:
            print("-------------------BUENOS DIAS BIENVENIDO---------------")
            print("======Menu principal========")
            print("Elige el rol con el que quiere continuar")
            print("Ingrese 1 si desea continuar como cordinador")
            print("ingrese 2 si desea continuar como profesor")
            print("ingrese 3 si desea continuar como estudiante")
            rol=int(input())
            if rol==1 or rol==2 or rol==3:
                break
        except ValueError:
                print("ingrese un numero de la lista😞 ")
    if rol==1: #funciones como cordinador
        nom_cor=input("Señor(a) cordinador ingrese su nombre:  ")
        usuario=input(f"señor(a) {nom_cor} ingrese su usuario:  ")
        contraseña=input(f"señor(a) {nom_cor} ingrese su contraseña de acceso:  ")
        if usuario==usuario_cor and contraseña==contraseña_cor:
            print("datos correctos")
        else:
            print("intente nuevamente")
            for i in range(2): #3 intentos de contraseña
                usuario=input(f"señor(a) {nom_cor} ingrese su usuario:  ")
                contraseña=input(f"señor(a) {nom_cor} ingrese su contraseña de acceso:  ")
                if usuario==usuario_cor and contraseña==contraseña_cor:
                    print("datos correctos")
                    break
                else:
                    print("intente nuevamente")
        op=1
        while op==1:
            while True:
                try:
                    print("===========Menu de opciones==================")
                    print("...............Elige que desea agregar................") 
                    print("Ingrese (1) para agragar estudiantes")
                    print("Ingrese (2) para agregar profesores")
                    print("Ingrese (3) para ver la lista de estudiantes agregados")
                    div=int(input())
                    
                        break
                except ValueError:
                    print("Ingrese un numero de la lista")
            lista_estu=[]
            if div==1: #validar documento estudiantes
                while True:
                    try:
                        can_est=int(input("ingrese la cantidad de estudiantes que desea validar:  "))
                        break
                    except ValueError:
                        print("Error: ingrese un numero entero😞 ")
                for i in range(can_est):
                    con1=con1+1
                    while True:
                         documento_est=input(f"ingrese el numero de documento del estudiante :  ")
                         if re.fullmatch(r"\d{6,10}", documento_est):
                                print("Documento válido.")
                                break
                         else:
                            print("Error: debe contener entre 6 y 10 dígitos.")
                    lista_estu.append(documento_est)
                op=int(input("Desea volver al menu de opciones ingrese (1) para SI o (2) para NO: "))
            lista_profe=[]
            if div==2: #validar documento de profesores
                while True:
                    try:
                        can_profe=int(input("ingrese cantidad de profesores que desea validar:  "))
                        if can_profe <=6:
                            break
                    except ValueError:
                        print("Error: ingrese un numero entero😞")
                
                for i in range(can_profe):
                    con2=con2+1
                    while True:
                        documento_profe=input(f"ingrese el numero de documento del profesore :  ")
                        if re.fullmatch(r"\d{6,10}", documento_profe):
                                print("Documento válido.")
                                break
                        else:
                            print("Error: debe contener entre 6 y 10 dígitos.")
                    lista_profe.append(documento_profe)
                op=int(input("Desea volver al menu de opciones ingrese (1) para SI o (2) para NO: "))
            if div==3: #ver lista de estudiantes agregados
                if len(lista_estu) ==0:
                    print("no a ingresado ningun estudiante 😞")
                    while True:
                        try:
                            decision=int(input("¿desea agregar algun estudiante? ingrese (1) si su respuesta es SI o (2) si su respuesta es NO: "))
                            if decision==1 or decision==2:
                                break
                        except ValueError:
                            print("Error: ingrese una de las opciones 😞")
                    if decision==1: 
                        while True:
                            try:
                                can_est=int(input("ingrese la cantidad de estudiantes que desea validar:  "))
                                break
                            except ValueError:
                                print("Error: ingrese un numero entero")
                        for i in range(can_est):
                            while True:
                                 documento_est=input(f"ingrese el numero de documento del estudiante:  ")
                                 if re.fullmatch(r"\d{6,10}", documento_est):
                                        print("Documento válido.")
                                        break
                                 else:
                                    print("Error: debe contener entre 6 y 10 dígitos.")
                            lista_estu.append(documento_est)
                        print("Validacion exitosa") 
                    else:
                        print(f"gracias por responder {nom_cor} 😊")
                else:
                    print(f"los estudiantes agregados son \n{lista_estu }")
                op=int(input("Desea volver al menu de opciones ingrese (1) para SI o (2) para NO: "))
    if rol==2 or rol==3:
        if con1==0 and con2==0:
                    print("Es necesario el ingreso del cordinador antes")
                    break
    usiarios_existe_profe=[]
    if rol==2:
        while True:
            doc_profe=input("ingrese su numero de documento para verificar informacion")
            if re.fullmatch(r"\d{6,10}", doc_profe):
                print("Documento válido.")
                break
            else:
                print("Error: debe contener entre 6 y 10 dígitos.")
        if doc_profe in lista_profe:
               prinom_profe = input("Primer nombre: ").strip().lower()
               segnom_profe = input("Segundo nombre: ").strip().lower()
               apellido_profe = input("Apellido: ").strip().lower()
               if prinom_profe== "" or segnom_profe=="" or apellido_profe=="":
                   print("Error:debe ingresar primer nombre, segundo nombre y apellido")
               else:
                   usuario_profe = prinom_profe[0] + segnom_profe[0] + apellido_profe

                   if usuario_profe in usiarios_existe_profe:
                       caracteres = ["!#$%&@"]
                       usuario_profe += random.choice(caracteres)
                       usiarios_existe_profe.append(usuario_profe)
                   print("su usuario es", usuario_profe)
                   
                    
   
    
    
  
