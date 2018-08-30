from pluralslib import are, plural

libraries = 2
apples = 1
print('There ' + are(libraries) + ' ' + plural(libraries, 'librar', 'ies', 'y'))
print('You have ' + plural(libraries, 'apple'))

libraries = 1
apples = 2
print('There ' + are(libraries) + ' ' + plural(libraries, 'librar', 'ies', 'y'))
print('You have ' + plural(libraries, 'apple'))
