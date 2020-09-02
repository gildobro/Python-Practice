temps = [221, 234, 340, -9999, 230]

'''
#conditional list with if/else (order matters)
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)


#conditional list with an if
new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)


#list comprehension way
new_temps = [temp / 10 for temp in temps]
print(new_temps)

#longer way
for temp in temps:
   new_temps.append(temp / 10)


print(new_temps)
'''