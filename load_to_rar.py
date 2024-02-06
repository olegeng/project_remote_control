s={'1':1, '2':2}
copy=dict(s)
s['1']=5
sum=s['1']+copy['1']
print(sum)