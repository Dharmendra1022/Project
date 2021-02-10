class A():
    def __init__(self,inu):
       self.inu=inu
       #print(self.inu)
    def func1(self):
        s1=''
        count=None
        for i in (self.inu):
            if i.isupper() and (ord(i)>=65 and ord(i)<=90):
                count=(90-ord(i))+65
                s1=s1+chr(count)
            elif(ord(i)>=97 and ord(i)<=122):
                count=(122-ord(i))+97
                s1=s1+chr(count)
            else:
                s1=s1+i
               
        #print(s1)
        k= open("output1.txt.","w+")
        k.write(s1)
        k.close()
       
        
        
with open('C:\\Users\\HP\\Desktop\\book.txt', encoding = 'utf-8') as f:
    l=f.read()
    
a=A(l)
a.func1()
        
        
