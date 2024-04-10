# Life building codes
# Built by Aarooshcoding33
# Helpers: Snakyguy, The IRL guy, GamingLegend
# Idea By: GamingLegend

# Imports
import time

# Definations
def data_received():
    Package_number = 29387462389482937467819492138472365235456352679371663616490817490490294283982357263481048524679209428375623542781041024
    Package_receiver = 'Build.py'
    Data = 'Build.py'

currenttime = "8:24"

print("Collecting data from Build.py, please wait...")
Data_collector = data_received()
time.sleep(8)
print("Success!")
print("Life Pre-Alpha")
time.sleep(2)
print("One line mode: ON (Auto)")
time.sleep(4)
print("start:")
while True:
    Input_code = str(input("Life > "))
    if Input_code == "talk" or Input_code == "me.talk":
        talk_string = str(input("String > "))
        print("You:",talk_string)
    elif Input_code == "mom.talk":
        talk_string_mom = str(input("String > "))
        print("Mom:",talk_string_mom)
    elif Input_code == "dad.talk":
        talk_string_dad = str(input("String > "))
        print("Dad:",talk_string_dad)
    elif Input_code == "exit":
        print(":end")
        break
    elif Input_code == "showcurrent.lifetime":
        print(currenttime)
    elif Input_code == "sleep" or Input_code == "me.sleep":
        print("You are now sleeping.")
    elif Input_code == "mom.sleep":
        print("Mom: *Sleeping*")
    elif Input_code == "dad.sleep":
        print("Dad: *Sleeping*")
    elif Input_code == "yawn" or Input_code == "me.yawn":
        yawntime = str(input("Duration (Also enter s (seconds), m (minutes), hr (hours)) > "))
        duration = yawntime
        print("You yawned for " + duration)
    elif Input_code == "mom.yawn":
        yawntime2 = str(input("Duration (Also enter s (seconds), m (minutes), hr (hours)) > "))
        duration2 = yawntime2
        print("Mom: *Yawns for " + duration2 + "*")
    elif Input_code == "dad.yawn":
        yawntime3 = str(input("Duration (Also enter s (seconds), m (minutes), hr (hours)) > "))
        duration3 = yawntime3
        print("Dad: *Yawns for " + duration3 + "*")
    elif Input_code == "life.fade":
        print("Faded")
    elif Input_code == "getup":
        print("You got up.")
    elif Input_code == "mom.getup":
        print("Mom got up.")
    elif Input_code == "dad.getup":
        print("Dad got up.")
    else:
        print("The syntax you have entered is either invalid syntax or syntax not available in one line code.")
        continue