def are(amount):
  if amount == 1:
    return 'is'
  else:
    return 'are'
def plural(amount, base, plural='s', singular=''):
  if amount == 1:
    return str(amount) + ' ' + base + singular
  else:
    return str(amount) + ' ' + base + plural
