import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv

# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


docs = db.collection(u'visualCR').where(u'round', u'==', '1').stream()

with open('trainee_data_blockly_test.csv', mode='w', newline='', encoding='utf-8') as trainee_csv:
    trainee_data_writer = csv.writer(trainee_csv, delimiter=';')
    trainee_data_writer.writerow(
        ['userID', 'pseudonym', 'round', 'blockly', 'points',
         'level', 'startTime', 'taskTimes', 'tries', 'ip', 
         'task1_start', 'task1_end', 'task1_hints', 'task1_points', 'task1_tlx_1', 'task1_tlx_2', 'task1_tlx_3', 'task1_tlx_4',
         'task2_start', 'task2_end', 'task2_hints', 'task2_points', 'task2_tlx_1', 'task2_tlx_2', 'task2_tlx_3', 'task2_tlx_4',
         'task3_start', 'task3_end', 'task3_hints', 'task3_points', 'task3_tlx_1', 'task3_tlx_2', 'task3_tlx_3', 'task3_tlx_4',
         'task4_start', 'task4_end', 'task4_hints', 'task4_points', 'task4_tlx_1', 'task4_tlx_2', 'task4_tlx_3', 'task4_tlx_4',
         'task5_start', 'task5_end', 'task5_hints', 'task5_points', 'task5_tlx_1', 'task5_tlx_2', 'task5_tlx_3', 'task5_tlx_4',
         'task6_start', 'task6_end', 'task6_hints', 'task6_points', 'task6_tlx_1', 'task6_tlx_2', 'task6_tlx_3', 'task6_tlx_4'])

    for doc in docs: 
        doc = doc.to_dict()
        trainee_data_writer.writerow([
            doc.get('userID'), doc.get('pseudonym'), doc.get('round'), doc.get('blockly'), doc.get('points'), 
            doc.get('level'), doc.get('startTime'), doc.get('taskTimes'), doc.get('tries'), doc.get('ip'),
            doc.get('task1_start'), doc.get('task1_end'), doc.get('task1_hints'), doc.get('task1_points'), 
            doc.get('task1_tlx')[0] if doc.get('task1_tlx') else '', doc.get('task1_tlx')[1] if doc.get('task1_tlx') else '', doc.get('task1_tlx')[2] if doc.get('task1_tlx') else '', doc.get('task1_tlx')[3] if doc.get('task1_tlx') else '',
            doc.get('task2_start'), doc.get('task2_end'), doc.get('task2_hints'), doc.get('task2_points'),
            doc.get('task2_tlx')[0] if doc.get('task2_tlx') else '', doc.get('task2_tlx')[1] if doc.get('task2_tlx') else '', doc.get('task2_tlx')[2] if doc.get('task2_tlx') else '', doc.get('task2_tlx')[3] if doc.get('task2_tlx') else '',
            doc.get('task3_start'), doc.get('task3_end'), doc.get('task3_hints'), doc.get('task3_points'),
            doc.get('task3_tlx')[0] if doc.get('task3_tlx') else '', doc.get('task3_tlx')[1] if doc.get('task3_tlx') else '', doc.get('task3_tlx')[2] if doc.get('task3_tlx') else '', doc.get('task3_tlx')[3] if doc.get('task3_tlx') else '',
            doc.get('task4_start'), doc.get('task4_end'), doc.get('task4_hints'), doc.get('task4_points'), 
            doc.get('task4_tlx')[0] if doc.get('task4_tlx') else '', doc.get('task4_tlx')[1] if doc.get('task4_tlx') else '', doc.get('task4_tlx')[2] if doc.get('task4_tlx') else '', doc.get('task4_tlx')[3] if doc.get('task4_tlx') else '',
            doc.get('task5_start'), doc.get('task5_end'), doc.get('task5_hints'), doc.get('task5_points'),
            doc.get('task5_tlx')[0] if doc.get('task5_tlx') else '', doc.get('task5_tlx')[1] if doc.get('task5_tlx') else '', doc.get('task5_tlx')[2] if doc.get('task5_tlx') else '', doc.get('task5_tlx')[3] if doc.get('task5_tlx') else '',
            doc.get('task6_start'), doc.get('task6_end'), doc.get('task6_hints'), doc.get('task6_points'),
            doc.get('task6_tlx')[0] if doc.get('task6_tlx') else '', doc.get('task6_tlx')[1] if doc.get('task6_tlx') else '', doc.get('task6_tlx')[2] if doc.get('task6_tlx') else '', doc.get('task6_tlx')[3] if doc.get('task6_tlx') else ''])
