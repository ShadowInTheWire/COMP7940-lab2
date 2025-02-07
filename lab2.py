import json
import requests

site="https://api.npoint.io/2b57052af2060e84dc86"
# Function to convert elements (except the first one) into numbers
def convert_number(elements):
    return [int(x) for x in elements[1:]]

# Function to replace all occurrences of a specified number in the list with another number
def replace_number(number_list, being_replace, to_replace):
    return [to_replace if x == being_replace else x for x in number_list]

# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']

# Debug
for i in text:
    print("parse " + str(i))

# Call the function convert_number
# Convert all elements (except the first one) into number and return it as a list
y = convert_number(text[0])
print("y")
print(y)

# Call the function replace_number
# Replace all number 1 by the number 10 in the function
z = replace_number(number_list=y, being_replace=1, to_replace=10)
print("z")
print(z)

# Calculate the sum of the numbers in the list
sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print("Total = " + str(sum))