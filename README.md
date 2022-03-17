# Pswgen
Simple utility for generating random passwords

## Requirements

Recommended python 3.7 or above

## Usage

`./pswgen.py -n <number> -m <mask> -c <charset>`

All options except `-m` are optional.
<br><br>
  -n - set the number of output passwords in stdout (by default that number is 1)<br>
  -m - set the mask of generated passwords<br>
  -c - set custom user charset for generated passwords<br>
<br><br>
Mask example:
<br><br>
  `Prefix_?u?u?u?u_Postfix`
<br><br>
?u means insert a character from users charset.<br>
For example:
<br><br>
  `./pswgen.py -m Prefix_?u?u?u?u_Postfix -c abcdef`
<br><br>
Result:
<br><br>
`Prefix_bbac_Postfix`
<br><br>
Mask value can considers escape characters (with "\". In that cases all mask value should be in quotes)
<br><br>
Builtin charsets:
<br><br>
?d - digits from 0 to 9<br>
?h - hex digits from 0 to f<br>
?H - hex digits in uppercase<br>
?l - latin letters in lowercase<br>
?L - latin letters in uppercase<br>
?s - special characters (non letters but printable characters)<br>
?c - cyrillic letters in lowercase<br>
?C - cyrillic letters in uppercase<br>
?a - all characters except cyrillic letters<br>
?A - all characters (with cyrillic letters)<br>
<br><br>
## Example
`./pswgen.py -n 10 -m ?a?a?a?a?a?a?a?u -c abcdef`
<br><br>
That will generate 10 random passwords in stdout.
