import csv 

from cs50 import SQL

open("moga.db","w").close()

db = SQL("sqlite:///moga.db")

db.execute("CREATE TABLE doctor(doctor_id INTEGER, doctor_names TEXT, doctor_age INTEGER, doctor_gender TEXT, PRIMARY KEY(doctor_id));")
db.execute("CREATE TABLE patient(patient_id INTEGER, names TEXT, occupation TEXT,age INTEGER, gender TEXT, disease TEXT, address_location TEXT, PRIMARY KEY (patient_id));")
db.execute("CREATE TABLE treatment(patient_id INTEGER, pharmacy_id INTEGER, doctor_id INTEGER, admission_discharge_id INTEGER, FOREIGN KEY(patient_id) REFERENCES patient(patient_id),FOREIGN KEY(doctor_id) REFERENCES doctor(doctor_id), FOREIGN KEY(admission_discharge_id) REFERENCES admission_discharge(id), FOREIGN KEY(pharmacy_id) REFERENCES pharmacy(pharmacy_id));")
db.execute("CREATE TABLE admission_discharge(id INTEGER,  ward_no INTEGER,  date_of_admission TEXT, date_of_discharge TEXT,bill INTEGER, amount_paid INTEGER, balance INTEGER, PRIMARY KEY(id));")
db.execute("CREATE TABLE pharmacy(pharmacy_id INTEGER, medicine_name TEXT,price INTEGER, PRIMARY KEY(pharmacy_id));")

with open("project data.csv","r") as file:

    reader = csv.DictReader(file)
    
    for row in reader:
        doctor_names = row["names"]
        doctor_age= row["age"]
        doctor_gender= row["gender"]
        doctor_id = db.execute("INSERT INTO doctor(doctor_names,doctor_age,doctor_gender) VALUES(?,?,?)",doctor_names,doctor_age,doctor_gender)

        names = row["names"]
        occupation = row["occupation"]
        age = row["age"]
        gender =row["gender"]
        disease =row["disease"]
        address_location = row["address_location"]
        patient_id = db.execute("INSERT INTO patient(names,occupation,age,gender,disease,address_location) VALUES(?,?,?,?,?,?)",names,occupation,age,gender,disease,address_location)

        ward_no = row["ward_no"]
        date_of_admission= row["date_of_admission"]
        date_of_discharge=row["date_of_discharge"]
        bill=row["bill"]
        amount_paid=row["amount_paid"]
        balance= row["balance"]
        admission_discharge_id = db.execute("INSERT INTO admission_discharge(ward_no,date_of_admission,date_of_discharge,bill,amount_paid,balance) VALUES (?,?,?,?,?,?)",ward_no,date_of_admission,date_of_discharge,bill,amount_paid,balance)

        medicine_name=row["medicine_name"]
        price=row["price"]
        pharmacy_id = db.execute("INSERT INTO pharmacy(medicine_name,price) VALUES (?,?)",medicine_name,price)
        

        db.execute('INSERT INTO treatment(patient_id,pharmacy_id,doctor_id,admission_discharge_id) VALUES((SELECT patient_id FROM patient WHERE patient_id=?),(SELECT pharmacy_id FROM pharmacy WHERE pharmacy_id=?),(SELECT doctor_id FROM doctor WHERE doctor_id=?),(SELECT id FROM admission_discharge WHERE id=?))',patient_id,pharmacy_id,doctor_id,admission_discharge_id)
