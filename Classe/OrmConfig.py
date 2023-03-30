from Personne import Personne
from Vehicule import Vehicule
from Voiture import Voiture
from Utilitaire import Utilitaire
from Monospace import Monospace
from Camion import Camion
from Location import Location

mapping = {
        Personne : {
            "tableName": "personne",
            "mapping": [
                {
                  "colomnName" : "id",
                  "type" : "int",
                  "attributName" : "id"
                },
                {   
                    "colomnName" : "name",
                    "type" : "varchar",
                    "attributName" : "nom"
                },
                {
                    "colomnName" : "prenom",
                    "type" : "varchar",
                    "attributName" : "prenom"
                },
                {
                    "colomnName" : "date_naissance",
                    "type" : "date",
                    "attributName" : "naissance"
                }
            ]
        },
        Voiture : {
            "tableName": "voiture",
            "mapping": [
                {
                "colomnName" : "nom",
                "type" : "varchar",
                "attributName" : "nom"
                },
                {
                "colomnName" : "model",
                "type" : "varchar",
                "attributName" : "model"
                },
                {
                "colomnName" : "annee",
                "type" : "int",
                "attributName" : "annee"
                },
                {
                "colomnName" : "matricule",
                "type" : "varchar",
                "attributName" : "matricule"
                },
                {
                "colomnName" : "km",
                "type" : "int",
                "attributName" : "km"
                },
                {
                "colomnName" : "nbrplace",
                "type" : "int",
                "attributName" : "nbrplace"
                }
            ]
        },
        Monospace : {
            "tableName": "monospace",
            "mapping": [
                {
                "colomnName" : "nom",
                "type" : "varchar",
                "attributName" : "nom"
                },
                {
                "colomnName" : "model",
                "type" : "varchar",
                "attributName" : "model"
                },
                {
                "colomnName" : "annee",
                "type" : "int",
                "attributName" : "annee"
                },
                {
                "colomnName" : "matricule",
                "type" : "varchar",
                "attributName" : "matricule"
                },
                {
                "colomnName" : "km",
                "type" : "int",
                "attributName" : "km"
                },
                {
                "colomnName" : "nbrplace",
                "type" : "int",
                "attributName" : "nbrplace"
                }
            ]
        },
        Utilitaire : {
            "tableName": "utilitaire",
            "mapping": [
                {
                "colomnName" : "nom",
                "type" : "varchar",
                "attributName" : "nom"
                },
                {
                "colomnName" : "model",
                "type" : "varchar",
                "attributName" : "model"
                },
                {
                "colomnName" : "annee",
                "type" : "int",
                "attributName" : "annee"
                },
                {
                "colomnName" : "matricule",
                "type" : "varchar",
                "attributName" : "matricule"
                },
                {
                "colomnName" : "km",
                "type" : "int",
                "attributName" : "km"
                },
                {
                "colomnName" : "volume",
                "type" : "int",
                "attributName" : "volume"
                }
            ]
        },
        Camion : {
            "tableName": "camion",
            "mapping": [
                {
                "colomnName" : "nom",
                "type" : "varchar",
                "attributName" : "nom"
                },
                {
                "colomnName" : "model",
                "type" : "varchar",
                "attributName" : "model"
                },
                {
                "colomnName" : "annee",
                "type" : "int",
                "attributName" : "annee"
                },
                {
                "colomnName" : "matricule",
                "type" : "varchar",
                "attributName" : "matricule"
                },
                {
                "colomnName" : "km",
                "type" : "int",
                "attributName" : "km"
                },
                {
                "colomnName" : "tonnage",
                "type" : "int",
                "attributName" : "tonnage"
                }
            ]
        },
        Location : {
            "tableName": "location",
            "mapping": [
                {
                "colomnName" : "code",
                "type" : "varchar",
                "attributName" : "code"
                },
                {
                "colomnName" : "client",
                "type" : "int",
                "attributName" : "client"
                },
                {
                "colomnName" : "vehicule",
                "type" : "varchar",
                "attributName" : "vehicule"
                }
            ]
        }
    }