#Python escape sequence
#\newline - backlash and newline ignored
#\\       - backslash
#\'       - single quote
#\"       - double quote
#\a       - ASCII bell
#\b       - ASCII backspace
#\f       - ASCII formfeed
#\n       - ASCII linefeed
#\r       - ASCII carriage return
#\t       - ASCII horizontal tab
#\v       - ASCII vertical tab
#\ooo     - Character with octal value ooo
#\xHH     - Character with headecimal value HH


a = 'Hi\nhow are you?'
print (a)
#b = "\helloooo\"
#print (b) -- throws error
c = '\\helloooo\\'
print (c)
d = 'isn\'t it beautiful!' 
print (d)
e = "he told like \"it should be done today\""
print (e)
f = "\a" # \a makes ringing bell alert sounds
print(f)

print (a + "\f" + c + "cf"+ "\b" + d + "\n" + e)

h = 10
print(h * 2)
print (h ** 2)
 
