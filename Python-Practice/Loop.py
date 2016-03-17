count=0
while(count<9):
    print "The count is :",count
    count = count+1
else :
    print "The count is now exceding above 8"

print "For Loop Handson"

for some_var in "Python" :
    print "Current Letter :",some_var

fruits = ['banana', 'mengo','apple','pinapple']

for fruit in fruits :
    print "Current Fruit :",fruit

print "Range :",range(len(fruits))

for index in range(len(fruits)) :
    print "Current fruit using index:",fruits[index]
print "Good Bye"