#dane wejsciowe 
data = [
    {"n": "A", "s": 6, "v": 15000},
    {"n": "B", "s": 2, "v": 10000},
    {"n": "C", "s": 10, "v": 30000}
]

#polecenia do zadania
#Napisz funkcję hr_lab_demo(), która przetworzy te dane w trzech krokach:
# 1. Filtrowanie (FILTER): Wybierz tylko tych pracowników, których staż pracy (s) jest większy niż 5 lat (tzw. seniorów).
# 2. Mapowanie (MAP): Dla wyselekcjonowanych seniorów oblicz wysokość premii, która wynosi 15% (0.15) ich wartości bazowej (v).
# 3. Redukcja (REDUCE): Zsumuj wszystkie wyliczone premie, aby uzyskać całkowity koszt, jaki firma musi ponieść.
#Niech funkcja zwraca trzy elementy w postaci krotki (tuple): listę seniorów, listę ich premii oraz całkowity koszt premii.
