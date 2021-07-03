lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Troie"]

# extend -> equivalente di array_merge
friends.extend(lucky_numbers)

# append -> aggiunge elemento
friends.append(5)

# insert -> specifico la posizione
friends.insert(1, "cacca")

# remove -> rimuove elemento

# clear -> pulisce tutto

# pop -> poppa un item

# index -> trova elemento
# throwa eccezione se elemento non è nella lista
friends.index("Paolo", 1, len(friends))

# sort -> ordina

# reverse -> inverte

# count -> conta elementi di un certo tipo
friends.count("cacca")

# copy -> clona lista
friends2 = friends.copy()
