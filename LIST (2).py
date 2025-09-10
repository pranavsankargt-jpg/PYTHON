##l=[]
##a=int(input('enter a limit:'))
##for i in range (0,a):
##    m=eval(input('enter the element:'))
##    l.append(m)
##print(l)
##
##l1=[1,2,3]
##l.extend(l1)
##print(l)
##l.extend([5,6,7]


d={'Eno':123,'Ename':'abc'}
print(d)
print(d['Eno'])
print(d.get('Ename'))

for key,values in d.items():
    print(key,':',values)
