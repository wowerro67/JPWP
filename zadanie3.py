from functools import reduce # Ta biblioteka przyda Ci się do rozwiązania!

prices = [10, 20, 30.5, 15]
total = 0

# Podejście imperatywne: pętla modyfikująca stan zmiennej total
for price in prices:
    total += price
    
print("Suma imperatywna:", total) # 75.5

# ==========================================
# TODO: Zrefaktoryzuj powyższy kod na styl funkcyjny!
# 1. Pozbądź się pętli 'for' oraz zmiennej akumulującej 'total'.
# 2. Użyj funkcji reduce() zaimportowanej na górze pliku.
# 3. Zastosuj wyrażenie 'lambda' do zsumowania elementów listy.
# ==========================================

# Tutaj wpisz swój kod funkcyjny:
