def check_anagram(st1,st2):
    if(len(st1)!=len(st2)):
        return false
    d={}
    for(char ch in st1):
        d[ch]+=1
    for(ch in st2):
        d[ch]-=1
    if(len(d)==0):
        return true
    return false
st1="rat"
st2="tar"
print(check_anagram(st1,st2))