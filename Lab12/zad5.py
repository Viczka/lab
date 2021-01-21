import math
m = float(input("podaj masę w kg:"))
wzr = float(input("podaj wzrost w m:"))
def masa (m,wzr):
 bmi = float(m) / pow(float(wzr),2)
 if bmi < 18.5:
  return "Masz niedowagę, leć po kebsa"
 if 18.5 < bmi < 24.99:
  return "Jest git"
 if bmi > 24.99:
  return "Masz nadwagę!!!"
print(masa(m,wzr))





