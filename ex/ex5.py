name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.5400000000102
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches( %d cm)  tall." % (height, height * 2.5400000000102)
print "He's %d pounds( %d kg) heavy." % (weight, weight * 0.4536)
print "Actually that;s not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teech are usually %s depending on th coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
