import random
lower_case='abcdefghijklmnopqrstuvwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym='!@$#%&*().'
num='0123456789'

string=lower_case+upper_case+sym+num
length=int(input("enter length"))
password="".join(random.sample(string,length))
print("your desired passoword is",password)
