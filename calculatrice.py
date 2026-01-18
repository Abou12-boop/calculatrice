


veri_fier=input("veut tu calcule (oui-non):")
while veri_fier=="oui":

    v1 = int(input("entre un nombre:"))
    symbole=input("entre un symbole de calcule(+,-,%,*):")
    v2 = int(input("entre un nombre:"))
    opera = ""

    if symbole=="+":
        opera=v1+v2
        print(opera)

    elif symbole=="-":
        opera=v1-v2
        print(opera)

    elif symbole=="%":
        opera=v1%v2
        print(opera)
        if v2==0:
            print("division par 0 est non valide")

    elif symbole=="*":
        opera=v1*v2
        print(opera)

    veri_fier = input("veut tu calcule (oui-non):")
print("Merci d'avoir utilisé la calculatrice !")

















