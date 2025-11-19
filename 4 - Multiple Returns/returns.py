def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

#1 Return Type - None -> "No Value"
#Meaning: Absense of value, not set, not found
#Use for: Missing Data, search failures, optional parameters
result = None
print(result is None) #True - identity check
print(result == None) #True - equality check
print(not result) #True - falsy check

#2 Return Type - False = Boolean False
#Meaning: Explicit false condition, validation failure, negative result
#Use for: Validation result, boolean operations, success/failure status
result1 = False
print(result1 is False) #True - identity check
print(not result1) #True - boolean negation
print(result1 == 0) #True - falsy check

#3 Return Zero - A Valid Number
result2 = 0
print(result2 == 00) #True - numeric equality
print(not result2) #True - falsy in boolean context
print(result2 is None) #False - different objects
print(result2 is False) #False - different types
#Multiple Returns- python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter #Turns into a tuple
a = calculate_room(10, 5)
print(a)
print(type(a))

print(type((42))) #int
print(type((42,))) #tuple
no_parentheses = 1,2,3
print(type(no_parentheses)) #tuple

#Unpacking tuple
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}, Perimeter: {perimeter_result}")

#Build a function that returns multiple grades
def analyze_grades(grades):
    # if not grades:
    #     return 0, 0, 0, False
    # average = sum(grades)/len(grades)
    # highest = max(grades)
    # lowest = min(grades)
    # if average > 60:
    #     passed = True
    # else:
    #     passed = False
    # return average, highest, lowest, passed
    
    #Gemici Way
    if not grades:
        return 0,0,0,False
    average = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 60
    return average, highest, lowest, passed
print(analyze_grades([85, 92, 78, 90])) #[86.25, 92, 78, True]
print(analyze_grades([])) #[0, 0, 0, False]
print(analyze_grades([80, 80, 80])) #[80.0, 80, 80, True]