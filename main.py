import random
variable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
variable2 = int(input("elige la longitud de la contraseña: "))
variable3 = ""
for i in range(variable2):
    character = random.choice(variable)
    variable3 += character
print("esta es tu contraseña: ", variable3)
