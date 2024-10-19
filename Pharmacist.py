import firebase_admin
from firebase_admin import db
import requests
import copy
import os

cred_obj = firebase_admin.credentials.Certificate('<INSERT FIREBASE CREDENTIAL CERTIFICATE FILE PATH HERE>')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':"<INSERT DATABASE URL HERE>"
    })

print("\nWelcome to the Pharmacist Portal for Medicable")
print("You can make prescriptions for patients here.")
print("Enter q in the prescription field if you want to exit application.\n")

location = input("Please enter the address of your pharmacy: ")
l = copy.copy(location)
location = location.replace(' ','%20')
location = location.replace('+','%2B')
url = "https://geocode.maps.co/search?q={}&api_key=670d447275180331827086mwlb29f9b".format(location)
response = requests.get(url)
data = response.json()

lat = data[0]['lat']
lng = data[0]['lon']
            
print('\nOk, here is your to-do list:')
ref = db.reference("/users").get()
d = ref['medicines'].split(',')
for t in d:
    print(t)


prescription = input("Enter the full name of the completed prescription and the patient: ")

while prescription!='q':
    
    selectedPrescription = copy.copy(prescription)
    ref = db.reference("/users/patients")
    selectedPrescription = selectedPrescription.split(' - ')
    ref.child(selectedPrescription[1]).update({"location":l})
    ref.child(selectedPrescription[1]).update({"latitude":lat})
    ref.child(selectedPrescription[1]).update({"longitude":lng})

    d.remove(prescription)
    ref = db.reference("/users")
    if len(d) == 0:
        ref.update({"medicines":""})
    else:
        ref.update({"medicines":d})
    os.system('cls')

    if len(d)!=0:
        print('\nOk, here is your updated to-do list:')
        ref = db.reference("/users/").get()
        print(ref)
        d = ref.get()['medicines'].split(',')
        for t in d:
            print(t)

        prescription = input("Enter the full name of the completed prescription and the patient: ")
    
    else:
        print("Ok! Your tasks are done for now, please check back later to see if there are any pending prescriptions.")
        break