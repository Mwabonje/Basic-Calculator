num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))

print("Choose calculation: \n", "Add \n", "Subtract \n", "Multiply \n","divide \n")

calc=input()
if calc=='Add':
    ans=num1 + num2
elif calc=='subtract':
    ans=num1-num2
elif calc=='Multiply':
    ans=num1 * num2
elif calc=='divide':
    ans=num1 / num2

print(ans)
