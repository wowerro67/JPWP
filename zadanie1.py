users = [
    {"name": "Anna", "is_active": True},
    {"name": "Jan", "is_active": False},
    {"name": "Maria", "is_active": True}
]

active_user_names = []
for user in users:
    if user["is_active"]:
        active_user_names.append(user["name"])
        
print(active_user_names) # ['Anna', 'Maria']


# Podejście ściśle funkcyjne (złożenie funkcji)
active_user_names = list(
    map(lambda user: user["name"], 
        filter(lambda user: user["is_active"], users))
)

print(active_user_names) # ['Anna', 'Maria']

#Uwaga dla prowadzących:** W Pythonie częstszą i bardziej "pythoniczną" alternatywą dla tego łańcucha jest tzw. *list comprehension* (`[user["name"] for user in users if user["is_active"]]`), które również ma charakter deklaratywny. Warto o tym wspomnieć jako o ciekawostce!