f = open('configuration.txt', 'r')
content = f.read()
print(content)
print('-------------------------')
print(f.closed)
f.close()
print(f.closed)