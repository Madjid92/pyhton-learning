from Personne import Personne
from Vehicule import Vehicule
from Voiture import Voiture
from Utilitaire import Utilitaire
from Monospace import Monospace
from Camion import Camion
from Location import Location
from DataManger import DataManager
import psycopg2
from OrmConfig import mapping

class DBManager(DataManager) :

    connection = None
    user="postgres"
    password="1992"
    host="127.0.0.1"
    port="5432"
    db_name= "location_2"

    classTotab = mapping

    tableToClass = {} 

    def createTableToClassMap() :
        DBManager.tableToClass = {}
        for curretKey, currentValue in DBManager.classTotab.items():
            key = currentValue["tableName"]
            value = {"classModel": curretKey,
                     "mapping" : currentValue["mapping"]
                    }
            DBManager.tableToClass[key] = value


    def checkDB() :
        try:
            DBManager.connection = psycopg2.connect(user = DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port)
            print('Database connected.')
        except:
            print('Database not connected.')

        if DBManager.connection is not None:
            #DBManager.connection.autocommit = True
            cur = DBManager.connection.cursor()

            cur.execute("SELECT datname FROM pg_database;")

            list_database = cur.fetchall()

            if (DBManager.db_name,) in list_database:
                print("'{}' Database already exist".format(DBManager.db_name))
                DBManager.connection.close()
                DBManager.connection = psycopg2.connect(user =DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port,
                            database = DBManager.db_name)
                return True
            else:
                print("'{}' Database not exist.".format(DBManager.db_name))
                DBManager.connection.close()
                DBManager.connection = None
                return False
        
        
        
    def createAndConnectToDB() :
        DBManager.connection = psycopg2.connect(user = DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port)
        DBManager.connection.autocommit = True
        cursor = DBManager.connection.cursor()
        sql = "CREATE database location_2"
        cursor.execute(sql)
        print("Database location_2 created successfully........")
        DBManager.connection.close()
        DBManager.connection = psycopg2.connect(database = DBManager.db_name,
                            user = DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port)
        return 
    
    def dbStructureSqlBuild() :
        query = ""
        for currentValue in DBManager.classTotab.values():
            query += "CREATE table "+currentValue["tableName"]+"("
         
            for value in currentValue["mapping"]:
                query += value["colomnName"]+" "+value["type"]+","
            query = query[0: len(query)-1]
            query += ");\n"
        return query
        
    
        
    def init():
        if(DBManager.connection != None):
            return 
        DBManager.createTableToClassMap()
        if(not DBManager.checkDB()) :
            # creat db and connect
            DBManager.createAndConnectToDB()
            sqlQuery = DBManager.dbStructureSqlBuild()
            DBManager.connection.autocommit = True
            curs = DBManager.connection.cursor()
            curs.execute(sqlQuery)

    def getAll(dataType):
        return super().getAll()
    
    def getById(id, dataType):
        return super().getById(dataType)
    
    def save(data):
        return super().save()
    
    def saveAll():
        pass


if __name__ == '__main__':
    DBManager.init()
    
    

    '''curs = connection.cursor()
    # Execute a query
    curs.execute("SELECT * FROM public.personne where personne.id = 1")

    # Retrieve query results
    records = curs.fetchall()
    for i in range(len(records)) :
        print(records[i])'''