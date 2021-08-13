import weather_forecast as wf
p = input("ENTER PLACE:")
r = input("ENTER DATE(YYYY - MM - DD):")
l = input("ENTER TIME:")
print(p)
wf.forecast(place=p, time=l, date=r, forecast="daily")





