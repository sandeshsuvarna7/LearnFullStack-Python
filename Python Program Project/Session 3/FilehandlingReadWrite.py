try:
    for line in open('myfile.txt'):
        print(line)
    f = open('myfile.txt', 'a')
    for i in range(0,10):
        print(i)
        f.write('Program added lines.... ' +str(i) + "\n")
    f.close()
except err:
    print('Error' + err)
finally:
    print('Success')