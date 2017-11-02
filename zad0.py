import re
f = open('D:\eg.txt')
line = f.readline()
while line:
    result = re.findall(r'\d{2}-\d{2}-\d{4}'+'', line)
    z=result
    line = f.readline()
    print(result)
    b = open( 'D:\egr.txt', 'w')
    for index in z:
        b.write(index)

    f.close()

f.close()
