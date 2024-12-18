
def count(string,element):
    result=0
    index_=0
    ifstatement=True
    data=''
    for index in range(len(string)):
        try:
            if len(element)==1:
                if string[index]==element:
                    result+=1
                ifstatement=False
            elif (element[0]*len(element)==element):
                if data==string[index:index+len(element)][len(element)-1]:
                    data=''
                elif (string[index:index+len(element)]==element):
                    result+=1
                    data=string[index:index+len(element)][len(element)-1]
                ifstatement=False
            else:
                index+=len(element)
                if (string[index_:index]==element):
                    result+=1
                index_+=1
                ifstatement=False
        except:
            break
    if (ifstatement):
        return 0
    else:
        return result
    
print(count('ksdjkfjkjsdlaajAjkmnKKaaa','ks'))
print('ksdjkfjkjsdlaajAjkmnKKaaa'.count('ks'))
        