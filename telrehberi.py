import pickle
import os


def DisplayMenu() -> None:
    print("1. Kayıtları Listele")
    print("2. kayıt ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil ")
    print("5. Çıkış")
    print()




def Menuloop() -> str:
    while True:
        DisplayMenu()
        option = input("Seçenek 1-5: ")
        print("\n")
        if option.isdigit() and int(option) >= 1 and int(option) <= 5 :   ## option sayıysa ve 1 5 arasındaysa
            break

    return option


def mainLoop() -> None:
    while True:
        option = Menuloop()
        if option =="1":
            listRecords()
        elif option =="2":
            searchRecord()
        elif option =="3":
            addRecord()
        elif option =="4":
            deleteRecord()
        elif option =="5":
            break


def listRecords() -> None:
    recordsList=readFile()
    for record in recordsList:
        print(f"{record.get('name', ' '):10.10} {record.get('surName', ' '):10.10} {record.get('telNumber', ' '):10.10}")  ###10 lar boşluk ve tamamlama
    print()

def searchRecord() -> None:
    pass


def addRecord() -> None:
    print("Yeni Kayıt Ekle")
    name = input("İsim: ")
    surName= input("Soyisim: ")
    telNumber=input("Telefon Numarası: ")
    print(f"Yeni kayıt: {name} {surName}  {telNumber}" )
    if addRecord():
        addRecordToFile(name, surName, telNumber)
        print("kayıt Eklendi/n")


def deleteRecord() -> None:
    pass


def areYouSure() -> bool:
    while True:
        answer = input(" (E)vet / (H)ayır")
        print()
        if answer.upper == "E":  #### UPPEr ile büyük harfe çeviriyor
            return True
        elif answer.upper =='H':
            return False


def readFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            pickle.load(fileObject)
    else:
        recordsList = list()

    return recordsList


def writeFile(recordListParam, data=None) -> None:
    with open(data.bin, "wb") as fileObject:
        pickle.dump(recordListParam, fileObject)


def addRecordToFile(nameParam : str, surNameParam : str, telNumberParam : str) -> None :
    recordsList=()
    recordDict = dict(name=nameParam, surName=surNameParam, telNumber=telNumberParam)
    recordsList.append(recordDict)
    writeFile(recordsList)

mainLoop()