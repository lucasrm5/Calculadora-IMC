altura = float(input("Qual a sua altura em cm: "))
peso = float(input("Qual o seu peso em kg: "))

IMC = peso / (altura/100)**2


if IMC < 18.5:
    print(f"Seu IMC é de {IMC}, e é classificado como Magreza")

elif IMC >= 18.5 and IMC < 24.9:
    print(f"Seu IMC é de {IMC}, e é classificado como Normal")

elif IMC>= 25 and IMC < 29.9:
    print(f"Seu IMC é de {IMC}, e é classificado como Sobrepeso")

elif IMC >= 30 and IMC < 39.9:
    print(f"Seu IMC é de {IMC}, e é classificado como Obesidade")

else:
    print(f"Seu IMC é de {IMC}, e é classificado como Obesidade grave")



# MENOR QUE 18,5	MAGREZA	0
# ENTRE 18,5 E 24,9	NORMAL	0
# ENTRE 25,0 E 29,9	SOBREPESO	I
# ENTRE 30,0 E 39,9	OBESIDADE	II
# MAIOR QUE 40,0	OBESIDADE GRAVE	III