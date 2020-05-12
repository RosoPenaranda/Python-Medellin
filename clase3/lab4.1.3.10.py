# regresa cuantas millas por galon gasta recibe litros
#galón =  liters/3.785411784
# milla = 1609.344 metros.

'''
1 milla = 1609.344 metros.
  x          100km

  x = 100000 m * 1milla / 1609.344 m

'''


def l100kmtompg(liters):
    millas = 100000/609.344
    galon = liters/3.785411784

    return millas/galon


'''
    metro cosumio  litos
    100km            x litro
'''


def mpgtol100km(miles):
    metros = miles * 1609.344
    litros = 3.785411784
    return (1000000*litros)/metros


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
