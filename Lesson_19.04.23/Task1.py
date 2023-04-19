s = 'Hi my friend yyp\n Foo ouyy'

def my_split(s):
    A = [0]
    for i in range(1, len(s)-1):
        if s[i].isalpha() != s[i-1].isalpha():
            A.append(i)
    A.append(len(s))
    B = []
    for i in range(1,len(A)):
        B.append(s[A[i-1]:A[i]])
    return B
def my_repl(s):
    A = my_split(s)
    for i in range(len(A)):
        if A[i][0].isalpha():
            A[i] = A[i][::-1]
    return ''.join(A)

print(my_repl(s))
