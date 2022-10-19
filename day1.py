firstname = 'majesty'
integervalue = '28'
floatvalue = '28.3'
booleanvalue = False
print(firstname)
print(integervalue)
print(floatvalue)
print(booleanvalue)

word = 'are\'nt they what we expected them to be'
print(word)
word2 = "they're all good boys in general"
word3 = 'majesty is a good boy\nmajesty loves music'
print(word2)
print(word3)

lastname = 'james'
print(lastname + ' '+word2)
surname = 'george'
print(surname +' '+firstname)
print(surname +' '+firstname +' '+lastname)
price1 = 2800
price2 = 32000
price3 = 40000
sales_report = 'I sold a shirt for {}, three pairs of trousers for {} and a pair of trousers for {}'
print(sales_report.format(price1,price2,price3))
print(f'I sold a shirt for {price3},three pairs of trousers for {price1}and a pair of trousers for{price2}')
word1 = 'MAJESTY'
word2 = 'majesty'
word3 = 'majesty is a boy'
word4 = '       prosper'
print(word1.lower())
print(word2.upper())
print(word3.title())
print(word3.capitalize())
print(word3.split())
print(word4.strip())

