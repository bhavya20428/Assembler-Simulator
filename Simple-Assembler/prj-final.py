import sys

#f = open("test.txt","w")

co=""

for line in sys.stdin:
    if line=="":
        break;
    co+=line
	#f.write(line)

#f.close()





import sys

var_check=0

vrrp=0
varchk=0
vars1=[]

def checker(x):
    if x=="R0":
        v="000"
        return(v)
                    
    if x=="R1":
        
        v="001"
        return(v)
                
    if x=="R2":
        
        v="010"
        return(v)
                    
    if x=="R3":
        v="011"
        return(v)
                
    if x=="R4":
        v="100"
        return(v)
                    
    if x=="R5":
        v="101"
        return(v)
                
    if x=="R6":
        v="110"
        return(v)
    


def abcd(z):
    
    bnr=bin(z).replace('0b','')
  
    
  
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


def instruction(character):
    instructions =['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
    if character not in instructions:
        return True
counter=0
#f=open("x1.txt","w+")

#file1 = open("test.txt","r")
fin=""



#file2=file1.read()





hlt=0

#file3=file2.split("\n")
length=len(co.splitlines())
if length>256:
    b= "Error: commands out of supported max limit "
    print(b)
    o = open("output.txt", "w")
    o.write(b)
    sys.exit()

if length<=0:
    b= "Error: no commands entered "
    print(b)
    o = open("output.txt", "w")
    o.write(b)
    sys.exit()

    

for x in co.splitlines():
    if x.startswith("var"):
        vrrp=vrrp
    else:
        vrrp=vrrp+1
        
#print("fin:",vrrp-1)
vrrpx=vrrp
vrrp=vrrp-1




#for x in file3:
    #print("X:",x)
#print("length:",length)

label={}

count = 0

for x in co.splitlines():
    temp1=x.split(" ")
    if x.startswith("var"):
        count=count
    else:
        count+=1
    if temp1[0]=='hlt':
        hlt=1
    #print(temp1)
    if temp1[0]!='' and temp1[0][-1]==":":
        
        if len(temp1)>1:
            if temp1[1]=="hlt":
                hlt=1
            label.update({temp1[0]:count})
        
    
    
        
    

if hlt==0:
    b= "Error: hlt not present "
    print(b)
    o = open("output.txt", "w")
    o.write(b)
    sys.exit()







lst=["R0","R1","R2","R3","R4","R5","R6"]

vars={}
xc=dict()
output = open("output.txt", "w")

for y in co.splitlines():

    y=y.replace('\t',' ')
    
    
    
    if y:

        temp=y.split()
        

        #temp=y.split(" ")
        #print("temp+",temp)
    
        counter=counter+1
        buffer=str()
        #print("COUNTER:",counter)
        
        
        flag=True
        for x in temp:


            
            
           
                
            
            
            
            
            
            
            
            
            #print("x=",x)
            #print("printed",x[0])
                      
                              
            
            
            if temp[0]!='var':
                #print("check here",temp[0])
                varchk=varchk+1
                
                #print("inc")
            
            
            if len(temp)==3:
                if temp[2]=="FLAGS" and temp[0]!="mov":
                    b="Error: Illegal use of FLAGS reg in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()
                
                    
                    

            if x=='hlt':
                
                flag=False
                if hlt==1:
                
                
        
                    if counter==length:
                    #print("1001100000000000")
                        buffer += "1001100000000000"
                    
                    if counter<length:
                        
                        #print("counter:",counter,length)
                    
                    
                    
                        b= "Error: hlt not at end of the file instead at line "+str(counter)
                        print(b)
                        o = open("output.txt", "w")
                        o.write(b)
                        sys.exit()
                        
                if hlt==0:
                    b= "Error: hlt not present"
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()

            if temp[0].startswith("$") or temp[0].startswith("R0") or temp[0].startswith("R1") or temp[0].startswith("R2") or temp[0].startswith("R3") or temp[0].startswith("R4") or temp[0].startswith("R5") or temp[0].startswith("R6"):
                b= "Error: Wrong syntax in line "+str(counter)
                print(b)
                o = open("output.txt", "w")
                o.write(b)
                sys.exit()
                    

            if x=="R0" or x=="R0\n":
                #print("000",end='')
                buffer += "000"
                
                        
            if x=="R1" or x=="R1\n":
                #print("001",end='')
                buffer += "001"
                
                    
            if x=="R2" or x=="R2\n":
                #print("010",end='')
                buffer += "010"
                        
            if x=="R3" or x=="R3\n":
                #print("011",end='')
                buffer += "011"
                    
            if x=="R4" or x=="R4\n":
                #print("100",end='')
                buffer += "100"
                        
            if x=="R5" or x=="R5\n":
                #print("101",end='')
                buffer += "101"
                    
            if x=="R6" or x=="R6\n":
                #print("110",end='')
                buffer += "110"
            if x=="FLAGS" or x=="FLAGS\n":
                buffer += "111"
                
            if x[0]=="R": 
                
                if int(x[1])<0 or int(x[1])>6:
                    b= "Error: Wrong resistor name in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()

                    
            if x!="var":
                var_check=1
                    
                    
            if x[0]=='$':
                
                if int(x[1:])>=0 and int(x[1:])<=256:
                    buffer += abcd(int(x[1:]))
                
                else:
                    
                    b= "Error: Wrong immediate value in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()
                    
                
                        
            if x=="add":
                
                flag=False
                if len(temp)!=4:
                    #print("Syntax Error")
                    b="Syntax Error in line "+str(counter)

                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()
                        
                #print("0000000",end='')
                buffer += "0000000"
            
            
            
            
            if x[len(x)-1]==":":

                
                flag = False

                if len(temp)==1:
                    b= "Error: No label definition provided in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()

                if(instruction(temp[1])):
                    b= "Error: Wrong instruction used in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()

                

                
                
                if temp[1]==":":


                    
                    b= "Error: Wrong label decleration in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()
                    
                
                for g in x[:-1]:
                    
                    #print("g",g)
                    if g.isalnum()==True or g=="_" :

                        #print("sats")
                        
                        cont=1
                    else:
                        #print("not sats")
                        cont=0
                        break;
                        
                    
                            
                if cont==1:    
                
                    #print ("ddddddd=",x[len(x)-1])
                    if temp[0] not in xc.keys():    
                        l=temp[0]
                        #print(l)
                        
                        xc.update({l:counter})
                        #print(xc)

                    elif temp[0] in xc.keys():
                        b= "Error: cannot define a label with the same name multiple times at line "+str(counter)
                        print(b)
                        o = open("output.txt", "w")
                        o.write(b)
                        sys.exit()
                    

                
                    
                    
                    temp=temp[1:]
                    
                if cont==0:
                    b= "Error: Wrong label decleration in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
      
            if x=='var':
                flag=False
                
                if var_check==0 and len(temp)==2 and temp[1].isalpha()==True:
                
                    v=temp[1]
                    
                    vars.update({v:counter})
                    vars1.append(v)
                   # print("caa",vars)
                    
                elif var_check==1 or len(temp)!=2 or temp[1].isalpha()==False:
                    b= "Error: Wrong variable decleration in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    break;
                break;
                    
            
            if x=="sub":

                flag=False

                if len(temp)!=4:
                    #print("Syntax Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    break;
                #print("00001",end='')
                buffer += "0000100"
    
            if x=="mov" and temp[2][0]=="$":

                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                #print("00010",end='')
                buffer += "00010"
                
            if x=="mov" and temp[2][0]!="$":
                flag=False
                        
                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                if temp[2][0]!="R" and temp[2][0]!="F":
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                    sys.exit()
                    
                    sys.exit()
                #print("0001100000",end='')
                buffer += "0001100000"
            
            if x=='ld':
                flag=False
                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                n=temp[2]
                #print("n=",n)
                #print("vars:",vars)
                #print("vars1",vars1)
                xx=False
                
                
                
    
                for g in vars.keys():
                    #print("g=",g)
                    
                    
                    if n == g:
                        #print("true")
                        xx=True
                        #print("00101",end='')
                        buffer += "00100"
                        #print(buffer)
                        
                        
                        buffer += checker(temp[1])
                        
                        #print("error:",checker(temp[1]))
                        #print(abcd(counter),end='')
                        #print("varchk:",varchk)
                        #print(vars[g])
                        var=vrrp+vars[g]
                        #print(var)
                        
                        #print("var:",var)
                        buffer += abcd(var)
                        #print("buffer:",buffer)
                        break;
                    else:
                        
                        for g in xc.keys():
                            
                           
                            if n+":"==g:
                                
                                b= "Error: Misuse of label as variable in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
                
                                
                                sys.exit()
                              
                
                if xx!=True:
                    b= "Variable not defined in line "+str(counter)
                    
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    break;
                break;
                
                        
           
            if x=='st':
                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                n=temp[2]
                #print("n=",n)
                #print("vars:",vars)
                #print("vars1",vars1)

                xx=False
                
                
                
    
                for g in vars.keys():
                    #print("g=",g)
                    
                    
                    if n == g:
                        #print("true")
                        xx=True
                        #print("00101",end='')
                        buffer += "00101"
                        #print(buffer)
                        
                        
                        buffer += checker(temp[1])
                        
                        #print("error:",checker(temp[1]))
                        #print(abcd(counter),end='')
                        #print("varchk:",varchk)
                        #print(vars[g])
                        var=vrrp+vars[g]
                        #print(var)
                        
                        #print("var:",var)
                        buffer += abcd(var)
                        #print("buffer:",buffer)
                        break;
                    else:
                        
                        for g in xc.keys():
                            
                           
                            if n+":"==g:
                                
                                b= "Error: Misuse of label as variable in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
                
                                
                                sys.exit()
                              
                
                if xx!=True:
                    b= "Variable not defined in line "+str(counter)
                    
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    break;
                break;

            if x=='mul':

                flag=False

                if len(temp)!=4:
                    #print("Error")
                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                #print("0011000",end='')
                buffer += "0011000"
                    
            if x=='div':

                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                #print("0011100000",end='')
                buffer += "0011100000"
                
            
                    
            
            
                    
                
                
                
                
            
    
    
    
    
            if x=="rs":
                

                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                buffer += "01000"
                
                
            if x=="ls":
                
                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                buffer +="01001"
                
            if x=="xor":
                
                flag=False

                if len(temp)!=4:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                buffer +="0101000"
                
            if x=="or":
                
                flag=False

                if len(temp)!=4:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                buffer +="0101100"
                
            if x=="and":
                
                flag=False

                if len(temp)!=4:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                buffer +="0110000"
                
            if x=="not":
                
                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                buffer +="0110100000"
                
            if x=="cmp":
                
                flag=False

                if len(temp)!=3:
                    #print("Error")
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                buffer+="0111000000"
                
            if x=="jmp":
                flag=False
                
                if len(temp)!=2:
                    b= "Error: Wrong syntax in line "+str(counter)
                                
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
                
                                
                    sys.exit()

                tmpx=temp[1]+":"
                
                
                
                
                
                if len(temp)!=2 or tmpx not in label.keys():
                    
                    for g in vars.keys():
                        
                            #print("G:",g)
                            
                           
                            if temp[1]==g:
                                #print(temp[1])
                                #print("herree")
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
                
                                
                                sys.exit()
                    
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                    
                    
                    
                    #print("Error")
                    
                    
                if tmpx in label.keys():    
                    
                    
                    buffer +="01111000"
                    
                    '''print("vrp:",vrrpx)
                    print("tmpx:",xc[tmpx])
                    print("counter:",length)
                    print("line count:",jmpchk)'''
                    
                    #var1=(length-vrrpx)   # length=10, vrrpx=7, label[ympx]=5, 
                    #print(tmpx, label[tmpx])
                    var1=label[tmpx]-1
                    #print("var1:",var1)
                    
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break;
                    
            
            if x=="jlt":
                
                flag=False

                tmpx=temp[1]+":"
                
                
                
                
                
                if len(temp)!=2 or tmpx not in label.keys():
                    
                    for g in vars.keys():
                        
                            #print("G:",g)
                            
                           
                            if temp[1]==g:
                                #print(temp[1])
                                #print("herree")
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
                
                                
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                    
                    
                    
                    #print("Error")
                    
                    
                if tmpx in label.keys():    
                    
                    
                    buffer +="10000000"
                    
                    '''print("vrp:",vrrpx)
                    print("tmpx:",xc[tmpx])
                    print("counter:",length)
                    print("line count:",jmpchk)'''
                    
                    var1=label[tmpx]-1
                    #print("var1:",var1)
                    
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break;
                
                
                
                
            
            if x=="jgt":
                
                flag=False

                tmpx=temp[1]+":"
                
                
                
                
                
                if len(temp)!=2 or tmpx not in label.keys():
                    
                    for g in vars.keys():
                        
                            #print("G:",g)
                            
                           
                            if temp[1]==g:
                               # print(temp[1])
                               # print("herree")
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
                
                                
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                    
                    
                    
                    #print("Error")
                    
                    
                if tmpx in label.keys():    
                    
                    
                    buffer +="10001000"
                    
                    '''print("vrp:",vrrpx)
                    print("tmpx:",xc[tmpx])
                    print("counter:",length)
                    print("line count:",jmpchk)'''
                    
                    var1=label[tmpx]-1
                    #print("var1:",var1)
                    
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break;
                
                
                
                
                    
                    
            if x=="je":
                
                flag=False

                tmpx=temp[1]+":"
                
                
                
                
                
                if len(temp)!=2 or tmpx not in label.keys():
                    
                    for g in vars.keys():
                        
                            #print("G:",g)
                            
                           
                            if temp[1]==g:
                                #print(temp[1])
                                #print("herree")
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                o = open("output.txt", "w")
                                o.write(b)
    
                    
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                   
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                
                    
                    
                    
                    #print("Error")
                    
                    
                if tmpx in label.keys():    
                    
                    
                    buffer +="10010000"
                    
                    '''print("vrp:",vrrpx)
                    print("tmpx:",xc[tmpx])
                    print("counter:",length)
                    print("line count:",jmpchk)'''
                    
                    var1=label[tmpx]-1
                    #print("var1:",var1)
                    
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break;
                    
                    
                    
            if(flag):
                    b= "Error"
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    o = open("output.txt", "w")
                    o.write(b)
    
                    
                    sys.exit()
                    
                
                
            
                
            
            
                    
                
            
           
            
                
                
            
                
           
           
        
            #if x[0]=="$":
             #   print(bina(int(i[1:])))
            
                
                
                
    
        if buffer:
            
            if buffer=="1001100000000000":
                
                output.write(buffer)
            

            else:
                output.write(buffer + '\n')
                
    




output.close()


filex=open("output.txt","r")


for txt in filex.read():
    
    print(txt,end="")
print()
        
    


