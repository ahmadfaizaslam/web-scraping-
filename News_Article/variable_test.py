from datetime import datetime

some_date = "August 2, 2021 @ 7:35pm"
some_date = some_date.split("@")[0].rstrip()

ayam = datetime.strptime(some_date, "%B %d, %Y").strftime("%Y-%m-%d")


daging = (str(datetime.today())).split(" ", 1)

print(daging[0])
print(ayam)
