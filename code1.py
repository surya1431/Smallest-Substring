def maxlen(s):
    n=len(s)
    if n<2: return n
    
    len1=set(s)  
    len2=len(len1)
    
    count1=n+1
 
    a={}
    start=0; cnt=1
    a[s[start]]=1
    while cnt<n:
 
        if s[cnt] in a: a[s[cnt]]+=1
 
        else: a[s[cnt]]=1
 
        if len(a)==len2:
 
            while start<cnt and a[s[start]]>1:
                a[s[start]]-=1
                start+=1
            if count1>cnt+1-start: count1=cnt+1-start
        cnt+=1
 
    print(count1)
 
    
s=str(input())
maxlen(s)
