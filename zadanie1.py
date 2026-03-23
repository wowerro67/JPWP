users = [
    {"name": "Anna", "is_active": True},
    {"name": "Jan", "is_active": False},
    {"name": "Maria", "is_active": True}
]

active_user_names = []
for user in users:
    if user["is_active"]:
        active_user_names.append(user["name"])
        
print("Wynik imperatywny:", active_user_names) 


# Zrefaktoryzuj powyższy kod na styl funkcyjny
# 1. Pozbądź się pętli 'for' oraz instrukcji 'if'.
# 2. Użyj wbudowanych funkcji: map() oraz filter().
# 3. Zastosuj wyrażenia 'lambda'.

