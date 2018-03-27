'''Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.'''

#Read comma separated list of numbers
a=input('Please enter a comma separated list of numbers : ');

#split the input from comma
numberList=a.split(',');

print('The list of entered number is : ');

#Print each number in List
for i in numberList:
    print(i);