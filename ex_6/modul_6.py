# with open('text.txt', 'w') as fd:
#     data = fd.write('Hello')
#     print(data)


with open('text.bin', 'wb') as fd:
    data = fd.write(b'Hello')
    print(data)
