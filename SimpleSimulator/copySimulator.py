import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



array=[] #stores memory

yaxis=[] #stores pc when accessed
xaxis=[] #storing the cycle no.




def memory(pc):
    global array

    return array[pc]

reg={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0} #stores the value of registers

def rf(R):  #Register File
    global reg
    return reg[R]

def GNR(code): #Give Register Name
    nameR={"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}
    return nameR[code]

def checkResult(result):  #For overloading in add,div,sub
    global reg
    if result<0:
        reg["FLAGS"]=8
        return 0
    elif result>256:
        reg["FLAGS"]=8
        return 255
    else:
        reg["FLAGS"]=0
        return result

def cto16bin(z):   #Converting to 16bin
    bnr=bin(z).replace('0b','')    
  
    x = bnr[::-1]
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr

def cto8bin(z):  #Converting to 8bin
    bnr=bin(z).replace('0b','')    
  
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


def ctoint(z):  #Converting to INT

    value=z[::-1]
    num=0
    
    for i in range(0,len(z)):
        
        if value[i]=="1":            
            num+=int(math.pow(2,i))
    return num


#main function

nextpc=0 #next value of Program Counter
haltValue=True #halt variable
cycleno=0 #cycle no

    
def main():
    global yaxis
    global array
    global haltValue
    global nextpc
    global xaxis
    global cycleno
  
    array=sys.stdin.read().splitlines()
    for i in range(len(array),256):
        array.append("0000000000000000")
    

    pc=0 #Program counter


    while(haltValue and pc<len(array)):
        
        EE(pc)

        yaxis.append(pc)
        xaxis.append(cycleno)

        BinPC= cto8bin(pc)

        BinR0= cto16bin(reg["R0"])
        BinR1= cto16bin(reg["R1"])
        BinR2= cto16bin(reg["R2"])
        BinR3= cto16bin(reg["R3"])
        BinR4= cto16bin(reg["R4"])
        BinR5= cto16bin(reg["R5"])
        BinR6= cto16bin(reg["R6"])
        BinFLAGS= cto16bin(reg["FLAGS"])

        print(BinPC+" "+BinR0+" "+BinR1+" "+BinR2+" "+BinR3+" "+BinR4+" "+BinR5+" "+BinR6+" "+BinFLAGS)
        
        pc=nextpc
        cycleno+=1
        
        

    

    for k in array:
        print(k)
   
    
        
   
def EE(pc):

    global nextpc
    global haltValue
    global variable
    global reg
    global vararr
    global xaxis
    global yaxis
    global cycleno

    inst=memory(pc)                           #instruction to be executed
    nextpc=pc+1                               #nextpc

    
    #halt    
    if inst[:5]=="10011":
        haltValue=False

    #Add
    if inst[:5]=="00000":

        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) + rf(o2)
        reg[register]=checkResult(result)
    
    #Subtract
    if inst[:5]=="00001":

        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) - rf(o2)
        reg[register]=checkResult(result)

    #Move Immediate
    if inst[:5]=="00010":

        register=GNR(inst[5:8])
        imm=ctoint(inst[8:16])
        
        reg[register]=imm    #wrong
        
        reg["FLAGS"]=0
    
    #Move Register
    if inst[:5]=="00011":

        register=GNR(inst[10:13])
        
        o1=GNR(inst[13:16])
        
        reg[register]=rf(o1)
        reg["FLAGS"]=0
        
    #Load
    if inst[:5]=="00100":

        register=GNR(inst[5:8])
        arrindex=ctoint(inst[8:16])
        value=ctoint(array[arrindex])
        reg[register]=value
        reg["FLAGS"]=0
        yaxis.append(arrindex)
        xaxis.append(cycleno)
        
    #Store
    if inst[:5]=="00101":

        register=GNR(inst[5:8])
        arrindex=ctoint(inst[8:16])
        array[arrindex]=cto16bin(rf(register))
        reg["FLAGS"]=0
        yaxis.append(arrindex)
        xaxis.append(cycleno)

    #Multiply
    if inst[:5]=="00110":

        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) * rf(o2)
        reg[register]=checkResult(result)

    #Divide
    if inst[:5]=="00111":

        o1=rf(GNR(inst[10:13]))
        o2=rf(GNR(inst[13:16]))
        reg["R0"]=o1/o2
        reg["R1"]=o1%o2
        reg["FLAGS"]=0
    
    #RightShift
    if inst[:5]=="01000":

        register=GNR(inst[5:8])
        imm=ctoint(inst[8:16])
        result=reg[register]>>imm
        result=cto16bin(result)
        convertedResult=result[:8]
        reg[register]=ctoint(convertedResult)
        reg["FLAGS"]=0

    #LeftShift
    if inst[:5]=="01001":

        register=GNR(inst[5:8])
        imm=ctoint(inst[8:16])
        result=reg[register]<<imm
        result=cto16bin(result)
        convertedResult=result[-8:]
        reg[register]=ctoint(convertedResult)
        reg["FLAGS"]=0

    #ExclusiveOr
    if inst[:5]=="01010":
        
        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) ^ rf(o2)
        reg[register]=result
        reg["FLAGS"]=0

    #Or
    if inst[:5]=="01011":

        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) | rf(o2)
        reg[register]=result
        reg["FLAGS"]=0

    #And
    if inst[:5]=="01100":

        register=GNR(inst[7:10])
        o1=GNR(inst[10:13])
        o2=GNR(inst[13:16])
        result = rf(o1) & rf(o2)
        reg[register]=result
        reg["FLAGS"]=0

    #Invert
    if inst[:5]=="01101":

        register=GNR(inst[10:13])
        o1 = str(inst[13:16])
        result = ""
        for i in o1:
            if i=="0":
                result+='1'
            else:
                result+='0'
        result=int(result)
        reg[register]=ctoint(result)
        reg["FLAGS"]=0

    #Compare    
    if inst[:5]=="01110":

        o1=rf(GNR(inst[10:13]))
        
        o2=rf(GNR(inst[13:16]))
        
        

        if o1==o2:
            reg["FLAGS"]=1

        elif o1>o2:
            reg["FLAGS"]=2
        else:
            reg["FLAGS"]=4

    #Unconditional Jump
    if inst[:5]=="01111":

        nextpc=ctoint(inst[8:16])
        reg["FLAGS"]=0

    #Jump if less than
    if inst[:5]=="10000":
        
        flagval=reg["FLAGS"]
        if flagval==4:
            nextpc=ctoint(inst[8:16])
        reg["FLAGS"]=0

    #Jump if  than greater than
    if inst[:5]=="10001":
        
        flagval=reg["FLAGS"]
        if flagval==2:
            nextpc=ctoint(inst[8:16])
        reg["FLAGS"]=0

    #Jump if equal
    if inst[:5]=="10010":
        
        flagval=reg["FLAGS"]
        if flagval==1:
            nextpc=ctoint(inst[8:16])
        reg["FLAGS"]=0

main()

plt.scatter(xaxis,yaxis,c ="blue")
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.title("Memory Accesses v/s Cycles")
plt.xlabel("Cycle")
plt.ylabel("Address")
plt.savefig("graph.png")
plt.show()














    
        
        
        

        
        
        




