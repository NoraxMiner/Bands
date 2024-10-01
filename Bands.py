input_data = open('input.txt', 'r') 

data = input_data.read() 
#--------------------------------------------------------------------
H = int
L = int 
X = int
Y = int 


data = data.split()
H = int(data[0])
L = int(data[1])
V = int(data[2])


X = V - H
Y = V - L

X = str(X)
Y = str(Y)
aut = str(X +' '+ Y)
#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(aut))


# Закрываем открытые ранее файлы!
input_data.close() 
output_data.close()