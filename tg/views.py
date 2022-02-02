from . import create_pub, calc, calc_all
from .services import *
from telegram import ReplyKeyboardMarkup, KeyboardButton


def btns(type=None, main=True):
    if type == "price":
        btn = [
            [KeyboardButton("UZS da ko'rsatish")],
            [KeyboardButton("Yana Texnika qo'shish")],
            [KeyboardButton("🏠 Bosh menyu")]
        ]
    elif type == "cam":
        btn = [
            [KeyboardButton("NVR || DVR || XVR"), KeyboardButton("IP || HD CAMERA")],
            [KeyboardButton("💽 HARD DISC"), KeyboardButton("🔌 Block Pitaniya Cam")],
            [KeyboardButton("🔌Штекер(Vilka) BNC"), KeyboardButton("📻 Radio Kabel")],
            [KeyboardButton("🔌Штекер Xvostik"), KeyboardButton("🎛Connector RJ45")],
            [KeyboardButton("KKB || UTB || CABEL"), KeyboardButton("📡Setavoy Commutator")],
            [KeyboardButton("HDMI Cabel"), KeyboardButton("🎥 Video Balun")],
            [KeyboardButton("🏠 Bosh menyu")]
        ]
        if main:
            del btn[-1]
            btn.append([KeyboardButton("Foyda")]),
            btn.append([KeyboardButton("Other")]),
            btn.append([KeyboardButton("💰Natijani chiqarish")])
            btn.append([KeyboardButton("🏠 Bosh menyu")])

    elif type == "next":
        btn = [
            [KeyboardButton("⬅️Back")],
            [KeyboardButton("🏠 Bosh menyu")],
        ]
    elif type == "head":
        btn = [
            [KeyboardButton("USD da ko'rsatish")],
            [KeyboardButton("Yana Texnika qo'shish")],
            [KeyboardButton("🏠 Bosh menyu")]
        ]
    elif type == "ctg":
        btn = [
            [KeyboardButton("📦 Korpus(Keys)"), KeyboardButton("🔌 Block Pitaniya")],
            [KeyboardButton("🎛 Materinka"), KeyboardButton("🖥 Protsessor(CPU)")],
            [KeyboardButton("🧯 CPU Cooler"), KeyboardButton("💾 RAM")],
            [KeyboardButton("📼 DVD-RW SATA"), KeyboardButton("📼 Video Karta(GPU)")],
            [KeyboardButton("💽 HDD"), KeyboardButton("💾 SSD yoki M2")],
            [KeyboardButton("🏠 Bosh menyu")]
        ]
        if main:
            btn.append([KeyboardButton("Foyda")]),
            btn.append([KeyboardButton("Other")]),
            btn.append([KeyboardButton("💰Natijani chiqarish")])



    else:
        btn = [
            [KeyboardButton("📺 PC"), KeyboardButton('📸 Camera')]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    log = get_log(user.id)
    tg_user = get_user(user.id)
    if not log:
        log = create_log(user.id)

    if not tg_user:
        tg_user = create_user(user.id)
    change_menu(user.id, 0)
    state = log.get('state', 0)

    update.message.reply_text("Assalomu Alaykum Altech.uz Do'koni botiga xush kelibsiz 👨🏻‍💻", reply_markup=btns())


def received_message(update, context):
    msg = update.message.text
    user = update.message.from_user

    if msg == '📺 PC':
        change_menu(user.id, 1)
        clear_log(user.id)

    if msg == '📸 Camera':
        change_menu(user.id, 2)
        clear_log(user.id)

    log = get_log(user.id)
    state = log.get('state', 0)
    tg_user = get_user(user.id)

    menu = tg_user.get('menu_log', 0)
    if msg == "🏠 Bosh menyu":
        clear_log(user.id)
        update.message.reply_text("Bosh menu 👨🏻‍💻\nQuyidagi menyulardan birini tanlang👇",
                                  reply_markup=btns())

    elif msg == "📦 Korpus(Keys)":
        log['state'] = 2
        update.message.reply_text("📦 Korpus(Keys) turini kiriting", reply_markup=btns("next"))

    elif msg == "🔌 Block Pitaniya":
        log['state'] = 4
        update.message.reply_text("🔌 Block Pitaniya turini kiriting", reply_markup=btns("next"))

    elif msg == "🎛 Materinka":
        log['state'] = 6
        update.message.reply_text("🎛 Materinka turini kiriting", reply_markup=btns("next"))

    elif msg == "🖥 Protsessor(CPU)":
        log['state'] = 8
        update.message.reply_text("🖥 Protsessor(CPU) turini kiriting", reply_markup=btns("next"))

    elif msg == "🧯 CPU Cooler":
        log['state'] = 10
        update.message.reply_text("🧯 CPU Cooler turini kiriting", reply_markup=btns("next"))

    elif msg == "💾 RAM":
        log['state'] = 12
        update.message.reply_text("💾 RAM turini kiriting", reply_markup=btns("next"))

    elif msg == "📼 Video Karta(GPU)":
        log['state'] = 14
        update.message.reply_text("📼 Video Karta(GPU) turini kiriting", reply_markup=btns("next"))

    elif msg == "💾 SSD yoki M2":
        log['state'] = 20
        update.message.reply_text("💾 SSD yoki M2ni  kiriting", reply_markup=btns("next"))

    elif msg == "💽 HDD":
        log['state'] = 18
        update.message.reply_text("💽 HDDni  kiriting", reply_markup=btns("next"))

    elif msg == "📼 DVD-RW SATA":
        log['state'] = 16
        update.message.reply_text("📼 DVD-RW SATAni  kiriting", reply_markup=btns("next"))

    elif msg == "NVR || DVR || XVR":
        log['state'] = 2
        update.message.reply_text("NVR || DVR || XVR ni  kiriting", reply_markup=btns("next"))

    elif msg == "IP || HD CAMERA":
        log['state'] = 4
        update.message.reply_text("IP || HD CAMERA ni  kiriting", reply_markup=btns("next"))

    elif msg == "💽 HARD DISC":
        log['state'] = 6
        update.message.reply_text("💽 HARD DISCni  kiriting", reply_markup=btns("next"))
    elif msg == "🔌 Block Pitaniya Cam":
        log['state'] = 8
        update.message.reply_text("🔌 Camerani Block Pitaniyasini  kiriting", reply_markup=btns("next"))

    elif msg == "🔌Штекер(Vilka) BNC":
        log['state'] = 10
        update.message.reply_text("🔌Штекер(Vilka) BNC ni  kiriting", reply_markup=btns("next"))

    elif msg == "📻 Radio Kabel":
        log['state'] = 12
        update.message.reply_text("📻 Radio Kabel turini  kiriting", reply_markup=btns("next"))

    elif msg == "🔌Штекер Xvostik":
        log['state'] = 14
        update.message.reply_text("🔌Штекер Xvostik turini  kiriting", reply_markup=btns("next"))

    elif msg == "🎛Connector RJ45":
        log['state'] = 16
        update.message.reply_text("🎛Connector RJ45ni  kiriting", reply_markup=btns("next"))

    elif msg == "KKB || UTB || CABEL":
        log['state'] = 18
        update.message.reply_text("KKB || UTB || CABEL birini  kiriting", reply_markup=btns("next"))

    elif msg == "📡Setavoy Commutator":
        log['state'] = 20
        update.message.reply_text("📡Setavoy Commutatorni  kiriting", reply_markup=btns("next"))

    elif msg == "HDMI Cabel":
        log['state'] = 22
        update.message.reply_text("HDMI Cabelni  kiriting", reply_markup=btns("next"))

    elif msg == "🎥 Video Balun":
        log['state'] = 24
        update.message.reply_text("🎥 Video Balunni  kiriting", reply_markup=btns("next"))

    elif msg == "Other":
        if menu == 1:
            log['state'] = 22
            update.message.reply_text(
                "⌨️Qolgan narsalarni kirting\n⚠️Qolgan narsalarni qo'shganingizdan keyin avtomatik tarzda oxirgi natija chiqariladi",
                reply_markup=btns("next"))
        else:
            log['state'] = 26
            update.message.reply_text(
                "⌨️Qolgan narsalarni kirting\n⚠️Qolgan narsalarni qo'shganingizdan keyin avtomatik tarzda oxirgi natija chiqariladi",
                reply_markup=btns("next"))


    elif msg == "💰Natijani chiqarish":
        if menu == 1:
            log['state'] = 24
            pub = create_pub(log, calc_all(log['price']))
            if pub:
                update.message.reply_html(pub, reply_markup=btns('price'))
            else:
                update.message.reply_text("Hech qanaqa ma'lumot topilmadi🤷‍️",
                                          reply_markup=ReplyKeyboardMarkup([[KeyboardButton("🏠 Bosh menyu")]],
                                                                           resize_keyboard=True), )

        else:
            log['state'] = 30
            pub = create_pub(log, calc_all(log['price']))
            if pub:
                update.message.reply_html(pub, reply_markup=btns('price'))
            else:
                update.message.reply_text("Hech qanaqa ma'lumot topilmadi🤷‍️",
                                          reply_markup=ReplyKeyboardMarkup([[KeyboardButton("🏠 Bosh menyu")]],
                                                                           resize_keyboard=True), )

    elif msg == "Foyda":
        log['state'] = 50
        update.message.reply_html("O'zizga qoluvchi foydani kiriting", reply_markup=btns('next'))


    elif msg == "USD da ko'rsatish":
        price = log.get("price", {})
        print("price>>>>", price)
        price = calc_all(price)
        print(">>>", price)
        update.message.reply_html(create_pub(log, price), reply_markup=btns('price'))

    elif msg == "Yana Texnika qo'shish":
        if menu == 1:
            update.message.reply_text("Yana Yangi ma'lumot qo'shish uchun Kategoriyani tanlang👨🏻‍💻"
                                      , reply_markup=btns('ctg'))
        else:
            update.message.reply_text("Yana Yangi ma'lumot qo'shish uchun Kategoriyani tanlang👨🏻‍💻"
                                      , reply_markup=btns('cam'))
    elif menu == 1:
        price = log.get("price", {})
        if state == 2:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 3
                log['📦 Korpus(Keys)'] = msg
                update.message.reply_text("💵Korpus(Keys) Narxini kiriting👇")

        elif state == 3:
            if msg == "⬅️Back":
                log['state'] = 2
                del log['📦 Korpus(Keys)']
                update.message.reply_text("📦 Korpus(Keys) turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_k'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 4:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 5
                log['🔌 Block Pitaniya'] = msg
                update.message.reply_text("💵Block Pitaniya Narxini kiriting")

        elif state == 5:
            if msg == "⬅️Back":
                log['state'] = 4
                del log['🔌 Block Pitaniya']
                update.message.reply_text("🔌 Block Pitaniya turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_b'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")
        elif state == 6:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 7
                log['🎛 Materinka'] = msg
                update.message.reply_text("💵Materinka Narxini kiriting")

        elif state == 7:
            if msg == "⬅️Back":
                log['state'] = 6
                del log['🎛 Materinka']
                update.message.reply_text("🎛 Materinka turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_m'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 8:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 9
                log['🖥 Protsessor(CPU)'] = msg
                update.message.reply_text("💵 Protsessor(CPU) Narxini kiriting")

        elif state == 9:
            if msg == "⬅️Back":
                log['state'] = 8
                del log['🖥 Protsessor(CPU)']
                update.message.reply_text("🖥 Protsessor(CPU) turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_cpu'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 10:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 11
                log['🧯 CPU Cooler'] = msg
                update.message.reply_text("💵 CPU Cooler Narxini kiriting")

        elif state == 11:
            if msg == "⬅️Back":
                log['state'] = 10
                del log['🧯 CPU Cooler']
                update.message.reply_text("🧯 CPU Cooler turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    log['state'] = 0
                    price['price_cool'] = int(msg)
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 12:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 13
                log['💾 RAM'] = msg
                update.message.reply_text("💵 RAM Narxini kiriting")

        elif state == 13:
            if msg == "⬅️Back":
                log['state'] = 12
                del log['💾 RAM']
                update.message.reply_text("💾 RAM turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_ram'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 14:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 15
                log['📼 Video Karta(GPU)'] = msg
                update.message.reply_text("💵 Video Karta(GPU) Narxini kiriting")

        elif state == 15:
            if msg == "⬅️Back":
                log['state'] = 14
                del log['📼 Video Karta(GPU)']
                update.message.reply_text("📼 Video Karta(GPU) turini kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_gpu'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")
        elif state == 16:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 17
                log['📼 DVD-RW SATA'] = msg
                update.message.reply_text("💵 DVD-RW SATA Narxini kiriting")

        elif state == 17:
            if msg == "⬅️Back":
                log['state'] = 16
                del log['📼 DVD-RW SATA']
                update.message.reply_text("📼 DVD-RW SATAni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_sata'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 18:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 19
                log['💽 HDD'] = msg
                update.message.reply_text("💵 HDD Narxini kiriting")

        elif state == 19:
            if msg == "⬅️Back":
                log['state'] = 18
                del log['💽 HDD']
                update.message.reply_text("💽 HDDni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_hdd'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 20:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 21
                log['💾 SSD yoki M2'] = msg
                update.message.reply_text("💵 SSD yoki M2 Narxini kiriting")

        elif state == 21:
            if msg == "⬅️Back":
                log['state'] = 20
                del log['💾 SSD yoki M2']
                update.message.reply_text("💾 SSD yoki M2ni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_ssd'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")
        elif state == 50:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                try:
                    price['price_foyda'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Foyda Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('ctg'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 22:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('ctg'))
            else:
                log['state'] = 23
                log['Other'] = msg
                update.message.reply_text("💵 Qolgan narsalarni Umumiy Narxini kiriting")

        elif state == 23:
            if msg == "⬅️Back":
                log['state'] = 22
                del log['Other']
                update.message.reply_text(
                    "⌨️Qolgan narsalarni kirting\n⚠️Qolgan narsalarni qo'shganingizdan keyin avtomatik tarzda oxirgi natija chiqariladi",
                    reply_markup=btns("next"))
            else:
                try:
                    price['price_other'] = int(msg)
                    log['state'] = 24
                    update.message.reply_html(create_pub(log, calc_all(log['price'])), reply_markup=btns('price'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 24:
            if msg == "UZS da ko'rsatish":
                _price = calc("USD", calc_all(price))
                update.message.reply_html(create_pub(log, _price, True), reply_markup=btns('head'))
                clear_log(user.id)
            else:
                update.message.reply_html(create_pub(log, calc_all(log['price'])), reply_markup=btns('head'))
        else:
            update.message.reply_text("Kerakli bo'limni tanlang", reply_markup=btns('ctg', main=False))
        log['price'] = price

    elif menu == 2:

        # [KeyboardButton("HDMI Cabel"), KeyboardButton("🎥 Video Balun")],

        price = log.get("price", {})
        print(f"state: {state} menu: {menu} price: {price}")
        if state == 2:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 3
                log['NVR || DVR || XVR'] = msg
                update.message.reply_text("NVR || DVR || XVR Narxini kiriting👇")

        elif state == 3:
            if msg == "⬅️Back":
                log['state'] = 2
                del log['NVR || DVR || XVR']
                update.message.reply_text("NVR || DVR || XVR ni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_nvr'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 4:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 5
                log['IP || HD CAMERA'] = msg
                update.message.reply_text("IP || HD CAMERA Narxini kiriting👇")

        elif state == 5:
            if msg == "⬅️Back":
                log['state'] = 4
                del log['IP || HD CAMERA']
                update.message.reply_text("IP || HD CAMERA ni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_ip'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 6:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 7
                log['💽 HARD DISC'] = msg
                update.message.reply_text("💽 HARD DISC Narxini kiriting👇")

        elif state == 7:
            if msg == "⬅️Back":
                log['state'] = 6
                del log['💽 HARD DISC']
                update.message.reply_text("💽 HARD DISCni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_hard'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 8:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 9
                log['🔌 Block Pitaniya'] = msg
                update.message.reply_text("🔌 Block Pitaniya Cam Narxini kiriting👇")

        elif state == 9:
            if msg == "⬅️Back":
                log['state'] = 8
                del log['🔌 Block Pitaniya']
                update.message.reply_text("🔌 Camerani Block Pitaniyasini  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_pit'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")


        elif state == 10:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 11
                log['🔌Штекер(Vilka) BNC'] = msg
                update.message.reply_text("🔌Штекер(Vilka) BNC Narxini kiriting👇")

        elif state == 11:
            if msg == "⬅️Back":
                log['state'] = 10
                del log['🔌Штекер(Vilka) BNC']
                update.message.reply_text("🔌Штекер(Vilka) BNC ni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_vilka'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 12:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 13
                log['📻 Radio Kabel'] = msg
                update.message.reply_text("📻 Radio Kabel Narxini kiriting👇")

        elif state == 13:
            if msg == "⬅️Back":
                log['state'] = 12
                del log['📻 Radio Kabel']
                update.message.reply_text("📻 Radio Kabel turini  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_radio_kabel'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")



        elif state == 14:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 15
                log['🔌Штекер Xvostik'] = msg
                update.message.reply_text("🔌Штекер Xvostik Narxini kiriting👇")

        elif state == 15:
            if msg == "⬅️Back":
                log['state'] = 14
                del log['🔌Штекер Xvostik']
                update.message.reply_text("🔌Штекер Xvostik turini  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_shtaker_xvost'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")


        elif state == 16:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 17
                log['🎛Connector RJ45'] = msg
                update.message.reply_text("🎛Connector RJ45 Narxini kiriting👇")

        elif state == 17:
            if msg == "⬅️Back":
                log['state'] = 16
                del log['🎛Connector RJ45']
                update.message.reply_text("🎛Connector RJ45ni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_rj45'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 18:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 19
                log['KKB || UTB || CABEL'] = msg
                update.message.reply_text("KKB || UTB || CABEL Narxini kiriting👇")

        elif state == 19:
            if msg == "⬅️Back":
                log['state'] = 18
                del log['KKB || UTB || CABEL']
                update.message.reply_text("KKB || UTB || CABEL birini  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_kkb'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 20:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 21
                log['📡Setavoy Commutator'] = msg
                update.message.reply_text("📡Setavoy Commutator Narxini kiriting👇")

        elif state == 21:
            if msg == "⬅️Back":
                log['state'] = 20
                del log['📡Setavoy Commutator']
                update.message.reply_text("📡Setavoy Commutatorni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_setovoy_com'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        # [KeyboardButton("HDMI Cabel"), KeyboardButton("🎥 Video Balun")],

        elif state == 22:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 23
                log['HDMI Cabel'] = msg
                update.message.reply_text("HDMI Cabel Narxini kiriting👇")

        elif state == 23:
            if msg == "⬅️Back":
                log['state'] = 22
                del log['HDMI Cabel']
                update.message.reply_text("HDMI Cabelni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_hdmi_cabel'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")


        elif state == 24:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 25
                log['🎥 Video Balun'] = msg
                update.message.reply_text("🎥 Video Balun Narxini kiriting👇")

        elif state == 25:
            if msg == "⬅️Back":
                log['state'] = 24
                del log['🎥 Video Balun']
                update.message.reply_text("🎥 Video Balunni  kiriting", reply_markup=btns("next"))
            else:
                try:
                    price['price_video_balun'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")


        elif state == 26:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                log['state'] = 27
                log['Other'] = msg
                update.message.reply_text("💵 Qolgan narsalarni Umumiy Narxini kiriting")

        elif state == 27:
            if msg == "⬅️Back":
                log['state'] = 26
                del log['Other']
                update.message.reply_text(
                    "⌨️Qolgan narsalarni kirting\n⚠️Qolgan narsalarni qo'shganingizdan keyin avtomatik tarzda oxirgi natija chiqariladi",
                    reply_markup=btns("next"))
            else:
                try:
                    price['price_other'] = int(msg)
                    log['state'] = 30
                    update.message.reply_html(create_pub(log, calc_all(log['price'])), reply_markup=btns('price'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")

        elif state == 50:
            if msg == "⬅️Back":
                log['state'] = 0
                update.message.reply_text("Qo'shish uchun boshqa bo'limni tanlang👇", reply_markup=btns('cam'))
            else:
                try:
                    price['price_foyda'] = int(msg)
                    log['state'] = 0
                    update.message.reply_text("Foyda Qo'shildi. \nKeyingi bo'limni tanlang👇", reply_markup=btns('cam'))
                except:
                    update.message.reply_text("Narxni faqat raqamlardan foydalangan holda kiriting")
        elif state == 30:
            if msg == "UZS da ko'rsatish":
                _price = calc("USD", calc_all(price))
                update.message.reply_html(create_pub(log, _price, True), reply_markup=btns('head'))
                clear_log(user.id)
            else:
                update.message.reply_html(create_pub(log, calc_all(log['price'])), reply_markup=btns('head'))

        else:
            update.message.reply_text("Kerakli bo'limni tanlang", reply_markup=btns('cam', main=False))
        log['price'] = price
    change_log(user.id, log)
