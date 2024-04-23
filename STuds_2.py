# using previous module to import the details of those students and print in new python file
# only happens on local folders
from Studs_array import S
import pyttsx3
engine = pyttsx3.init()
# code is simple "from 'file_name' import 'which/what u want to import'...."
for i in S:
        print(i['Student'])
        print(i['Age'], end="\n")
        print(i['Dept'], end="\n")
        print(i['Fav'], end="\n")
        print("\t")
# end of programme

engine.runAndWait()