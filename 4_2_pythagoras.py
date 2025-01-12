import math

kateter1 = int(input("hur lång är kateter1?"))
kateter2 = int(input("hur lång är kateter2?"))
hypotenusa = math.sqrt(kateter1 * kateter1 + kateter2 * kateter2)
print("Triangelns hypotenusa blir: " + str(hypotenusa))