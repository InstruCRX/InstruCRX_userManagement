## InstruCRX_userManagement

This repository belings to InstruCRX, a cyber range exercise (CRX) to introduce cybersecurity novices to incident response. This web application is the central platform over which users register for the CRX and are assigned a distinct CRX environment and submit their team solutions over the flag submission dashboard.

(1) trainee registration and 


 <p align="center">
  <img src="https://github.com/InstruCRX/InstruCRX_userManagement/assets/56884203/4ebbef05-1827-4616-8a78-fecdf1ba3767" width="500" />
</p>




(2) the platform for collaborative flag submission.

 <p align="center">
  <img src="https://github.com/InstruCRX/InstruCRX_backend/assets/56884203/3fa1176f-2d14-4083-8236-8eb750fc00fa" width="500" />
</p>

To deploy the repository, please follow these steps:

1. Create a Service Account on Firebase. This can be done on the Firebase Dashboard via Settings -> Service Account -> "Generate Private Key" as described [here]( https://firebase.google.com/docs/admin/setup#python)

2. Replace the file [serviceAccount.json](https://github.com/InstruCRX/InstruCRX_frontend/blob/main/userDataScripts/serviceAccount.json) with your created key (also naming it serviceAccount.json). You will need two create two Firestore databases, one which holds all available VMS (e.g. InstruVMs) and one in which the actual user data (of the registered trainees) is stored (e.g. instruCRXTraineeData), for this reason, add the following lines to firebase.js (**both in [InstruCRX_userManagement](https://github.com/InstruCRX/InstruCRX_userManagement) AND [InstruCRX_frontend](https://github.com/InstruCRX/InstruCRX_frontend)**)

```bash
const VM_db = db.collection('InstruVMs')
const userDashboard = db.collection('instruCRXTraineeData')
 ``` 

3. Create a list of available VMs, each assigned a random group pseuodnym and the round of training (to only display those groups on the leaderboard that are playing in one round at the same time). This list is saved in [VMs.csv](https://github.com/Instru_CRX/InstruCRX_userManagement/blob/main/userDataScripts/VMs.csv)

|     IP        |  Pseudonym |    Round   |
|----------------------|------|--------|
|     148.199.125.83        |  DataDevils |    1   |
|     148.199.125.10        |   HackerGang  |    1   |
|     148.199.125.23       | DefenseGroup |    1   |


4. Run import script:
```bash
cd https://github.com/Instru_CRX/InstruCRX_userManagement/blob/main/userDataScripts/importFromCsv.py && \
python3 importFromCsv.py
 ```
 
5. Deploy User Data Management:
```bash
cd InstruCRX_userManagement && \
npm install
npm run serve
 ```
 
The IP the user data management is deployed on serves as a central entry point to the cyber range, possible link it a DNS name, e.g. cyberrange.yourorganization.org
The trainees are randomly assigned to a group with a group ID (we gave them a note with their group ID). When the trainees register their groupID they are automatically assigned a free CRX VM. 


6. To export user data (points, level, times) after the training, run:
 
 ```bash
cd InstruCRX_userManagement/userDataScripts && \
python3 exportToCsv.py
 ```




