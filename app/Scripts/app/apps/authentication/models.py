
from django.db import models

# Create your models here.
from pymongo import MongoClient
from datetime import datetime
from pymongo.errors import DuplicateKeyError
# from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, AutoReconnect

class PatientPerscription:
    def addnewprescription(self,uname,fname,lname,dob,mail,gen,hospital,dname,dd,df,PrescriptionD,PrescriptionDur,exdate,mname,strength,instruction,admit,admitdate,dischargeDate,instruction1,Operation,operationDate,surgeon,operationDetails):
        stat={}
        try:
            client = MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
            db=client["patient"]
            coll=db["PerscriptionDetails"]
            dic={}
            dic['Username']=uname
            dic['First Name']=fname
            dic['Last Name']=lname
            dic['Date-of-Birth']=dob
            dic['Gender']=gen
            dic['email']=mail
            dic['Hospital Name']=hospital
            dic['Doctor Name']=dname
            dic['Doctor Degree']=dd
            dic['Hospital Addiliation']=df
            dic['Prescription Date']=PrescriptionD
            dic['Prescription Duration']=PrescriptionDur
            dic['Expirationdate']=exdate
            dic['Medicine Name']=mname
            dic['strength']=strength
            dic['Instruction for Medicine Intake']=instruction
            dic['Admitted']=admit
            dic['Admit Date']=admitdate
            dic['Discharge Date']=dischargeDate
            dic['Instruction while Admitted']=instruction1
            dic['Operationed']=Operation
            dic['operation Date']=operationDate
            dic['Surgeon Name']=surgeon
            dic['operationDetails']=operationDetails

            coll.insert_one(dic)
            stat['msg']='Registered Successfully'
        except DuplicateKeyError as err:
            print("exception: "+str(err))
            stat['err']='Number already exist'
        except Exception as err:
            print("exception: "+str(err))
            stat['err']='Oops! Something went wrong'
        return stat

