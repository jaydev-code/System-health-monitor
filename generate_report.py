import json

with open("data/metrics.json") as f:
    data = json.load(f)

cpu = data["cpu_usage"]
memory = data["memory_used"]
Windows_drivers_disk_used = data["Windows_drivers_disk_used"]
wsl_disk_used = data["wsl_disk_used"]
timestamp = data["timestamp"]
User = data["User"]

print("-----------------------------------------------------------")
print(f"cpu : {cpu} %")
print(f"Memory used : {memory} %")
print(f"windows driver disk used : {Windows_drivers_disk_used} %")
print(f"wsl disk used : {wsl_disk_used} %")
print(f"timestamp : {timestamp}")
print("-----------------------------------------------------------")

def check_cpu_usage():
    if cpu >= 0 and cpu <= 10 :
        print("Status Label: Excellent ")
        print("Computer Status : Computer almost idle")
        print("Action needed : Everything is fine ")
        print(f"cpu usage : {cpu} %")
        return "#28a745"
    elif cpu > 10 and cpu <= 30 :
        print("Status Label : Good")
        print("Computer Status : Normal light work ")
        print("Action needed : None - healthy")
        print(f"cpu usage : {cpu} %")
        return "#34ce57" 

    elif cpu > 30 and cpu <= 50 :
        print("Status Label : Fair ")
        print("Computer Status : Moderate Activity")
        print("Action needed : Monitor Occasionally")
        print(f"cpu usage : {cpu} %")
        return "#ffc107"

    elif cpu > 50 and cpu <= 70 :
        print("Status label : Busy ")
        print("Computer Status : Heavy processing")
        print("Action needed : Keep eye on it ")
        print(f"cpu usage : {cpu} %")
        return "#fd7e14"

    elif cpu > 70 and cpu <= 85 :
        print("Status label : Warning ")
        print("Computer Status : System struggling ")
        print("Action needed : Investigate soon")
        print(f"cpu usage : {cpu} %")
        return "#ff9800"

    elif cpu > 85 and cpu <= 95 :
        print("Status Label : Critical ")
        print("Computer Status : Performance issue ")
        print("Action Needed : Take action now ")
        print(f"cpu usage : {cpu} %")
        return "#dc3545"

    else :
        print("Status Label : Severe ")
        print("Computer Status : Almost freeze ")
        print("Action Needed : Emergency intervention")
        print(f"cpu usage : {cpu} %")
        return "#721c24"


def check_memory():


    if memory > 0 and memory <= 10:
        print("Status Label : Excellent ")
        print("Computer Status : Very light memory use ")
        print("Action Needed : None ")
        print(f"Memory used : {memory} %")
        return "#28a745"
    
    elif memory > 10 and memory <= 30 :
        print("Status Label : Good ")
        print("Computer status : Normal Operation ")
        print("Action Needed : None ")
        print(f"Memory used : {memory} %")
        return "#34ce57"
    
    elif memory > 30 and memory <= 50 :
        print("Status Label : Fair ")
        print("Computer Status : Moderate memory usage ")
        print("Action Needed : Monitor occasionally ")
        print(f"Memory used : {memory} %")
        return "#ffc107"
    
    elif memory > 50 and memory <= 65:
        print("Status Label : Busy ")
        print("Computer Status : Heavy memory usage ")
        print("Action Needed : Keep an eye on it")
        print(f"Memory Used : {memory} %")
        return "#fd7e14"
    
    elif memory > 65 and memory <= 80:
        print("Status Label : Warning ")
        print("Computer Status : Getting close to limit ")
        print("Action Needed : Investigate soon")
        print(f"Memory Used : {memory} %")
        return "#ff9800"

    elif memory > 80 and memory <= 90 :
        print("Status Label : Critical ")
        print("Computer Status : Memory pressure High ")
        print("Action Needed : Take action now ")
        print(f"Memory Used: {memory} %")
        return "#dc3545"
    
    else :
        print("Status Label : Severe")
        print("Computer Status : Out of memory risk ")
        print("Action Needed : Emergency Intervention ")
        print(f"Memory Used : {memory} %")
        return "#721c24"

