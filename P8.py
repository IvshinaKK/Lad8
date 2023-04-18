from PIL import Image, ImageDraw
def z1(n):
    foto=Image.open ("Dr.jpg")
    print(foto.size)
    i = foto.crop((500,0,1200,500))
    i.save("i.jpg")
    return ""
def z2(n):
        d = {1: "Dr.jpg", 2: "f.jpg", 3: "m.jpg", 4: "ng.jpg"}
        print("1-День рождения\n"
              "2-23 февраля\n"
              "3-8 марта\n"
              "4-Новый год")
        v=int(input("Для получения открытки введите число-номер праздника :"))
        name = d[v]
        with Image.open(name) as img:
            img.load()
        img.show()
        return ""
def z3(n):
    foto=Image.open("Dr.jpg")
    print(foto.size)
    name=(input("Введите имя"))
    new=ImageDraw.Draw(foto)
    new.text((50,100), name, (0,0,0))
    foto.show()
    foto.save("o.jpg")
    return ""
z1(" ")
z2(" ")
z3(" ")