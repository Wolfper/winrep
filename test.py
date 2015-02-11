
def zgadne(x):
    import random
    import time
    t1 = time.time()
    z = random.randint(0, 101)
    #while (x != z):
    print(t1)
    target = [z for z in range(0,101) if z == x]
    t2 = time.time()
    print(t2)
    tdelta = t2 -t1
    print(tdelta)
    print('twoja liczba {} {}'.format(target[0], tdelta))

def opis1(liczzgadywana, krok):
    print('Komputer wprowadził liczbę {} w kroku {}'.format(liczzgadywana, krok))

import pdb
def zgadne2(x):
    import random
    import time
    t1 = time.time()
    liczzgadywana = random.randint(0, 101)
    krok = 0
    while x != liczzgadywana:
        krok +=1

        licz1 = liczzgadywana
        liczzgadywana = random.randint(licz1,int(liczzgadywana+1))
        print(licz1, liczzgadywana+1)

        #pdb.set_trace()

        if x< liczzgadywana :
            opis1(liczzgadywana,krok)
            zmienna1 = liczzgadywana
            liczzgadywana = int(liczzgadywana /2)
            print(' {} / 2 ={}'.format(zmienna1, liczzgadywana))
            continue

        elif x > liczzgadywana:
            opis1(liczzgadywana,krok)
            liczzgadywana = int(liczzgadywana * 1.3)
            continue
        print(liczzgadywana)
    t2 = time.time()
    tdelta = t2 - t1
    print(tdelta)

    print('ta liczba to {}'.format(liczzgadywana))
import sys
import pdb
c = int(input('Podaj lizbę od 1 so 100: '))
zgadne2(c)
zgadne(c)
#pdb.set_trace()