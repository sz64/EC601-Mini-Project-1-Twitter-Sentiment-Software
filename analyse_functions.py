ls=[
    ["Hamburger",12],
    ["Cheese",15],
    ["Cheese",18],
    ["Ice",18]
    ]

def simplify_data_list(ls):
    length=len(ls)
    newls=[]
    name=[]
    b=0
    for i in range(length):
        if ls[i][0] in name:
            b=b+1
            for j in range(len(newls)):
                if ls[i][0]==newls[j][0]:
                    newls[j].append(ls[i][1])
                
                
        else:
           name.append(ls[i][0])
           newls=newls+[[(ls[i][0])]]
           newls[i-b].append(ls[i][1])
           print(newls)

        
    return newls
def identify_simularity(a,b):
#if entities a,b are almost same thing like hamburger and burger, return true
    lengtha=len(a)
    lengthb=len(b)
    count1=0
    count2=0
    for x in a:
        if x in b:
            count1=count1+1
    for y in b:
        if y in a:
            count2=count2+1
    percent=float((count1+count2)/(lengtha+lengthb))
    if percent>0.8:
        return 1
    else:
        return 0
        

#cbb=simplify_data_list(ls)
#print(identify_simularity("Hello","hi"))


