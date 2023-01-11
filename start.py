from my_math import my_math

def pobierz_rodzaj_dzialania():
    dzialanieIN = input("\nPodaj rodzaj dzialania, q - jezeli chcesz wyjsc\n (+, -, *, /):\t")
    if (len(dzialanieIN) >= 1 and str(dzialanieIN[0]) in '+-/*'):
        return str(dzialanieIN[0])
    elif (len(dzialanieIN) >= 1 and str(dzialanieIN[0]) == 'q'):
        return ""
    else:
        print("\n\tnieprawidlowy wybor !!!")
        pobierz_rodzaj_dzialania()


while True:
    dzialanie = pobierz_rodzaj_dzialania()
    #print(dzialanie)
    if not dzialanie: break
    try:
        liczba1 = float(input("Podaj pierwsza liczba: "))
        liczba2 = float(input("Podaj druga liczba   : "))
    except:
        print("\nNieodpowiednie dane wejsciowe!\n")
    if dzialanie == '+':
        print("Wynik:",my_math.dodawanie(liczba1, liczba2))
    elif dzialanie == '-':
        print("Wynik:", my_math.odejmowanie(liczba1, liczba2))
    elif dzialanie == '*':
        print("Wynik:",my_math.mnozenie(liczba1, liczba2))
    if dzialanie == '\\':
        print("Wynik:",my_math.dzielenie(liczba1, liczba2))