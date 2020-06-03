import requests
HTML=requests.get("https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8C%80%EB%AC%B8")
html=HTML.text
L=len(html)
ListC=list()
ListT=list()
for i in range(L):
    if html[i]=="<" and html[i+1]!="/":
        ListC.append(i)
        j=i
        while True:
            j+=1
            if html[j]==" " or html[j]==">":
                ListT.append(html[i+1:j])
                break
        
    elif html[i]=="<" and html[i+1]=="/":
        j=i
        while True:
            j+=1
            if html[j]==">":
                break
        k=len(ListT)
        while True:
            if k==0:
                break
            k-=1
            if html[i+2:j+1]==ListT[k]:
                ListC.pop(k)
                break
for i in ListC:
    j=i
    while True:
        j+=1
        if html[j]==">":
            break
    print(html[i:j+1])

