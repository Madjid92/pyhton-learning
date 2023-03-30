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
from datetime import datetime

class DBManager(DataManager) :

    user="postgres"
    password="1992"
    host="127.0.0.1"
    port="5432"
    db_name= "location_2"

    classTotab = mapping
    
    def connect() :
        return psycopg2.connect(user =DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port,
                            database = DBManager.db_name)
    
    def checkDB() :
        connection = None
        try:
            connection = psycopg2.connect(user = DBManager.user,
                            password = DBManager.password,
                            host = DBManager.host,
                            port = DBManager.port)
            print('Database connected.')
        except:
            print('Database not connected.')

        if connection is not None:
            #DBManager.connection.autocommit = True
            cur = connection.cursor()

            cur.execute("SELECT datname FROM pg_database;")

            list_database = cur.fetchall()
            connection.close()
            if (DBManager.db_name,) in list_database:
                print("'{}' Database already exist".format(DBManager.db_name))
                return True
            else:
                print("'{}' Database not exist.".format(DBManager.db_name))
                return False
           
    

        
        
    def createDB() :
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
        if(not DBManager.checkDB()) :
            # creat db and connect
            DBManager.createDB()
            connection = DBManager.connect()
            sqlQuery = DBManager.dbStructureSqlBuild()
            connection.autocommit = True
            curs = connection.cursor()
            curs.execute(sqlQuery)
            connection.close()

    def generateSelectQuery(dataType):
        query = "SELECT "
        map = DBManager.classTotab[dataType]
        
        attributNames = ()
        for value in map["mapping"]:
            query += value["colomnName"]+","
            attributNames += (value["attributName"],)
        query = query[0:len(query)-1]
        query += " from "+ map["tableName"]
        return (query,attributNames)

    def mapResult(resultat,attributList,dataType):
        objects = []
        for elm in resultat:
            obj = dataType()
            for i in range(len(elm)) :
                setattr(obj,attributList[i],elm[i])
            objects.append(obj)
        return objects
                

    def getAll(dataType):
        selectResult = DBManager.generateSelectQuery(dataType)
        selectQuery = selectResult[0]
        connexion = DBManager.connect()
        connexion.autocommit = True
        curs = connexion.cursor()
        curs.execute(selectQuery)
        selection = curs.fetchall()
        connexion.close()
        return DBManager.mapResult(selection,selectResult[1],dataType)
        
    
    def getById(id, dataType):
        return super().getById(dataType)
    
    def generateInsertQuery(data):
        mapData = mapping[type(data)]
        if(mapData == None): 
            raise "Not corresponding mapping for type"+ type(data)
        insertQuery = "INSERT into "+mapData["tableName"]+" "
        fields = "("
        values = "("

        for value in mapData["mapping"]:
            fields+=value["colomnName"]+","
            if value["type"] == "varchar" or value["type"] == "date":
                values+="'"+str(getattr(data,value["attributName"]))+"'"+","
            else:
                values+=str(getattr(data,value["attributName"]))+","
    
        fields= fields[0: len(fields)-1]+")"
        values= values[0: len(values)-1]+")"
        insertQuery+=fields+" values "+values
        return insertQuery
    
    def save(data):
        insertQuery = DBManager.generateInsertQuery(data)
        connexion = DBManager.connect()
        connexion.autocommit = True
        curs = connexion.cursor()
        curs.execute(insertQuery)
        connexion.close()

    def saveAll():
        pass

if __name__ == '__main__':
    
    per = Personne("test","test","10-10-1990")
    per1 = Personne("test1","test1","11-11-1991")
    DBManager.init()
    DBManager.save(per)
    DBManager.save(per1)
    pers = DBManager.getAll(Personne)
    for p in pers:
        print(p)
    #print(DBManager.getAll(Personne))
