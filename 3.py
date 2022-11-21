def checkEqual(S):
    for i in range(len(S)):
        if (S[i] != '1' and S[i] != '0' and S[i] != '2' and S[i] != '6' and S[i] != '5'
                        and S[i] != '8' and S[i] != '9'):
            return "No";
    return "Yes" 
n=100
arr=[]
for i in range(n):
    if (checkEqual(str(i)) == 'Yes'):
        arr.append(i)
print(arr[8])
