# Creado por: Geovas or MartL7
# Create by: MartL7 or Geovas

import os, webbrowser

def CentrarBanner(texto, ancho):
    return texto.center(ancho)

Banner = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

texto = "--------Bienvenido a mi Script MartL7----------"

ancho = 80

BannerCentrado = CentrarBanner(Banner, ancho)
TextoCentrado = CentrarBanner(texto, ancho)

print(BannerCentrado)
print(TextoCentrado)


print("\033[94m"+ "[1]" + "\033[0m" + "Edad")
print("\033[94m"+ "[2]" + "\033[0m" + "Nombre")
print("\033[94m"+ "[3]" + "\033[0m" + "Mejor Amig@")
print("\033[94m"+ "[4]" + "\033[0m" + "Cuantas Novias?")
print("\033[94m"+ "[5]" + "\033[0m" + "Mainer Lenguajes")
print("\033[94m"+ "[6]" + "\033[0m" + "Contacto")
print("\033[94m"+ "[7]" + "\033[0m" + "Grupo de WhatsApp")
print("\033[94m"+ "[8]" + "\033[0m" + "Correo Electronico")
print("\033[94m"+ "[9]" + "\033[0m" + "Actualizar Termux")
print("\033[94m"+ "[10]" + "\033[0m" + "Creditos/Credits")

Reinicio = True
while Reinicio:
    nivel = int(input("¿Que opcion eliges? => "))
    if nivel == 1:
        print("\033[92m" + "17" + "\033[0m")
    elif nivel == 2:
        print("\033[92m" + "Geovas Or MartL7" + "\033[0m")
    elif nivel == 3:
        print("\033[92m" + "Alguna vez lo fue 'J' y ahora lo es 'M'" + "\033[0m")
    elif nivel == 4:
        print("\033[92m" + "4 ya no andes de chismos@" + "\033[0m")
    elif nivel == 5:
        print("\033[92m" + "Python" + "\033[0m")
        print("\033[92m" + "JavaScript" + "\033[0m")
        print("\033[92m" + "PHP" + "\033[0m")
        print("\033[92m" + "C#" + "\033[0m")
        print("\033[92m" + "HTML" + "\033[0m")
        print("\033[92m" + "Java" + "\033[0m")
    elif nivel == 6:
        print("\033[94m" + "https://wa.me/527761029302?text=Hola%20Rey" + "\033[0m")
    elif nivel == 7:
        print("\033[92m" + "Actualmente no hay, pronto habra mas novedades" + "\033[0m")
    elif nivel == 8:
        print("\033[94m" + "MartL7contact@gmail.com" + "\033[0m")
    elif nivel == 9:
        print("\033[93m" + "ACTUALIZANDO TERMUX" + "\033[0m")
        os.system("pkg update && pkg upgrade -y")
    elif nivel == 10:
        print("\033[93m" + "Create by: Geovas or MartL7. 🥰" + "\033[0m")