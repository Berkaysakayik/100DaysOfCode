import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("iris.csv")

print(data.head())                           # data setinin ilk 5 datasını gösterir
#print(data.tail())                            # data setinin son 5 datasını gösterir
print(data.isnull().sum())                 # csv içerisinde boş (null) data olup olmadığını kontrol et, varsa kaç adet olduğunu topla

data.rename(columns={'SepalLengthCm':'Sepal_length_cm',
                   'SepalWidthCm':'Sepal_width_cm',
                   'PetalLengthCm':'Petal_length_cm',
                   'PetalWidthCm':'Petal_width_cm',},inplace=True)

print(data.head(15))                      # data setinin ilk parantez içerisi kadar datasını gösterir

 
s= data['Species'].unique()           # datanın "Species" kolonunun farklı değerlerini listele

for sp in s:
    print("Species: ",sp)                 # listelenen veriyi yazdır


Iris_setosa = data[data['Species'] == 'Iris-setosa'].value_counts().sum()    # datanın "Spieces" kolonunda kaç tane "Iris-setosa" olduğunu say ve kaç tane olduğunu topla
print("How many we have Iris-setosa: ",Iris_setosa)

# print(data[data['Species']=='Iris-setosa'])                                                 # bütün datadaki "Iris-setosa" ya ait verileri gösterir

Iris_versicolor = data[data['Species'] == 'Iris-versicolor'].value_counts().sum()    # datanın "Spieces" kolonunda kaç tane "Iris-versicolor" olduğunu say ve kaç tane olduğunu topla
print("How many we have Iris-versicolor: ",Iris_versicolor)

Iris_virginica = data[data['Species'] == 'Iris-virginica'].value_counts().sum()    # datanın "Spieces" kolonunda kaç tane "Iris-virginica" olduğunu say ve kaç tane olduğunu topla
print("How many we have Iris-virginica: ",Iris_virginica)


colmn = data.columns                   # kaç tane sütun olduğunu bul

for col in colmn:
    print("Column: ",col)                  # sütunları yazdır


"##################### GÖRSELSSSS #####################"


sns.pairplot(data,hue='Species', diag_kind='hist')
plt.show()


sns.violinplot(x = 'Species', y ='Petal_length_cm', data = data)
plt.title("petal length by species")
plt.show()


sns.swarmplot(x = 'Species', y ='Petal_length_cm', data = data)
plt.title("petal length by species")
plt.show()


sns.barplot(x = 'Species', y ='Petal_length_cm', data = data)
plt.title("petal length by species")
plt.show()


plt.figure(figsize=(16,7))
x = plt.xticks(rotation=90)
sns.kdeplot(data = data, x = "Sepal_length_cm", hue = 'Species', shade = True)
plt.show()
