from hmac import compare_digest
from traceback import print_tb
import mysql.connector
import os

mydb = mysql.connector.connect(host='localhost',user='root',
                                passwd='Haxorus12',db='dbtest', port='3306' )
menuOp = -1
op = 0



mycursor = mydb.cursor()


#mycursor.execute("CREATE TABLE Usuario (ID VARCHAR(255), Nombre VARCHAR(255), Apellidos VARCHAR(255), Direccion VARCHAR(255), Telefono VARCHAR(10))")
#mycursor.execute("CREATE TABLE cuentaUsuario (ID VARCHAR(255),nombreUsuario VARCHAR(255), Contraseña VARCHAR(255))")
#mycursor.execute("CREATE TABLE Compra (ID VARCHAR(255),Producto VARCHAR(255),Categoria VARCHAR(255),Modelo VARCHAR(255),Cantidad INT(255))")


while menuOp != 0:
    print("***********BIENVENIDO***********")
    print("*[0] Salir                     *")
    print("*[1] Agregar Registro          *")
    print("*[2] Eliminar Registro         *")
    print("*[3] Consultar Registro        *")
    print("*[4] Modificar Registro        *")
    print("********************************\n")
    print("Selecciona una opcion")
    menuOp = int(input())

    if menuOp == 1:
        print("Ha ingresado a *Agregar registro*")
        print("[0] Compra          [1] Cuenta_Usuario      [2] Usuario")
        print("Seleccione la tabla en la que desea agregar: \n")
        op = int(input())
        if op == 0:
            print("Digite el ID: ") 
            Id = str(input())
            print("Digite el producto: ")
            Producto = str(input())
            print("Digite la categoria: ")
            Categoria = str(input())
            print("Digite el modelo: ")
            Modelo = str(input())
            print("Digite la cantidad: ")
            Cantidad = int(input())
            string0 = "INSERT INTO compra (ID,Producto,Categoria,Modelo,Cantidad) VALUES ('{id}','{producto}','{categoria}','{modelo}','{cantidad}')".format(id=Id,producto=Producto,categoria=Categoria,modelo=Modelo,cantidad=Cantidad)
            mycursor.execute(string0)
            mydb.commit()
            print("\nREGISTRO AGREGADO")
        elif op == 1:
            print("Digite el ID: ")
            Id = str(input())
            print("Digite el nombre de usuario: ")
            userName = str(input())
            print("Digite la contraseña: ")
            password = str(input())
            string1 = "INSERT INTO cuentausuario (id, nombreUsuario, Contraseña) VALUES ('{id}','{nombreUsuario}','{Contraseña}')".format(id = Id, nombreUsuario=userName, Contraseña=password)
            mycursor.execute(string1)
            mydb.commit()
            print("\nREGISTRO AGREGADO")
        elif op == 2:
            print("Digite el ID: ")
            Id = str(input())
            print("Digite el nombre/s: ")
            Nombre = str(input())
            print("Digite el apellido/s: ")
            Apellido = str(input())
            print("Digite la direccion: ")
            Direccion = str(input())
            print("Digite el telefono: ")
            Telefono = int(input())
            string2 = "INSERT INTO usuario (ID, Nombre, Apellidos, Direccion, Telefono) VALUES ('{id}','{nombre}','{apellidos}','{direccion}','{telefono}')".format(id=Id,nombre=Nombre,apellidos=Apellido,direccion=Direccion,telefono=Telefono)
            mycursor.execute(string2)
            mydb.commit()
            print("\nREGISTRO AGREGADO")

    elif menuOp == 2:
        print("Ha ingresado a *Eliminar Registro*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("Digite el Id del registro a eliminar: ")
        Id = str(input())
        print("Digite el numero de la tabla a la que desea acceder: ")
        compare = int(input())
        if (compare > 2) & (compare < 0):
            os.system("cls")
            print("Tabla no existente...")
            os.system("cls")
        else:
            if compare == 0:
                Tabla = "compra"
            elif compare == 1:
                Tabla = "cuentausuario"
            elif compare == 2:
                Tabla = "usuario"
            delete = "DELETE FROM {tabla} WHERE Id='{id}'".format(tabla=Tabla,id=Id)
            mycursor.execute(delete)
            mydb.commit()
            print("REGISTRO ELIMINADO")
            os.system("cls")

    elif menuOp == 3:
        print("Ha ingresado a *Consultar Registros*")
        mycursor.execute("Show tables;") 
        myresult = mycursor.fetchall()   
        for x in myresult: 
            print(x)
    elif menuOp == 4:
        print("Ha ingresado a *Modificar Registro*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("Digite el numero de la tabla a la que desea acceder: ")
        compare = int(input())
        print("Digite el Id del registro a modificar: ")
        Id = str(input())
        if (compare > 2) & (compare < 0):
            os.system("cls")
            print("Tabla no existente...")
            os.system("cls")
        else:
            if compare == 0:
                oldID = Id
                Tabla = "compra"
                print("Digite el nuevo ID")
                Id = str(input())
                print("Digite el producto: ")
                Producto = str(input())
                print("Digite la categoria: ")
                Categoria = str(input())
                print("Digite el modelo: ")
                Modelo = str(input())
                print("Digite la cantidad: ")
                Cantidad = int(input())
                string0 = "UPDATE compra SET ID='{id}',Producto='{producto}',Categoria='{categoria}',Modelo='{modelo}',Cantidad='{cantidad}' WHERE ID='{old}'".format(id=Id,producto=Producto,categoria=Categoria,modelo=Modelo,cantidad=Cantidad,old=oldID)
                mycursor.execute(string0)
                mydb.commit()
                print("REGISTRO MODIFICADO")
            elif compare == 1:
                oldID = Id
                Tabla = "cuentausuario"
                print("Digite el nuevo ID: ")
                Id = str(input())
                print("Digite el nombre de usuario: ")
                userName = str(input())
                print("Digite la contraseña: ")
                password = str(input())
                string1 = "UPDATE cuentausuario SET ID='{id}',nombreUsuario='{username}',Contraseña='{contraseña}' WHERE ID='{old}'".format(id=Id,username=userName,contraseña=password,old=oldID)
                mycursor.execute(string1)
                mydb.commit()
                print("REGISTRO MODIFICADO")
            elif compare == 2:
                oldID = Id
                Tabla = "usuario"
                print("Digite el nuevo ID: ")
                Id = str(input())
                print("Digite el nombre: ")
                Nombre = str(input())
                print("Digite el apellido/s: ")
                Apellido = str(input())
                print("Digite la direccion: ")
                Direccion = str(input())
                print("Digite el telefono: ")
                Telefono = str(input())
                string2 = "UPDATE usuario SET ID='{id}',Nombre='{nombre}',Apellidos='{apellido}',Direccion='{direccion}',Telefono='{telefono}' WHERE ID='{old}'".format(id=Id,nombre=Nombre,apellido=Apellido,direccion=Direccion,telefono=Telefono,old=oldID)
                mycursor.execute(string2)
                mydb.commit()
                print("REGISTRO MODIFICADO")

        
        

#mycursor.execute("DROP TABLE clientes")
#mydb.commit()





