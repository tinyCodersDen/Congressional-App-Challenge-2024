import firebase_admin
from firebase_admin import db
import os

cred_obj = firebase_admin.credentials.Certificate('<INSERT FIREBASE CREDENTIAL CERTIFICATE FILE PATH HERE>')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':"<INSERT DATABASE URL HERE>"
    })
ref = db.reference("/users/patients")

print("\nWelcome to the Doctor Portal for Medicable")
print("You can add prescriptions for patients here.")
print("Enter None for prescriptions field to remove patient's prescription.")
print("Enter q in the fields if you want to exit application.\n")

patient = input("Enter the patient's First and Last Name without spaces: ")
prescription = input("Enter the prescription: ")

while patient !='q' and prescription != 'q':
    
    os.system('cls')
    ref = db.reference("/users/patients")
    ref.child(patient).update({"prescriptions":prescription})

    ref = db.reference("/users")
    if ref.get()['medicines']=="":
        ref.update({"medicines":prescription+' - '+patient})
    else:
        if prescription != "None":
            ref.update({"medicines":ref.get()['medicines']+","+prescription+' - '+patient})
    
    print("\nDone!\n")
    patient = input("Enter the patient's First and Last Name without spaces: ")
    prescription = input("Enter the prescription (enter q to quit): ")