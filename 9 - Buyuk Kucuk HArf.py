kucuk = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

buyuk = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def harfsayisi(kelime):
    kucuktoplam = []
    buyuktoplam = []

    for i in kelime:
        if i in kucuk:
            kucuktoplam+=i
        else:
            buyuktoplam+=i

    return kucuktoplam,buyuktoplam
while True:
    a = input("Lutfen Kelimeyi Giriniz : ")
    print("Buyuk Ve Kucuk HArfler : ",harfsayisi(a),"\n")