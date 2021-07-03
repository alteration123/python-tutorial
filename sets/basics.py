# non sono ordinati, mutabili, non accettano duplicati

myset = set()
myset = set("Hello")
myset = {"H", "e", "l", "l", "o"}
print(myset)

# output -> {'o', 'e', 'H', 'l'}

myset.add("k")
myset.remove("k")  # -> lancia eccezione se non trova
myset.discard("k")  # -> NON lancia eccezione se non trova

popped = myset.pop()  # -> preleva e rimuove

if "H" in myset:
    print("H in myset")
