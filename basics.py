#R2:24
''' how to remove the first character of a string, the last character of a string.
 '''

name = 'Mark'
first_letter = name[0]
last_letter = name[-1]
##print(name[-1:])
##print(name[:1])

#R:25
# check if the value is decimal, ist or string
a = 2.0 - 1.0
b = 1 + 9
c = '44'
#print(isinstance(a,str))
#print(isinstance(b,int))
#print(isinstance(c,str))

#R:26
#Create a function that prints the value
def val(val):
  print('the input value is:',val)
val(3*1000*1000)

#E2:1
#CREATE A PROGRAM THAT CONVERTS THE DIMENSIONS OF A LETTER SIZE(8.5X11 INCH) TO MILIMETERS
def MIL_PER_IN():
  return 25.4
def convert_inches_to_milimeters(w,h):
  widht = w * MIL_PER_IN()
  height = h * MIL_PER_IN()
  return 'The width in mlm is:' + str(widht) + ' the height in mlm is:' +str(height)

#print(convert_inches_to_milimeters(8.5,11))

#E2:2
number = input('Pease enter a number?')
print(int(number) **2,int(number)**4)