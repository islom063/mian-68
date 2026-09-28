class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, username, parol):
        super().__init__(ism, yosh)
        self.username = username
        self.parol = parol

class Talaba(Foydalanuvchi):
    def __init__(self, ism, yosh, username, parol, talaba_id):
        super().__init__(ism, yosh, username, parol)
        self.talaba_id = talaba_id
        self.kurslar = []

    def kursga_yozil(self, kurs):
        self.kurslar.append(kurs)

class Oqituvchi(Foydalanuvchi):
    def __init__(self, ism, yosh, username, parol, mutaxassislik):
        super().__init__(ism, yosh, username, parol)
        self.mutaxassislik = mutaxassislik

class Administrator(Foydalanuvchi):
    def __init__(self, ism, yosh, username, parol, daraja):
        super().__init__(ism, yosh, username, parol)
        self.daraja = daraja

class Hisob:
    def __init__(self, balans=0):
        self.balans = balans

class Tolov(Hisob):
    def __init__(self, summa, talaba):
        super().__init__()
        self.summa = summa
        self.talaba = talaba

class Kassa:
    def __init__(self):
        self.tolovlar = []

    def tolov_qabul_qilish(self, tolov):
        self.tolovlar.append(tolov)

class Chek:
    def __init__(self, tolov):
        self.tolov = tolov

class Chegirma:
    def __init__(self, foiz):
        self.foiz = foiz

class Bino:
    def __init__(self, manzil):
        self.manzil = manzil
        self.xonalar = []

class Xona:
    def __init__(self, raqam, sigim):
        self.raqam = raqam
        self.sigim = sigim

class Jadval:
    def __init__(self, kun, vaqt):
        self.kun = kun
        self.vaqt = vaqt

class Fan:
    def __init__(self, nomi, qiyinlik_darajasi):
        self.nomi = nomi
        self.qiyinlik_darajasi = qiyinlik_darajasi

class Kurs:
    def __init__(self, fan, oqituvchi, narx):
        self.fan = fan
        self.oqituvchi = oqituvchi
        self.narx = narx

class Imtihon:
    def __init__(self, fan, max_ball):
        self.fan = fan
        self.max_ball = max_ball

class Natija:
    def __init__(self, talaba, imtihon, toplagan_ball):
        self.talaba = talaba
        self.imtihon = imtihon
        self.toplagan_ball = toplagan_ball

class Sertifikat:
    def __init__(self, talaba, kurs):
        self.talaba = talaba
        self.kurs = kurs

class Xabar:
    def __init__(self, qabul_qiluvchi, matn):
        self.qabul_qiluvchi = qabul_qiluvchi
        self.matn = matn

class OquvMarkazi:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
        self.kurslar = []
        self.kassa = Kassa()


if __name__ == "__main__":
    centr = OquvMarkazi("Tech Academy")
    python_fani = Fan("Python Dasturlash", "O'rta")
    ustoz = Oqituvchi("Anvar", 30, "anvar_dev", "1234", "Senior Backend")
    python_kursi = Kurs(python_fani, ustoz, 300)
    centr.kurslar.append(python_kursi)

    talaba1 = Talaba("Islom", 19, "islom_dev", "qwerty", "T-001")
    talaba1.kursga_yozil(python_kursi)
    centr.talabalar.append(talaba1)

    tolov1 = Tolov(300, talaba1)
    centr.kassa.tolov_qabul_qilish(tolov1)

    print(f"O'quv Markazi: {centr.nomi}")
    print(f"Kurs: {python_kursi.fan.nomi} | O'qituvchi: {python_kursi.oqituvchi.ism}")
    print(f"Talaba: {talaba1.ism} ({talaba1.talaba_id}) kursga yozildi va {tolov1.summa}$ to'ladi.")