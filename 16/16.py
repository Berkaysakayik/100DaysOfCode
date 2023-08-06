import numpy as np

# print(help(np))

# print(np.__version__)

numarray = np.arange(10)
# print(numarray)

# for i in range(len(numarray)):
#     print(numarray[i])

# print(help(np.full))

#""" boolaray - 1 """

# np.full((3,3), True, dtype=bool)

# boolaray1 = np.full((3,3), True, dtype=bool)
# print("boolean array 1: \n",boolaray1)


#""" boolaray - 2 """

# boolaray2 = np.full((9), True, dtype=bool).reshape(3,3)
# print("boolean array 2: \n",boolaray2)


#""" boolaray - 3 """

# boolaray3 = np.ones((3,3),dtype=bool)
# print(boolaray3)


#""" boolaray - 4 """

# boolaray4 = np.ones((27),dtype=bool).reshape(3,3,3)
# print(boolaray4)


# odd numbers = tek sayılar

# numar = numarray[numarray%2 != 0]
# print("\nnumpy odd numbers: ", numar)


# even numbers = çift sayılar

# numar = numarray[numarray%2 == 0]
# print("\nnumpy even numbers: ", numar)


# Numpy array de belirli bir durumu başka bir değer ile nasıl yer değiştirirsin

# numarray[numarray%2 != 0] = -1
# print("\nnodd numbers but modificated: ", numarray)


# Numpy array de aslını değiştirmeden belirli bir durumu başka bir değer ile nasıl yer değiştirirsin

# marr = numarray.copy()
# marr[marr%2 == 1] = -1             # arrayimizdeki elemanların 2 ile bölümünde kalan var ise yerlerine -1 yazdırdık

# marr[(marr % 5)!=  0 ] *=-1      # değişik bir şey

# print(marr)