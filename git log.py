import os
from datetime import date
log = os.popen("git log --oneline --all --graph").read()
reflog = os.popen("git reflog --all").read()
c = input("log or reflog:")
if c =='log' or  c == 'l':
    with open("log.txt", 'w') as file:
        file.write(str(date.today()))
        file.write(log)
        print('done')
elif c == 'reflog' or c == 'r':
    with open('reflog.txt', 'w') as file2:
        file2.write(str(date.today()))
        file2.write("--------------")
        file2.write(reflog)
        print('done')
else:
    print('wrong')