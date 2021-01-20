from numpy import load

data = load('traces-class.npz')
lst = data.files
for item in lst:
    #print(item)
    print(data[item][1])