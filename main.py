from hmac import compare_digest
import string
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
#mycursor.execute("CREATE TABLE pago (ID VARCHAR(255), Cantidad VARCHAR(255), Concepto VARCHAR(255), Fecha VARCHAR(255), Banco VARCHAR(255))")
#mycursor.execute("CREATE TABLE inventario (ID VARCHAR(255), Producto VARCHAR(255), Cantidad VARCHAR(255), Categoria VARCHAR(255), Modelo VARCHAR(255))")
#mycursor.execute("CREATE TABLE vendedor (ID VARCHAR(255), Nombre VARCHAR(255), Apellidos VARCHAR(255), Puesto VARCHAR(255))")

#mycursor.execute("CREATE TABLE logs_usuario (ID VARCHAR(255), Nombre VARCHAR(255), Apellidos VARCHAR(255), Direccion VARCHAR(255), Telefono VARCHAR(10))")
#mycursor.execute("CREATE TABLE logs_cuentausuario (ID VARCHAR(255),nombreUsuario VARCHAR(255), Contraseña VARCHAR(255))")
#mycursor.execute("CREATE TABLE logs_compra (ID VARCHAR(255),Producto VARCHAR(255),Categoria VARCHAR(255),Modelo VARCHAR(255),Cantidad INT(255))")
#mycursor.execute("CREATE TABLE logs_pago (ID VARCHAR(255), Cantidad VARCHAR(255), Concepto VARCHAR(255), Fecha VARCHAR(255), Banco VARCHAR(255))")
#mycursor.execute("CREATE TABLE logs_inventario (ID VARCHAR(255), Producto VARCHAR(255), Cantidad VARCHAR(255), Categoria VARCHAR(255), Modelo VARCHAR(255))")
#mycursor.execute("CREATE TABLE logs_vendedor (ID VARCHAR(255), Nombre VARCHAR(255), Apellidos VARCHAR(255), Puesto VARCHAR(255))")
#mycursor.execute("""
#CREATE TRIGGER after_update_cuentausuario
#BEFORE UPDATE ON cuentausuario
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_cuentausuario(ID,nombreUsuario,Contraseña) VALUES(
#			OLD.ID,OLD.nombreUsuario,OLD.Contraseña
#		);
#END
#""")

#mycursor.execute("""
#CREATE TRIGGER after_update_usuario
#BEFORE UPDATE ON usuario
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_usuario(ID,Nombre,Apellidos,Direccion,Telefono) VALUES(
#			OLD.ID,OLD.Nombre,OLD.Apellidos,OLD.Direccion,OLD.Telefono
#		);
#END
#""")

#mycursor.execute("""
#CREATE TRIGGER after_update_compra
#BEFORE UPDATE ON compra
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_compra(ID,Producto,Categoria,Modelo,Cantidad) VALUES(
#			OLD.ID,OLD.Producto,OLD.Categoria,OLD.Modelo,OLD.Cantidad
#		);
#END
#""")

#mycursor.execute("""
#CREATE TRIGGER after_update_pago
#BEFORE UPDATE ON pago
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_pago(ID,Cantidad,Concepto,Fecha,Banco) VALUES(
#			OLD.ID,OLD.Cantidad,OLD.Concepto,OLD.Fecha,OLD.Banco
#		);
#END
#""")

#mycursor.execute("""
#CREATE TRIGGER after_update_vendedor
#BEFORE UPDATE ON vendedor
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_vendedor(ID,Nombre,Apellidos,Puesto) VALUES(
#			OLD.ID,OLD.Nombre,OLD.Apellidos,OLD.Puesto
#		);
#END
#""")

#mycursor.execute("""
#CREATE TRIGGER after_update_inventario
#BEFORE UPDATE ON inventario
#FOR EACH ROW
#BEGIN
#  INSERT INTO logs_inventario(ID,Producto,Cantidad,Categoria,Modelo) VALUES(
#			OLD.ID,OLD.Producto,OLD.Cantidad,OLD.Categoria,OLD.Modelo
#		);
#END
#""")

while menuOp != 0:
    
    print("***********BIENVENIDO******************")
    print("*[0] Salir                            *")
    print("*[1] Agregar Registro                 *")
    print("*[2] Eliminar Registro                *")
    print("*[3] Eliminar Registro(Rango)         *")
    print("*[4] Consultar Tablas                 *")
    print("*[5] Modificar Registro               *")
    print("*[6] Imprimir Registros               *")
    print("*[7] Imprimir Registros(Coincidencia) *")
    print("********************************\n")
    print("Selecciona una opcion")
    menuOp = int(input())

    if menuOp == 1:
        print("Ha ingresado a *Agregar registro*")
        print("[0] Compra          [1] Cuenta_Usuario      [2] Usuario")
        print("[3] Pago            [4] Inventario          [5] Vendedor")
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
        elif op == 3:
            print("Digite el ID: ")
            Id = str(input())
            print("Digite la Cantidad: ")
            Cantidad = str(input())
            print("Digite el producto: ")
            Concepto = str(input())
            print("Digite la fecha (DIA/MES/AÑO sin diagonales): ")
            Fecha = str(input())
            print("Digite el Banco: ")
            Banco = str(input())
            string2 = "INSERT INTO pago (ID, Cantidad, Concepto, Fecha, Banco) VALUES ('{id}','{cantidad}','{concepto}','{fecha}','{banco}')".format(id=Id,cantidad=Cantidad,concepto=Concepto,fecha=Fecha,banco=Banco)
            mycursor.execute(string2)
            mydb.commit()
            print("\nREGISTRO AGREGADO")
        elif op == 4:
            print("Digite el ID: ")
            Id = str(input())
            print("Digite el Producto: ")
            Producto = str(input())
            print("Digite el Cantidad: ")
            Cantidad = str(input())
            print("Digite la Categoria: ")
            Categoria = str(input())
            print("Digite el Modelo: ")
            Modelo = str(input())
            string2 = "INSERT INTO inventario (ID, Producto, Cantidad, Categoria, Modelo) VALUES ('{id}','{producto}','{cantidad}','{categoria}','{modelo}')".format(id=Id,producto=Producto,cantidad=Cantidad,categoria=Categoria,modelo=Modelo)
            mycursor.execute(string2)
            mydb.commit()
            print("\nREGISTRO AGREGADO")
        elif op == 5:
            print("Digite el ID: ")
            Id = str(input())
            print("Digite el nombre/s: ")
            Nombre = str(input())
            print("Digite el apellido/s: ")
            Apellido = str(input())
            print("Digite el puesto: ")
            Puesto = str(input())
            string2 = "INSERT INTO vendedor (ID, Nombre, Apellidos,Puesto) VALUES ('{id}','{nombre}','{apellidos}','{puesto}')".format(id=Id,nombre=Nombre,apellidos=Apellido,puesto=Puesto)
            mycursor.execute(string2)
            mydb.commit()
            print("\nREGISTRO AGREGADO")

    elif menuOp == 2:
        print("Ha ingresado a *Eliminar Registro*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("[3] Pago            [4] Inventario         [5] Vendedor")
        print("Digite el numero de la tabla a la que desea acceder: ")
        compare = int(input())
        print("Digite el Id del registro a eliminar: ")
        Id = str(input())
        if (compare > 5) & (compare < 0):
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
            elif compare == 3:
                Tabla = "pago"
            elif compare == 4:
                Tabla = "inventario"
            elif compare == 5:
                Tabla = "vendedor"
            delete = "DELETE FROM {tabla} WHERE Id='{id}'".format(tabla=Tabla,id=Id)
            mycursor.execute(delete)
            mydb.commit()
            print("REGISTRO ELIMINADO")
            os.system("cls")
    
    elif menuOp == 3:
        print("Ha ingresado a *Eliminar Registro(Rango)*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("[3] Pago            [4] Inventario         [5] Vendedor")
        print("Digite el numero de la tabla a la que desea acceder: ")
        compare2 = int(input())
        print("Digite el Id del limite inferio desde el cual desea eliminar todos los registros: ")
        Id = str(input())
        if (compare2 > 5) & (compare2 < 0):
            os.system("cls")
            print("Tabla no existente...")
            os.system("cls")
        else:
            if compare2 == 0:
                Tabla = "compra"
            elif compare2 == 1:
                Tabla = "cuentausuario"
            elif compare2 == 2:
                Tabla = "usuario"
            elif compare == 3:
                Tabla = "pago"
            elif compare == 4:
                Tabla = "inventario"
            elif compare == 5:
                Tabla = "vendedor"
            delete = "DELETE FROM {tabla} WHERE Id>'{id}'".format(tabla=Tabla,id=Id)
            mycursor.execute(delete)
            mydb.commit()
            print("REGISTRO ELIMINADO")
            os.system("cls")

    elif menuOp == 4:
        print("Ha ingresado a *Consultar Registros*")
        mycursor.execute("Show tables;") 
        myresult = mycursor.fetchall()   
        for x in myresult: 
            print(x)
    elif menuOp == 5:
        print("Ha ingresado a *Modificar Registro*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("[3] Pago            [4] Inventario         [5] Vendedor")
        print("Digite el numero de la tabla a la que desea acceder: ")
        compare = int(input())
        print("Digite el Id del registro a modificar: ")
        Id = str(input())
        if (compare > 5) & (compare < 0):
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
            elif compare == 3:
                oldID = Id
                print("Digite el ID: ")
                Id = str(input())
                print("Digite la Cantidad: ")
                Cantidad = str(input())
                print("Digite el producto: ")
                Concepto = str(input())
                print("Digite la fecha (DIA/MES/AÑO sin diagonales): ")
                Fecha = str(input())
                print("Digite el Banco: ")
                Banco = str(input())
                string2 = "UPDATE pago SET ID='{id}',Cantidad='{cantidad}',Concepto='{concepto}',Fecha='{fecha}',Banco='{banco}' WHERE ID='{old}'".format(id=Id,cantidad=Cantidad,concepto=Concepto,fecha=Fecha,banco=Banco,old=oldID)
                mycursor.execute(string2)
                mydb.commit()
                print("REGISTRO MODIFICADO")
            elif compare == 4:
                oldID = Id
                print("Digite el ID: ")
                Id = str(input())
                print("Digite el Producto: ")
                Producto = str(input())
                print("Digite el Cantidad: ")
                Cantidad = str(input())
                print("Digite la Categoria: ")
                Categoria = str(input())
                print("Digite el Modelo: ")
                Modelo = str(input())
                string0 = "UPDATE inventario SET ID='{id}',Producto='{producto}',Categoria='{categoria}',Modelo='{modelo}',Cantidad='{cantidad}' WHERE ID='{old}'".format(id=Id,producto=Producto,categoria=Categoria,modelo=Modelo,cantidad=Cantidad,old=oldID)
                mycursor.execute(string0)
                mydb.commit()
                print("REGISTRO MODIFICADO")
            elif compare == 5:
                oldID = Id
                print("Digite el ID: ")
                Id = str(input())
                print("Digite el nombre/s: ")
                Nombre = str(input())
                print("Digite el apellido/s: ")
                Apellido = str(input())
                print("Digite el puesto: ")
                Puesto = str(input())
                string0 = "UPDATE vendedor SET ID='{id}',Nombre='{nombre}',Apellidos='{apellido}',Puesto='{puesto}' WHERE ID='{old}'".format(id=Id,nombre=Nombre,apellido=Apellido,puesto=Puesto,old=oldID)
                mycursor.execute(string0)
                mydb.commit()
                print("REGISTRO MODIFICADO")
    elif menuOp == 6:
        print("Ha ingresado a *Imprimir registros*")
        print("[0] Compra          [1] CuentaUsuario      [2] Usuario")
        print("[3] Pago            [4] Inventario         [5] Vendedor")
        print("Digite el numero de la tabla de la que desea imprimir los registros: ")
        compare3 = int(input())
        if (compare3 > 5) & (compare3 < 0):
            os.system("cls")
            print("Tabla no existente...")
            os.system("cls")
        else:
            if compare3 == 0:
                view = "CREATE OR REPLACE VIEW view1 AS SELECT ID,Producto,Categoria,Modelo,Cantidad FROM compra;"
                conteo = "SELECT * FROM view1;"
            elif compare3 == 1:
                view = "CREATE OR REPLACE VIEW view2 AS SELECT ID,nombreUsuario,Contraseña FROM cuentausuario;"
                conteo = "SELECT * FROM view2;"
            elif compare3 == 2:
                view = "CREATE OR REPLACE VIEW view3 AS SELECT ID,Nombre,Apellidos,Direccion,Telefono FROM usuario;"
                conteo = "SELECT * FROM view3;"
            elif compare3 == 3:
                view = "CREATE OR REPLACE VIEW view4 AS SELECT ID,Cantidad,Concepto,Fecha,Banco FROM pago;"
                conteo = "SELECT * FROM view4;"
            elif compare3 == 4:
                view = "CREATE OR REPLACE VIEW view5 AS SELECT ID,Producto,Categoria,Modelo,Cantidad FROM inventario;"
                conteo = "SELECT * FROM view5;"   
            elif compare3 == 5:
                view = "CREATE OR REPLACE VIEW view6 AS SELECT ID,Nombre,Apellidos,Puesto FROM vendedor;"
                conteo = "SELECT * FROM view6;"
                
            mycursor.execute(conteo)
            data = mycursor.fetchall()
            for res in data:
                print(res, "\n--------------")
            os.system("pause")
    elif menuOp == 7:
        print("Ha ingresado a *Imprimir Registros(Coincidencia)*")
        print("[1] CuentaUsuario      [2] Usuario")
        print("Digite el numero de la tabla en la que desea encontrar las compras por usuario: ")
        search = int(input())
        if (search > 2) | (search < 1):
            os.system("cls")
            print("Tabla no existente...")
            os.system("cls")
        else:
            if search == 1:
                sentence = "SELECT x.ID,x.nombreUsuario,y.Producto from cuentausuario x left join compra y on x.ID = y.ID"
            elif search == 2:
                sentence = sentence = "SELECT x.ID,x.Nombre,y.Producto from usuario x left join compra y on x.ID = y.ID"    
        mycursor.execute(sentence)
        data = mycursor.fetchall()
        for i in data:
            print(i, "\n-----------------")    
        os.system("pause")
        






