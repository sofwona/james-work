from datetime import datetime

q= datetime.now()
print("Today is: {}/{}/{}".format(q.strftime("%d"),q.strftime("%m"),q.strftime("%y")))