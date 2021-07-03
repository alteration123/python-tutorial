odds = {1, 3, 5}
evens = {0, 2, 4}
primes = {2, 3, 5, 7}

# unione
u = odds.union(evens)
print(u)

# intersezione
i = odds.intersection(odds, primes)
print(i)

# differenza
d = odds.difference(primes)
print(d)

# è il contrario dell'intersezione, prende quelli NON in comune
sd = odds.symmetric_difference(primes)

# se non vogliamo un nuvo set ma modificare uno esistente
backupOdds = odds

# unione updatando
backupOdds.update(evens)
print(backupOdds)

# vedere se è un subset/contenuto
print({2, 3}.issubset(primes))

# vedere invece se contiene/superset
print(primes.issuperset({2, 3}))

# vedere se hanno elementi in comune
print(evens.isdisjoint(odds))

# assegnamento -> quando si assegna c'è la referenza, infatti
# anche odds è cambiato
# per clonare:
realBackupOdds = set(odds)
