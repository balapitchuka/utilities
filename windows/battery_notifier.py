import psutil
from win10toast import ToastNotifier
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)
if plugged==False:
    plugged="Not Plugged In"
else:
    plugged="Plugged In"
toaster = ToastNotifier()
if percent <25:
    toaster.show_toast("Reminder2!! plug in charger  now  fast!!!")
    exit(0)
elif percent < 30:
	toaster.show_toast("Reminder1!! plug in charger  now  fast!!!")
	exit(0)

  

    
    
