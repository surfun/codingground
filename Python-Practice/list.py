list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
print "3rd value in touple : ",tuple[2]
tuple[2] = 1000    # Invalid syntax with tuple
print "3rd value in list ",list[2]
list[2] = 1000     # Valid syntax with list