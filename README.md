# JPWP

ZADANIE 1
# Zrefaktoryzuj powyższy kod na styl funkcyjny
# 1. Pozbądź się pętli 'for' oraz instrukcji 'if'.
# 2. Użyj wbudowanych funkcji: map() oraz filter().
# 3. Zastosuj wyrażenia 'lambda'.

ZADANIE 2
# Zrefaktoryzuj powyższy kod na styl funkcyjny
# 1. Przerób 'add_to_cart' na czystą funkcję (pure function).
# 2. Funkcja powinna przyjmować obecny koszyk oraz nowy element jako argumenty.
# 3. Zastosuj zasadę niemutowalności (nie używaj metody .append()).
# 4. Funkcja ma zwracać nową listę, zostawiając oryginalny 'cart' bez zmian.

ZADANIE 3
# Zrefaktoryzuj powyższy kod na styl funkcyjny!
# 1. Pozbądź się pętli 'for' oraz zmiennej akumulującej 'total'.
# 2. Użyj funkcji reduce() zaimportowanej na górze pliku.
# 3. Zastosuj wyrażenie 'lambda' do zsumowania elementów listy.

ZADANIE 4
#Napisz funkcję hr_lab_demo(), która przetworzy te dane w trzech krokach:
# 1. Filtrowanie (FILTER): Wybierz tylko tych pracowników, których staż pracy (s) jest większy niż 5 lat (tzw. seniorów).
# 2. Mapowanie (MAP): Dla wyselekcjonowanych seniorów oblicz wysokość premii, która wynosi 15% (0.15) ich wartości bazowej (v).
# 3. Redukcja (REDUCE): Zsumuj wszystkie wyliczone premie, aby uzyskać całkowity koszt, jaki firma musi ponieść.
#Niech funkcja zwraca trzy elementy w postaci krotki (tuple): listę seniorów, listę ich premii oraz całkowity koszt premii.

ZADANIE 5
# 1. Parsowanie (MAP): Przekształć każdy element listy logs z postaci tekstowej na słownik zawierający co najmniej dwa klucze: ip oraz status.
# 2. Filtrowanie (FILTER): Z nowej listy wyciągnij tylko te logi, które są nieudanymi próbami logowania (status to "401").
# 3. Ekstrakcja (MAP): Z przefiltrowanej listy wyciągnij wyłącznie same adresy IP w postaci listy ciągów znaków (stringów).
# 4. Raportowanie (REDUCE): Zlicz wystąpienia każdego adresu IP, tworząc słownik, w którym kluczem jest adres IP, a wartością liczba jego wystąpień (tzw. "Frequency Map").


