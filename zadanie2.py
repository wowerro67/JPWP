cart = ['Jabłka', 'Banany']

def add_to_cart(item):
    # Podejście imperatywne: modyfikujemy stan oryginalnej listy!
    cart.append(item) 
    return cart

updated_cart = add_to_cart('Pomarańcze')

print("Oryginalny koszyk po dodaniu:", cart) # Uwaga: oryginał został zmieniony!
print("Zaktualizowany koszyk:", updated_cart)

# ==========================================
# TODO: Zrefaktoryzuj powyższy kod na styl funkcyjny!
# 1. Przerób 'add_to_cart' na czystą funkcję (pure function).
# 2. Funkcja powinna przyjmować obecny koszyk oraz nowy element jako argumenty.
# 3. Zastosuj zasadę niemutowalności (nie używaj metody .append()!).
# 4. Funkcja ma zwracać nową listę, zostawiając oryginalny 'cart' bez zmian.
# ==========================================

# Tutaj wpisz swój kod funkcyjny:
