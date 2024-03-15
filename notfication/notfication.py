from plyer import notification
from datetime import datetime

time=datetime.now()

iftar_hour=19-time.hour
iftar_min=15-time.minute

if iftar_hour < 0:
    iftar_hour += 24
if iftar_min < 0:
    iftar_min += 60

iftar_time = "{:02d}:{:02d}".format(iftar_hour, iftar_min)

if time.hour == 19 and time.minute == 15:
    notification.notify(title="İFTAR VAKTİ", message="İSTANBUL İÇİN İFTAR VAKTİ")
else:
    notification.notify(title="İFTAR VAKTİ", message="İFTARA DAHA {} SAAT VAR".format(iftar_time))




