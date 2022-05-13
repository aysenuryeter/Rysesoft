#Ayşenur YETER
#aysenuryeter@gmail.com

#Python

for number in range(1,100):
    if(number %3 == 0 and number %7 == 0 ):
        print("Açık Kaynak")
    elif(number %3 == 0):
        print("Açık")
    elif(number % 7 == 0):
        print("Kaynak")
    else:
        print(number)