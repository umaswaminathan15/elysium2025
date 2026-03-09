from a2controller import *
while True:
    rno = int(input("Enter Roll No.:"))
    sname = input("Enter Student Name:")
    m1 = float(input("Enter Mark 1:"))
    m2 = float(input("Enter Mark 2:"))
    if createData({"rno":rno, "sname":sname, "m1":m1, "m2":m2}):
        print('Inserted data')
    if input("Do you want to add another data [y]es/[N]o:").upper() != 'Y':
        break

'''
Enter Roll No.:1002
Enter Student Name:x3
Enter Mark 1:43
Enter Mark 2:36.5
Inserted data
Do you want to add another data [y]es/[N]o:Y

Enter Roll No.:1003
Enter Student Name:x1
Enter Mark 1:54.5
Enter Mark 2:52
Inserted data
Do you want to add another data [y]es/[N]o:Y

Enter Roll No.:1004
Enter Student Name:x2
Enter Mark 1:98
Enter Mark 2:20
Inserted data
Do you want to add another data [y]es/[N]o:Y

Enter Roll No.:1005
Enter Student Name:x4
Enter Mark 1:47.5
Enter Mark 2:54.5
Inserted data
Do you want to add another data [y]es/[N]o:N
'''