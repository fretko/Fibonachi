n=int(input())
k=int(input())
spisok="m"
krug=1
spisok=spisok.replace('m','S')
while krug!=n:
    krug+=1
    spisok=spisok.replace("m", '%temp%')
    spisok=spisok.replace('S', 'S'+'m'*k)
    spisok=spisok.replace('%temp%','S')
print(len(spisok))
