counter = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in counter:
	print "This is count %d" % number

# ditto
for fruit in fruits:
	print "Here's the next fruit: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0-5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)

# now we can print them out, too
for i in elements:
	print "Next element is %d" % i

