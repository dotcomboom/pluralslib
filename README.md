# pluralslib
The purpose of pluralslib is to avoid embarassing situations like `1 apples` and `0 apple`

## Functions
`is(amount, base, plural, singular)` - Returns the amount and base word with either a plural or singular suffix. If `plural` is not set, `s` is used. If `singular` is not set, the base word is treated as the singular word, and is only changed if the amount warrants a plural word.

`is(number)` - returns string. "is" or "are" depending on amount

## Usage
`apples = 0`

`print('You have ' + plural(apples, 'apple'))` outputs `You have 0 apples.`

`apples = 1`

`print('You have ' + plural(apples, 'apple'))` outputs `You have 1 apple.`

Some words, like "library", have different suffixes for singular and plural versions. In this situation, you can do this:

`libraries = 0`

`print('There ' + is(libraries) + ' + plural(libraries, 'librar', 'ies', 'y'))` outputs `There are 0 libraries.`

Another function pluralslib offers shown in the above example is `is`. `is` reports "are" or "is" depending on the number.
