import pyql
import ystockquote

print('Using pyql')
print('----------------------------------')

#list = ['FFIV', 'MSFT', 'GOOG']
#print pyql.lookup(list)
list = ['GOOG']
json = pyql.lookup(list)

print json

print('Using ystockquote')
print('----------------------------------')
print ystockquote.get_all('GOOG')