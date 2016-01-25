import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub('#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub('\D', "", phone) 
print "Phone Num : ", num
