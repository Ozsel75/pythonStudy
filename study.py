
from bs4 import BeautifulSoup
import requests
import random
tcno = (input(" tcnizi giriniz ? : "))


def tcvalid(tcno) -> bool:
    if len(tcno != 11):
        print("not valid")

    teknolar = (int(tcno[0])+int(tcno[2]) +
                int(tcno[4])+int(tcno[6])+int(tcno[8]))
    ciftnolar = (int(tcno[1]) + int(tcno[3]) + int(tcno[5]) + int(tcno[7]))
    if ((teknolar*7-ciftnolar) % 10 == int(tcno[9])):
        print("valid")
    else:
        print("not valid")


tcvalid(tcno)


""""  POLİNDROM KONTROL """
index = input("lütfen girin ")
poly = index[::-1]
if index == poly:
    print(f"polindrom budur {poly}")
else:
    print(f"bu {index} polindrom değil")
"""
""" POLİNDROME HOCA


def ispoli(string: str) -> bool:
    reverse = ""
    for character in string:
        reverse = character + reverse
    if string == reverse:
        return True
    return False


string = "nalan"
if ispoli(string):
    print(f"bu {string} polindrom dur")
else:
    print(f"bu {string} polindrome değildir")
"""

"""


def vertcno(tcno: str) -> bool:
    ciftsayilar = 0
    teksayilar = 0
    index = 0
    for number in tcno:
        if index > 9:
            break
        if index % 2 == 0:
            ciftsayilar += int(number)
        else:
            teksayilar += int(number)
        index += 1
    if (teksayilar*7-ciftsayilar) % 10 == int(tcno[9]):
        return true
    else:
        return false


tcno = (input(" tcnizi giriniz ? : "))
if vertcno(tcno) is true:
    print("bu tc no verified")
else:
    print("yannış")
"""

"""" RANDOM ŞİFRE YARATMA FOR KULLANARAK

characters = "abcdefghjklmmnoprstyuwz123456776780!'^++%&+&/(=)"
password = ""

for index in range(random.randint(5, 10)):
    password += random.choice(characters)

print(password)
"""

"""   ÖDEV 14
counter = 0
number = []
while counter < 4:
    tamsayi = int(input("lütfen tam sayı girin"))
    if tamsayi not in number:
        number.append(tamsayi)
    else:
        print("bu sayi zaten listede")
    counter += 1

print(number)

"""
### 2020 - 1900 artık yıl hesaplayan ÖDEV 13###
"""


def leapyear(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False


for year in range(2020, 1900, -1):
    if leapyear(year):
        print(f"{year} is leap year")
"""

### FOR KULLANIMI ###

"""
numbers = [1, 2, 3, 4, 5, 65, 48, 81]
squares = []
for number in numbers:
    squares.append(number**2)

print(squares)

# FOR DA RANGE KULLANIMI 3 E BÖLÜNENLER
numbers2 = [number2 for number2 in range(2, 100) if number2 % 3 == 0]

print(numbers2)

"""

# ÖDEV 15

"""
list = []
counter = 1
while counter < 5:
    isim = input("lütfen isim giriniz : ")
    if isim in list:
        print("bu isim daha önce girildi")
        continue
    else:
        list.append(isim)

    counter += 1
print(list)
"""

# SÖZLÜKLER - KEY VE VALUE DEĞERLERİNDEN OLUŞUR SÜSLÜ PARANTEZ veya dict(key="value")  İLE OLUŞTURULUR
"""
customer = {
    "name": "Öz sel",
    "Tel": "05434636821",
    "email": "sanane@socc",
    "KEY": "VALUE"
}
print(customer)
print(customer["name"])
for key in customer:
    print(f"{key}= {customer[key]}")

"""

# DOSYALAR   ## W HER SEFERİNDE YENİ DOSYA, R SADECE OKUMAK İÇİN, A YENİ DOSYA VE KALAN YERDEN YENİ VER EKLEMEK İÇİN , A+ OKUMAK TA İÇİN

"""
with open("deneme.txt", "a+", encoding="utf-8") as file:
    file.write("Bu\n")
    file.write("örnek\n")
    file.write("metindir.")

    list = ["naber", "nasılsın\n"]
    file.writelines(list)  # LİST EKLEMEK İÇİN

    file.seek(0)  # CURSORUN KONUMUNU BELİRLEMEK İÇİN
    text = file.read()
    print(text)

    text = text[::-1]  # METİN VEYA LİSTE TERSE ÇEVİRMEK İÇİN
"""

# ÖDEV  18 GİRİLEN CÜMLEDE YASAKLI KELİMELERİN YERİNE *** YAZ

"""
bannedwords = ["amk", "aq"]
string = input("bir cümle giriniz : ")

words = string.split()  # CÜMLENİN İÇİNDE KELİMELERİ AYIRIP LİSTE YAPIYOR SPLİT KOMUTU

string = ""
for word in words:
    if word in bannedwords:
        string += "***"
    else:
        string += f"{word} "

print(string)

"""

# HATA AYIKLAMA  TRY   EXCEPT
"""
counter = 1


while True:
    try:
        age = int(input("yaşınızı giriniz: "))

    except ValueError:  # hata varsa işler
        print("Hatalı giriş yaptınız")
    except Exception:
        # her hangi bir hata oluştuğunda çalışır
        print("herhangi bir hata oluştu")
    else:
        print(f"{age} yaşındasınız")  # hata yoksa geldiyse buraya geçer
        break
    finally:  # hata alınsada alınmasada bu satır çalışır
        print(f"döngü {counter} kere çalıştı")
        counter += 1
        if counter > 5:
            # kendimiz bir hata verdirttik
            raise ValueError("çok fazla deneme")
"""

# REQUESTS İLE GITHUBTAN VERİ ÇEKME

"""


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def getUser(self, userName):
        response = requests.get(self.api_url+"/users/"+userName)
        return response.json()

    def repoStories(self, userName):
        response = requests.get(self.api_url+'/users/'+userName+"/repos")
        return response.json()


github = Github()


while True:
    secim = input(
        "1-Find User\n2-Get repositories\n3-Create repository\n4-Exit\n Seçim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            userName = input("Kullanıcı adı")
            result = github.getUser(userName)
            print(
                f"name:{result['name']} public repos:{result['public_repos']} follower: {result['followers']}  ")
        elif secim == "2":
            userName = input("Kullanıcı adı")
            result = github.getUser(userName)
            for repo in result:
                print(repo['name'])
        elif secim == "3":
            pass
        else:
            print("Yanlış seçim")
"""

# BEAUTIFULSOUP KULLANIMI html den bilgi çekmek için

"""

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()
result = soup.title

print(result)
"""


# RETURN ÇALIŞMASI İLE İLGİLİ

"""


def toplam(a, b):
    return a + b


a = int(input("a değer girin"))
b = int(input("a değer girin"))


print(toplam(a, b))
"""
