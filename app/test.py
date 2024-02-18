import datetime 

now = datetime.datetime.now() # today's date
date_joined = datetime.date(2019, 2, 7) # a specific date
## Format the date to return only month and year date
print ("Joined " + date_joined.strftime("%B, %Y") )
print(now.strftime("%B, %Y"))
print(now)







