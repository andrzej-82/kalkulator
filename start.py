from my_math import my_math as m

def pobierz_rodzaj_dzialania():
    dzialanieIN = input("\nPodaj rodzaj dzialania, q - jezeli chcesz wyjsc\n (+, -, *, /):\t")
    if (len(dzialanieIN) >= 1 and str(dzialanieIN[0]) in '+-/*'):
        return str(dzialanieIN[0])
    elif (len(dzialanieIN) >= 1 and str(dzialanieIN[0]) == 'q'):
        return ""
    else:
        print("\n\tnieprawidlowy wybor !!!")
        pobierz_rodzaj_dzialania()

def wykonaj_dzialanie(funkcja, liczba1, liczba2):
    return funkcja(liczba1,liczba2)



while True:
    dzialanie = pobierz_rodzaj_dzialania()
    #print(dzialanie)
    if not dzialanie: break
    try:
        liczba1 = float(input("Podaj pierwsza liczba: "))
        liczba2 = float(input("Podaj druga liczba   : "))
    except:
        print("\nNieodpowiednie dane wejsciowe!\n")
    slownik_dzialan = {'+':m.dodawanie, '-':m.odejmowanie, '*':m.mnozenie, '/':m.dzielenie}
    print("Wynik dzialania: ", wykonaj_dzialanie(slownik_dzialan[dzialanie], liczba1, liczba2))
