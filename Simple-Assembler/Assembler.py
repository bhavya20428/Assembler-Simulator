import sys

co="" #Input String

for line in sys.stdin:
    if line=="":
        break;
    co+=line
lst=[]
for i in co.splitlines():
    if(i):
        lst.append(i)



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
    

#Converts integer to 8 bit binary
def abcd(z):
    
    bnr=bin(z).replace('0b','')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr

#Instruction function -->to check next term after label definition
def instruction(character):
    instructions =['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
    if character not in instructions:
        return True

length=len(lst)  #Total number of lines in input
if length>256:
    b= "Error: commands out of supported max limit "
    print(b)    
    sys.exit()

if length<=0:
    b= "Error: no commands entered "
    print(b)    
    sys.exit()

vrrp=0 #Counts no of lines without var


for x in lst:
    if x[0:4]!="var ":        
        vrrp=vrrp+1
        
        
vrrp=vrrp-1 #Subtracting by 1 as to start linecount by 0

hlt=0 #Used to check for halt

label={} #Stores labelname and memory address
count=0  #Used in memory address of label



for x in lst:
    temp1=x.split(" ")
    if temp1[0]!=("var"):        
        count+=1
        
    if temp1[0]=='hlt':
        hlt=1
    
    if temp1[0]!='' and temp1[0][-1]==":":
        
        if len(temp1)>1:
            label.update({temp1[0]:count})
            if temp1[1]=="hlt":
                hlt=1
            
            

if hlt==0:
    b= "Error: hlt not present"
    print(b)   
    sys.exit()

counter=0 #Checks at what line of input we are
var_check=0 #Checks if any var statement is defined after non-var code

vars={} #Stores Varname and counter number
xc=dict() #Used to check for label errors

output = open("output.txt", "w")


for y in lst:

    y=y.replace('\t',' ')


    if y:

        temp=y.split()
        counter=counter+1

        buffer=str() #Stores the binary output of each line
           

        if temp[0]!="var":
                var_check=1

        if temp[0].startswith('$') or temp[0]==("R0") or temp[0]==("R1") or temp[0]==("R2") or temp[0]==("R3") or temp[0]==("R4") or temp[0]==("R5") or temp[0]==("R6"):
            b= "Error: Wrong syntax in line "+str(counter)
            print(b)                
            sys.exit()

        #Flags Statement
        if len(temp)==3:
            if temp[2]=="FLAGS" and temp[0]!="mov":
                b="Error: Illegal use of FLAGS reg in line "+str(counter)
                print(b)
                sys.exit() 
        

        for x in temp: 
            flag=True 
            #Halt statement
            if x=='hlt':                
                flag=False
                if counter==length:
                    buffer += "1001100000000000"
                
                if counter<length:
                    b= "Error: hlt not at end of the file instead at line "+str(counter)
                    print(b)                        
                    sys.exit()

            #Registers and Flags
            if x=="R0" or x=="R0\n":
                flag=False
                buffer += "000"                
                        
            if x=="R1" or x=="R1\n":
                flag=False                
                buffer += "001"                
                    
            if x=="R2" or x=="R2\n":
                flag=False          
                buffer += "010"

            if x=="R3" or x=="R3\n":
                flag=False             
                buffer += "011"
                    
            if x=="R4" or x=="R4\n":
                flag=False             
                buffer += "100"
                        
            if x=="R5" or x=="R5\n":
                flag=False             
                buffer += "101"
                    
            if x=="R6" or x=="R6\n":
                flag=False             
                buffer += "110"

            if x=="FLAGS" or x=="FLAGS\n":
                flag=False             
                buffer += "111"
                
            if x[0]=="R": 
                
                if x[1:].isnumeric():
                    if int(x[1:])<0 or int(x[1:])>6:
                        b= "Error: Wrong resistor name in line "+str(counter)
                        print(b)                    
                        sys.exit()

            #Immediate Value
            if x[0]=='$':
                flag=False              
                if int(x[1:])>=0 and int(x[1:])<=256:
                    buffer += abcd(int(x[1:]))                
                else:                    
                    b= "Error: Wrong immediate value in line "+str(counter)
                    print(b)
                    sys.exit()

            #Label
            if x[len(x)-1]==":":

                flag = False

                if len(temp)==1:
                    b= "Error: No label definition provided in line "+str(counter)
                    print(b)                   
                    sys.exit()

                if temp[1]==":":                    
                    b= "Error: Wrong label decleration in line "+str(counter)
                    print(b)                    
                    sys.exit()

                if(instruction(temp[1])):
                    b= "Error: Wrong instruction used in line "+str(counter)
                    print(b)
                    sys.exit()                
                
                    
                #Checking labelname
                for g in x[:-1]:
                    if g.isalnum()==True or g=="_" :
                        cont=1
                    else:                       
                        cont=0
                        break

                if cont==0:
                    b= "Error: Wrong label decleration in line "+str(counter)
                    print(b)
                    sys.exit()
                            
                if cont==1: 
                    if temp[0] not in xc.keys():    
                        l=temp[0]
                        xc.update({l:counter})

                    elif temp[0] in xc.keys():
                        b= "Error: cannot define a label with the same name multiple times at line "+str(counter)
                        print(b)
                        sys.exit()

                    temp=temp[1:]

            #Variable
            if x=='var':
                flag=False
                if var_check==1 or len(temp)!=2 :
                    b= "Error: Wrong variable declaration in line "+str(counter)
                    print(b)                    
                    sys.exit()
                    

                for g in temp[1]:
                    if g.isalnum()==True or g=="_" :
                        cont=1
                    else:                       
                        cont=0
                        break
                
                if cont==1:                
                    v=temp[1]
                    if v not in vars.keys():    
                        vars.update({v:counter})

                    elif v in vars.keys():
                        b= "Error: cannot define a variable with the same name multiple times at line "+str(counter)
                        print(b)
                        sys.exit()                    
                    

                elif cont==0:
                    b= "Error: Wrong variable declaration in line "+str(counter)
                    print(b)                    
                    sys.exit()

                break                  
            
            
            #Move statements
            if x=="mov":

                flag=False

                if len(temp)!=3:
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()

                elif temp[2][0]=="$":
                    buffer += "00010"                
            
                elif temp[2][0]!="R" and temp[2][0]!="F":
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                
                
                else:
                    buffer += "0001100000"
            
            #Load statement
            if x=='ld':
                flag=False
                if len(temp)!=3:
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()

                if(temp[1] not in ['R0','R1','R2','R3','R4','R5','R6']):
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()

                n=temp[2]   

                xx=False #to check for presence of variable

                for g in vars.keys():
                    if n == g:                        
                        xx=True                        
                        buffer += "00100"                                               
                        buffer += checker(temp[1])
                        var=vrrp+vars[g]
                        buffer += abcd(var)                       
                        break
                
                if xx!=True:
                    for g in label.keys():                       
                        if n+":"==g:                                
                            b= "Error: Misuse of label as variable in line "+str(counter)                                
                            print(b)                               
                            sys.exit()

                    b= "Variable not defined in line "+str(counter)                    
                    print(b)                    
                    sys.exit()
                    
                break              
                        
            #Store Statement
            if x=='st':
                flag=False

                if len(temp)!=3:
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()

                if(temp[1] not in ['R0','R1','R2','R3','R4','R5','R6']):
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                
                n=temp[2]

                xx=False

                for g in vars.keys():                                       
                    if n == g:                        
                        xx=True                        
                        buffer += "00101"
                        buffer += checker(temp[1])
                        var=vrrp+vars[g]
                        buffer += abcd(var)
                        break
                
                if xx!=True:
                    for g in label.keys():                         
                        if n+":"==g:                                
                            b= "Error: Misuse of label as variable in line "+str(counter)                                
                            print(b)                            
                            sys.exit()

                    b= "Variable not defined in line "+str(counter)                    
                    print(b)                                 
                    sys.exit()
                    
                break

            if x=="add":
                
                flag=False
                if len(temp)!=4:
                    b="Syntax Error in line "+str(counter)
                    print(b)                   
                    sys.exit()
                
                buffer += "0000000"

            if x=="sub":

                flag=False
                if len(temp)!=4:
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                    
                buffer += "0000100"


            if x=='mul':

                flag=False
                if len(temp)!=4:
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()                  
                
                buffer += "0011000"
                    
            if x=='div':

                flag=False

                if len(temp)!=3:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()

                buffer += "0011100000"

            if x=="rs":
                flag=False
                if len(temp)!=3:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()                
                buffer += "01000"                
                
            if x=="ls":
                
                flag=False

                if len(temp)!=3:
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                buffer +="01001"
                
            if x=="xor":
                
                flag=False

                if len(temp)!=4:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                    
                buffer +="0101000"
                
            if x=="or":
                
                flag=False

                if len(temp)!=4:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)                    
                    sys.exit()
                    
                buffer +="0101100"
                
            if x=="and":
                
                flag=False

                if len(temp)!=4:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()
                    
                buffer +="0110000"
                
            if x=="not":
                
                flag=False

                if len(temp)!=3:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()
                    
                buffer +="0110100000"
                
            if x=="cmp":
                
                flag=False

                if len(temp)!=3:                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()
                    
                buffer+="0111000000"
                
            if x=="jmp":            #hehe
                flag=False
                
                if len(temp)!=2:
                    b= "Error: Wrong syntax in line "+str(counter)                                
                    print(b)
                    sys.exit()

                tmpx=temp[1]+":"
                
                if tmpx not in label.keys():
                    
                    for g in vars.keys(): 
                            if temp[1]==g:                               
                                b= "Error: Misuse of variable as label in line "+str(counter)                                
                                print(b)
                                sys.exit()                    
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    sys.exit()

                if tmpx in label.keys(): 
                    buffer +="01111000"                   
                    
                    var1=label[tmpx]-1;                   
                    
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break
                    
            
            if x=="jlt":

                flag=False

                if len(temp)!=2:
                    b= "Error: Wrong syntax in line "+str(counter)                                
                    print(b)
                    sys.exit()                
                

                tmpx=temp[1]+":"
                
                if tmpx not in label.keys():
                    
                    for g in vars.keys():
                            if temp[1]==g:
                               
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    sys.exit()

                if tmpx in label.keys():  
                    buffer +="10000000"
                    var1=label[tmpx]-1
                                       
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break
            
            if x=="jgt":
                flag=False

                if len(temp)!=2:
                    b= "Error: Wrong syntax in line "+str(counter)                                
                    print(b)
                    sys.exit()                
                

                tmpx=temp[1]+":"
                
                if tmpx not in label.keys():
                    
                    for g in vars.keys():
                            if temp[1]==g:
                               
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    sys.exit()

                if tmpx in label.keys():  
                    buffer +="10001000"
                    var1=label[tmpx]-1
                                       
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break                
                

            if x=="je":

                flag=False

                if len(temp)!=2:
                    b= "Error: Wrong syntax in line "+str(counter)                                
                    print(b)
                    sys.exit()                
                

                tmpx=temp[1]+":"
                
                if tmpx not in label.keys():
                    
                    for g in vars.keys():
                            if temp[1]==g:
                               
                                b= "Error: Misuse of variable as label in line "+str(counter)
                                
                                print(b)
                                sys.exit()
                    
                    b= "Error: label not defined in line "+str(counter)
                    
                    print(b)
                    sys.exit()

                if tmpx in label.keys():  
                    buffer +="10010000"
                    var1=label[tmpx]-1
                                       
                    buffer +=abcd(var1)
                    buffer +="\n"
                    output.write(buffer)
                    buffer=""
                    break 

            if(flag):                    
                    b= "Syntax Error in line "+str(counter)
                    print(b)
                    sys.exit()
                    

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
        
    


