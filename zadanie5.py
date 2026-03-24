#dane wejsciowe 
logs = [
    "2026-03-24 10:01:05;IP:192.168.1.10;STATUS:200;USER:admin",
    "2026-03-24 10:01:08;IP:10.0.0.5;STATUS:401;USER:root",
    "2026-03-24 10:01:10;IP:10.0.0.5;STATUS:401;USER:guest",
    "2026-03-24 10:01:12;IP:192.168.1.12;STATUS:200;USER:user1",
    "2026-03-24 10:01:15;IP:10.0.0.5;STATUS:401;USER:admin"
]

from functools import reduce

#polecenie
# 1. Parsowanie (MAP): Przekształć każdy element listy logs z postaci tekstowej na słownik zawierający co najmniej dwa klucze: ip oraz status.
# 2. Filtrowanie (FILTER): Z nowej listy wyciągnij tylko te logi, które są nieudanymi próbami logowania (status to "401").
# 3. Ekstrakcja (MAP): Z przefiltrowanej listy wyciągnij wyłącznie same adresy IP w postaci listy ciągów znaków (stringów).
# 4. Raportowanie (REDUCE): Zlicz wystąpienia każdego adresu IP, tworząc słownik, w którym kluczem jest adres IP, a wartością liczba jego wystąpień (tzw. "Frequency Map").
