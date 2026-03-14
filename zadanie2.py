cart = ['Jabłka', 'Banany']

def add_to_cart(item):
    # BŁĄD w podejściu funkcyjnym: modyfikujemy stan oryginalnej listy!
    cart.append(item) 
    return cart

add_to_cart('Pomarańcze')


cart = ['Jabłka', 'Banany']

# Czysta funkcja: zależy tylko od wejścia i tworzy nową strukturę
def add_to_cart(current_cart, item):
    return current_cart + [item] 

updated_cart = add_to_cart(cart, 'Pomarańcze')

print(cart)          # ['Jabłka', 'Banany'] - oryginał nietknięty!
print(updated_cart)  # ['Jabłka', 'Banany', 'Pomarańcze']