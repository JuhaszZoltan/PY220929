# 3x engedi, hogy próbálkozzak "belépni"
# ha sikerül, akkor kiíírja, hogy 'sikeres bejelentkezés'
# ha 3 próbálkozás után sem, akkor pedig kiírja, hogy 'beszélj a rendszergazdával'

pw = 'PassWord123'

probalkozasok_szama = 0
while probalkozasok_szama < 3 and input('írd be a jelszavad: ') != pw:
    probalkozasok_szama = probalkozasok_szama + 1

if probalkozasok_szama < 3:
    print('sikeres bejelentkezés!')
else:
    print('valami nem stimmel,\nkérlek beszélj a rendszergazdával!')