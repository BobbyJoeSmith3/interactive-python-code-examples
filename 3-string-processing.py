#############################################/
#   first example of string processing
#############################################/

### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3]
print len(s1)
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38





#############################################/
#   second example of string processing
#   money converter
#############################################/

# convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = int(100 * (val - dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"

# Tests
print convert(11.23)
print convert(11.20)
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)
