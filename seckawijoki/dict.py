d={'Michael':95, 'Bob':75,'Tracy':85}
print d
print d['Michael']

d['Adam']=67
print d['Adam']

d['Jack']=90
print d['Jack']
d['Jack']=88
print d['Jack']

# print d['Thomas']
print 'Thomas' in d
print d.get('Thomas')
print d.get('Thomas',-1)

print d.pop('Bob')
print d

# key=[1,2,3]
# d[key]='a list'
