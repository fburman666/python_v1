pris = 2000
rea_procent = input ("hur många procents rea är det?")
slut_pris = pris - pris * int(rea_procent) / 100
print("Slutpris blir: " + str(slut_pris))