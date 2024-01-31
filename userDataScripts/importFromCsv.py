import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv

# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


with open('VMs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        ip=row[0];
        pseudonym = row[1];
        round = row[2];
        userID = "";
        doc_ref = db.collection(u'IR_VM_pseudonyms').document(ip)
        doc_ref.set({
    u'ip': ip,
    u'pseudonym': pseudonym,
    u'userID': userID,
    u'round': round

 })



