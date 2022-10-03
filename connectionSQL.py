import sqlite3


class ConnectionDatabase:

    def __init__(self):
        self.conn = None

    def getConn(self):
        try:
            self.conn = sqlite3.connect('identifier.sqlite')
        except:
            print('error al connectar a la base de datos')

    def closeConn(self):
        try:
            self.conn.close()
        except:
            print('No se pudo cerrar la conneccion')

    def insert(self, nombre, apellido, telefono, direccion):
        try:
            self.conn.execute(
                "INSERT INTO Person (LastName, FirstName, Phone, Residence) values ('" + str(apellido) + "','" + str(
                    nombre) + "','" + str(telefono) + "','" + str(direccion) + "');")
            self.conn.commit()
        except:
            print('Error al insertar datos')

    def getLen(self):
        numero_personas = self.conn.execute('select count(*) from Person')
        return numero_personas.fetchone()[0]
    def insertDefault(self,personas):
        if int(personas) > 0:
            for i in range(int(personas)):
                self.conn.execute("INSERT INTO Person (LastName, FirstName, Phone, Residence) values ('apellido','nombre','0979290014','mi casa');")
                self.conn.commit()
        else:
            personas = -1 * int(personas)
            print(personas)
            table = self.conn.execute("SELECT * FROM Person ORDER BY PersonID DESC LIMIT "+str(personas)+";")
            for row in table:
                self.conn.execute("DELETE FROM Person WHERE PersonID="+str(row[0])+";")
                self.conn.commit()



