import requests


def calc(code, price):
    print(">>>>>>>>>>>>", price, code)
    response = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/').json()
    for i in response:
        if i['Ccy'] == code:
            print(i["Rate"])
            result = price * float(i["Rate"])
            print("keldi")
            break
    print("<<<<<<<<<<", result)
    return result


def calc_all(price):
    narx = 0
    for i in price.items():
        narx += i[1]
    return narx


def create_pub(log, price, type=None):
    s = ""

    for i, j in log.items():
        if i == "state":
            continue
        elif i == "price":
            continue
        else:
            s += f"{i} ....... {j}\n"
    if not s:
        return False

    if type:
        s = s + f"\nUmumiy narx: {price} So'm bo'ldi"
    else:
        s = s + f"\nUmumiy narx: {price}$ bo'ldi"

    s = s + "\n\n<a href='https://t.me/altechuzz'>TELEGRAM</a> | <a href='https://vm.tiktok.com/ZSJw3A8ht/'>TIK TOK</a> | <a href='https://www.instagram.com/altech.uz/'>INSTAGRAM</a> | <a href='https://www.facebook.com/profile.php?id=100074295934415'>FACEBOOK</a> | <a href='https://www.youtube.com/channel/UCYWWBWGG-pjtJI4MbEyxTLA'>YOUTUBE</a> "
    return s
