
import csv, json
from datetime import datetime

with open('C:/Users/LocalAdmin/Nextcloud/Iceberg_Evaluation/Evaluation/timeDataIR.csv', mode='w', newline='',
          encoding='utf-8') as time_csv:
    trainee_data_writer = csv.writer(time_csv, delimiter=';')
    trainee_data_writer.writerow(['userID', 'startTime', 'endTime', 'duration'])

with open("C:/Users/LocalAdmin/Nextcloud/Iceberg_Evaluation/Evaluation/RawDataFirebase/taskTimes.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        userID=row[0];
        startTime = row[1];
        startTime= startTime[:-6]
        startTime = datetime.fromisoformat(startTime)
        taskTimesRaw = row[2]
        taskTimesRaw = eval(taskTimesRaw)
        try:
            endTime=taskTimesRaw[2][5]
            endTime = datetime.fromisoformat(endTime[:-1])
            duration = endTime - startTime
            print(duration)

            with open('C:/Users/LocalAdmin/Nextcloud/Iceberg_Evaluation/Evaluation/timeDataIR.csv', mode='a', newline='', encoding='utf-8') as time_csv:
                trainee_data_writer = csv.writer(time_csv, delimiter=';')
                trainee_data_writer.writerow([userID, startTime, endTime, duration])

        except IndexError:
            continue





