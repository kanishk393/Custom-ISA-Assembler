
Reg_Binary={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
opcodeA={'add':"10000",'sub': '10001','mul': '10110','xor':'11010' ,'or':'11011','and': '11100'}
opcodeB={'mov': '10010','ls':'11001','rs': '11000'}
opcodeC={'mov':'10011','div':'10111','not':'11101','cmp':'11110'}
opcodeD={'ld':'10100','st':'10101'}
opcodeE={'jmp':'11111','jlt': "01100", 'jgt':"01101",'je':'01111'}
opcodeF={'hlt': '01010'}

def d2b(n):
    rem=[]#Empty list
    while n!=0:
        a=n//2#n gets divided by 2 
        b=n%2#remainder
        rem.append(b)#remainder appended to list
        n=a
        
    length=8-len(rem)    
    while(length>0):
        rem.append(0)
        length=length-1    

    rem.reverse() #list reversed to get the binary number
    a=""
    for i in rem:
        a+=str(i)#list converted to string
    return a    

lst0=[]
# data = sys.stdin.readlines()
# for line in data:
#     w = line.split()
#     lst0.append(w)
with open("assembly.txt", "r+") as file:
    data = file.readlines()
    for line in data:
        w = line.split()
        lst0.append(w)
      
      
lst=[]        
for i in lst0:
    if len(i)!=0:
        lst.append(i)

vardict={}

for i in range((len(lst))):
    if 'var' in lst[i]:
        vardict[lst[i][-1]]=d2b(i+1)

labelstore={}
new=''
for i in range(len(lst)):
        if "label" in lst[i][0]:
            new=lst[i][0].replace(':','',-1)
            labelstore[new]=d2b(i+1)
            lst[i].remove(lst[i][0])
       

def printlist(list):
    str=""
    lst=[]
    for i in list:
        str=str+i
    lst.append(str)
    for i in lst:
        print(i)
    with open("output.txt", "a") as file:
        for i in lst:
            file.write("%s\n" % i)    
          
error_list=[]
def funcerror(error_list):
    

    def errorgen_typo(lst,error_list):
        dict={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101",
        "R6":"110","FLAGS":"111",'add':"10000",'sub': '10001','mul': '10110',
        'xor':'11010' ,'or':'11011','and': '11100','mov': '10010','ls':'11001','rs': '11000',
        'mov':'10011','div':'10111','not':'11101','cmp':'11110','ld':'10100','st':'10101',
        'jmp':'11111','jlt': "01100", 'jgt':"01101",'je':'01111','hlt': '01010','label':'','var':''}
        
        for i in range(len(lst)):
            if len(lst[i])<4:
                for j in range(len(lst[i])-1):
                    if lst[i][j] in dict:
                        pass
                    
                    else:
                        error_list.append(f'Typo error in line {i+1}:{lst[i][j]}')
            else:
                for j in range(len(lst[i])):
                    if lst[i][j] in dict:
                        pass
                    
                    else:
                        error_list.append(f'Typo error in line {i+1}:{lst[i][j]}')

    errorgen_typo(lst,error_list)

    def hlt_error(error_list):
        str=[]
        for i in lst:
            for j in i:
                str.append(j)  
        if 'hlt' not in str:
            error_list.append(f'Error:hlt not present in line {len(lst0)+1}')
    hlt_error(error_list)        
            

    def var_undefined(lst,opcodeD,opcodeE,vardict,error_list):
        for i in range(len(lst)):
            if lst[i][0] in opcodeD and lst[i][-1] not in vardict:
                if 'label' in lst[i][-1]:
                    error_list.append(f"misuse of variable and label and vice-versa in line {i+1}")
                else:    
                    error_list.append(f"Variable undefined in line {i+1}")

            if lst[i][0] in opcodeE and lst[i][-1] not in vardict:
                if 'label' in lst[i][-1]:
                    error_list.append(f"misuse of variable and label and vice-versa in line {i+1}")
                else:    
                    error_list.append(f"Variable undefined in line {i+1}")

    var_undefined(lst,opcodeD,opcodeE,vardict,error_list)  

    def flags_error(lst,error_list):
        for i in range(len(lst)):
                if lst[i][0]!='mov' and lst[i][-1]=='FLAGS':
                    error_list.append(f"Illegal use of flags in line {i+1}")

    flags_error(lst,error_list)  

    def immediate_error(lst,error_list):
        for i in range(len(lst)):
            for j in lst[i]:
                if '$' in j:
                    j=j.replace('$','')
                    if int(j)<0 or int(j)>255:
                        error_list.append(f'Invalid immediate in line {i+1}')
                    
    immediate_error(lst,error_list) 
    
funcerror(error_list)     
    
def TypeA(opcodeA,lst,Reg_Binary):
    list=[]
    unused="00"
    for i in lst:
        if i in opcodeA:
            list.append(opcodeA[i])
            list.append(unused)    
        if i in Reg_Binary:
            list.append(Reg_Binary[i])
    printlist(list)
    
def TypeB(opcodeB,lst,Reg_Binary):
    list=[]
    for i in lst:
        if i in opcodeB:
            list.append(opcodeB[i])
            
        if i in Reg_Binary:
            list.append(Reg_Binary[i])

        if i in labelstore:
            list.append(labelstore[i])      

    immediatelist=[]
    for i in lst[2]:
        immediatelist.append(i)
    str=""
    for i in range(1,len(immediatelist)):
        str=str+immediatelist[i]
    list.append(d2b(int(str)))
    printlist(list) 

def TypeC(opcodeC,lst,Reg_Binary):
    list=[]
    unused="00000"
    for i in lst:
        if i in opcodeC:
            list.append(opcodeC[i])
            list.append(unused)    
        if i in Reg_Binary:
            list.append(Reg_Binary[i])

           
    printlist(list) 

def TypeD(opcodeD,lst,Reg_Binary):
    list=[]
    for i in lst:
        if i in opcodeD:
            list.append(opcodeD[i])
        if i in Reg_Binary:
            list.append(Reg_Binary[i])
        if i in vardict:
            list.append(vardict[i])

        if i in labelstore:
            list.append(labelstore[i])         
    printlist(list) 
 

def TypeE(opcodeE,lst):
    list=[]
    for i in lst:
        if i in opcodeE:
            list.append(opcodeE[i])
            list.append('000')
        if i in vardict:
            list.append(vardict[i])  

        if i in labelstore:
            list.append(labelstore[i])
              
    printlist(list)    
        

def TypeF(opcodeF,lst):
    list=[]
    for i in lst:
        if i in opcodeF:
            list.append(opcodeF[i])
            list.append('00000000000') 
    printlist(list)       


def main():
           
    for i in range(len(lst)):   
        if lst[i][0] in opcodeA:
            TypeA(opcodeA,lst[i],Reg_Binary) 

        elif lst[i][0] in opcodeB and lst[i][2] not in Reg_Binary:
            TypeB(opcodeB,lst[i],Reg_Binary)

        elif lst[i][0] in opcodeC and lst[i][2] in Reg_Binary:
            TypeC(opcodeC,lst[i],Reg_Binary)

        elif lst[i][0] in opcodeD:
            TypeD(opcodeD,lst[i],Reg_Binary)

        elif lst[i][0] in opcodeE:
            TypeE(opcodeE,lst[i])

        elif lst[i][0] in opcodeF:
            TypeF(opcodeF,lst[i])
                                   
if (len(error_list))==0:
    main()
else:
    with open("output.txt", "a") as file:
        for i in error_list:
            file.write("%s\n" % i)
            print(i)
    exit()    
                  
              

