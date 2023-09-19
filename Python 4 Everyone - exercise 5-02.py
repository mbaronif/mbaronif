number = 0
total = 0.0

while True:
    StringVal = input('Enter a number: ')
    if StringVal == 'Done':
        break
    try:
        FloatVal = float(StringVal)      
    except:
        print("Invalid input")
        continue  
   
    if number == 0:
        largest = FloatVal
        smallest = FloatVal
    elif FloatVal > largest:
        largest = FloatVal
    elif FloatVal < smallest:
        smallest = FloatVal
    
    total = total + FloatVal
    number = number + 1

print (total, number, total/number, largest, smallest)