def check_windows_disk_space():

    if Windows_drivers_disk_used > 0 and Windows_drivers_disk_used <= 10 :
        print("Status Label : Excellent ")
        print("Computer Status : Almost empty ")
        print("Action Needed : None needed ")
        print(f"Windows Storage used : {Windows_drivers_disk_used} %")
        return "#28a745"

    elif Windows_drivers_disk_used > 10 and Windows_drivers_disk_used <= 20:
        print("Status Label : Excellent ")
        print("Coputer Status : Very Spacious ")
        print("Action Needed : None Needed ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#28a745"
    
    elif Windows_drivers_disk_used > 20 and Windows_drivers_disk_used <= 30 :
        print("Status Label : Excellent ")
        print("Computer Status : Plenty of space ")
        print("Action Needed : None Needed ")
        print(f"Windows Storage used : {Windows_drivers_disk_used} %")
        return "#28a745"

    elif Windows_drivers_disk_used > 30 and Windows_drivers_disk_used <= 40:
        print("Status Label : Good ")
        print("Computer Status : Healthy amount free ")
        print("Action Needed : None Needed ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#34ce57"

    elif Windows_drivers_disk_used > 40 and Windows_drivers_disk_used <= 50 :
        print("Status Label : Good ")
        print("Computer Status : Good ")
        print("Action Needed : None needed ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#34ce57"

    elif Windows_drivers_disk_used > 50 and Windows_drivers_disk_used <= 60:
        print("Status Label : Fair ")
        print("Computer Status : halfway there to full ")
        print("Action Needed : Keep an eye on it ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#ffc107"

    elif Windows_drivers_disk_used > 60 and Windows_drivers_disk_used <= 70:
        print("Status Label : Getting Full ")
        print("Computer Status : Space decreasing ")
        print("Action Needed : Plan ahead ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#fd7e14"


    elif Windows_drivers_disk_used > 70 and Windows_drivers_disk_used <= 75:
        print("Status Label : warning ")
        print("Computer Status : Getting low ")
        print("Action Needed : Consider cleanup")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#ff9800"

    elif Windows_drivers_disk_used > 75 and Windows_drivers_disk_used <= 80:
        print("Status Label : Warning ")
        print("Computer Status : Low space warning ")
        print("Action Needed : Start cleaning up ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#ff9800"

    elif Windows_drivers_disk_used > 80 and Windows_drivers_disk_used <= 85:
        print("Status Label : Critical ")
        print("Computer Status : Very low space  ")
        print("Action Needed : Immediate cleanup ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#dc3545"

    elif Windows_drivers_disk_used > 85 and Windows_drivers_disk_used <= 90:
        print("Status Label : Critical ")
        print("Computer Status : Dangerously low ")
        print("Action Needed : Urgent action needed ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#dc3545"
    
    elif Windows_drivers_disk_used > 90 and Windows_drivers_disk_used <= 95:
        print("Status Label : Severe ")
        print("Computer Status : Almost Full")
        print("Action Needed : System at risk  ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#721c24"
    
    else:
        print("Status Label : Full ")
        print("Computer Status : Completely full ")
        print("Action Needed : System may crash ")
        print(f"Windows storage used : {Windows_drivers_disk_used} %")
        return "#000000"
        

def check_wsl_disk_used():

    if wsl_disk_used > 0 and wsl_disk_used <= 20 :
        print("Status Label : Excellent ")
        print("Computer Status : Very Spacious ")
        print("Action needed : none needed ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#28a745"
    
    elif wsl_disk_used > 20 and wsl_disk_used <= 40 :
        print("Status Label : Good ")
        print("Computer Status : Plenty of space ")
        print("Action needed : none needed ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#34ce57"

    elif wsl_disk_used > 40 and wsl_disk_used <= 50 :
        print("Status Label : Fair ")
        print("Computer Status : Moderate usage")
        print("Action needed : Monitor occasionally ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#ffc107"

    elif wsl_disk_used > 50 and wsl_disk_used <= 60 :
        print("Status Label : getting full ")
        print("Computer Status : Halfway there")
        print("Action needed : keep an eye on it ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#fd7e14"

    elif wsl_disk_used > 60 and wsl_disk_used <= 70 :
        print("Status Label : Warning ")
        print("Computer Status : Getting low ")
        print("Action needed : Plan cleanup ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#ff9800"

    elif wsl_disk_used > 70 and wsl_disk_used <= 80 :
        print("Status Label : Critical ")
        print("Computer Status : Very low space ")
        print("Action needed : Free up space soon ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#dc3545"

    elif wsl_disk_used > 80 and wsl_disk_used <= 90 :
        print("Status Label : Severe ")
        print("Computer Status : Almost full")
        print("Action needed : Emergency cleanup ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#721c24"
    
    else :
        print("Status Label : Critical  ")
        print("Computer Status : Out of space risk ")
        print("Action needed : Immediate action ")
        print(f"Wsl disk Used {wsl_disk_used} %")
        return "#000000"

    
    

           


print("--------------------------------------------")
cpu_color = check_cpu_usage()
print("--------------------------------------------")
memory_color = check_memory()
print("--------------------------------------------")
windows_color = check_windows_disk_space()
print("--------------------------------------------")
wsl_color = check_wsl_disk_used()
print("--------------------------------------------")





html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>
            System Health Monitor System
        </title>
        <style>
            body{{
                background-color: #72d06a;
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
            .metrics{{
                background-color: #41a230;
                padding: 20px;
                border-radius: 10px;
                max-width: 600px;
                margin: 0 auto;
            }}
            .cpu{{
                background-color: {cpu_color};
                color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }}
            .memory{{
                background-color: {memory_color};
                color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }}
            .windows{{
                background-color: {windows_color};
                color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }}
            .wsl{{
                background-color: {wsl_color};
                color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }}
            .timestamp{{
                background-color: #6c757d;
                color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                text-align: center;
                font-size: 0.9em;
            }}
            h1{{
                color: white;
                text-align: center;
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="metrics">
            <h1>Hello {User}</h1>
            <div class="cpu">CPU Usage : {cpu} %</div>
            <div class="memory">Memory Usage : {memory} %</div>
            <div class="windows">Windows drivers disk used : {Windows_drivers_disk_used} %</div>
            <div class="wsl">WSL drivers disk used : {wsl_disk_used} %</div>
            <div class="timestamp">Time/date : {timestamp}</div>
        </div>
    </body>
</html>
"""

with open("reports_system_health_monitor.html","w") as file :
    file.write(html)