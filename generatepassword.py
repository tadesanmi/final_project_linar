# A program that generates passwords randomly
import random
p = int(input("length of password:-"))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?/"
m = ""
for i in range(p):
    m = m+random.choice(s)
print(m)
