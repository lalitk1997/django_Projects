# Dict
mydict = {'key1':'value1', 'key2':'value2'}
print(mydict['key2'])

mydict1 = {'key':123, 'key2':'value2', 'key3':{'123':[1,2,'grabMe']}}
print(mydict1['key3']['123'][2].upper())

#re-assign dict items
mydict2 = {'lunch':'pizza', 'break-fast':'eggs'}
print(mydict2)
mydict2['lunch'] = 'burger'
mydict2['break-fast'] = 'pasta'
print(mydict2)
print(mydict2['lunch'])
print(mydict2['break-fast'])
