# LISTA létrehozása: <lista_neve = [lista_elem, lista_elem, ...]>:
#           0         1         2         3          4         5         6
nevek = ['Bianka', 'Emese', 'Zsuzsa', 'Zsuzsa', 'Veronika', 'Zsófi', 'Renáta']

# lista elemeinek bejárása for ciklussal:
for nev in nevek:
    print(nev)

# új elem hozzáadása listához:
nevek.append("Kata")
print(nevek)

# első azonos ÉRTÉKŰ elem eltávolítása listáról:
nevek.remove('Zsuzsa')
print(nevek)

# adatt INDEXŰ elem megváltoztatása:
nevek[3] = 'Pál'
print(nevek)

# visszaadja adott ÉRTÉKŰ elem INDEXÉT
keresett_index = nevek.index('Emese')
print(f'Emese indexe: {keresett_index}')

# + előzővel kombinálva:
# adott ÉRTÉKŰ elem megváltoztatása:
nevek[nevek.index('Emese')] = 'Kriszta'
print(nevek)

# lista elemeinek száma:
elemek_szama = len(nevek)
print(f'lista elemeinek száma: {elemek_szama}')