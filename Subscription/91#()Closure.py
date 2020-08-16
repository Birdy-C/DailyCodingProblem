'''
This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
'''
'''
At a first glance, it seems like the snippet should print out from 0 to 9. But actually, it prints 9 10 times.

The problem is that the functions have closure and have access to the non-local variable i. We instead want the value of i when the functions are declared.

In order to solve this issue, we should capture the value i when the funcionts are declared. This would make i a local variable inside the anonymous functions.
'''
functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())
