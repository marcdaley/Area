#This program will compute the area of a circle and a triangle.

print 'Time to get this party started!'

option = raw_input('Enter C for Circle or T for Triangle: ')

if option == 'C':
  radius = float(raw_input("Please input the radius. "))
  area = 3.14159 * radius**2
  print 'The area of a circle is %s with a radius of %s' % (radius, area)
elif option == 'T':
  base = float(raw_input("Please input the triangle base. "))
  height = float(raw_input("Please input the triangle height. "))
  area = 0.5 * base * height
  print 'The area of a triangle is %s with a base of %s and a height of %s' % (base, height, area)
else:
  print 'We are unable to process your request. '
