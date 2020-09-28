import pandas as pd
student_frame = pd.DataFrame({
    "Name" : ["Osias Apedzeagbo", "Steve", "Aron", "Robin", "Bernard"],
    "Age" : [24,20,21,19,22],
    "Sepcialisation" :["IOT", "IOT", "IOT", "IOT", "IOT"]
}
)
#tabel printen
print(student_frame)
# enkel leeftijd printen uit tabel
print (student_frame["Age"])
# enkel naam printen uit tabel
print(student_frame["Name"])
#serie leeftijd halen uit tabel
age_serie = student_frame["Age"]
#print minnimum leeftijd van de tabel
print(age_serie.min())
# beschrijf alles
print(age_serie.describe())