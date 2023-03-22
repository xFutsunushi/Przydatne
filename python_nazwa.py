# Skrypt lswiezak task D_DZS-9750
import sys
import hashlib


def about():
    print('\n')
    print("**************************")
    print("Skrypt lswiezak z taska D_DZS-9750")
    print("**************************")
    print("\n")


def print_file():
    f = open('/home/lswiezak/python/baza.txt', 'r')
    print('\n')
    print("**************************")
    print(f.read())
    print("**************************")
    print("\n")



def write():
    with open('/home/lswiezak/python/baza.txt', 'r') as fr:
        for count, line in enumerate(fr):
            pass
        print('Total Lines', count + 1)

    with open('/home/lswiezak/python/baza.txt', "r+") as fr:
        lines = fr.readlines()
        for line in lines:
            Num, A = line.split(". ")
            maksim = int(max(Num))
        #print(maksim)

    fr = open('/home/lswiezak/python/baza.txt', 'a')
    x,y,z = input("Podaje dane w formacie Imię Nazwisko IP: \n").split(' ')
    fr.write('\n')
    fr.writelines("{}. {} {} {}".format(maksim + 1, x,y,z))


def delete_user():
    toWrite = ""
    with open('/home/lswiezak/python/baza.txt', "r") as fr:
        lines = fr.readlines()
        #print(lines)
        num_to_del = input("Line to del? \n")
        for line in lines:
            Num, A = line.split(". ")
            if not Num == num_to_del:
                toWrite += line
    with open('/home/lswiezak/python/baza.txt', "w") as fw:
        fw.write(toWrite)


def create_md5():
    file_name = '/home/lswiezak/python/baza.txt'
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    with open('/home/lswiezak/python/baza.sum', 'w') as fw:
        fw.write(hash_md5.hexdigest())
    print("MD5 zapisane do baza.sum", hash_md5.hexdigest())

def check_md5():
    file_name = '/home/lswiezak/python/baza.txt'

    with open('/home/lswiezak/python/baza.sum', 'r') as f:
        original_md5 = f.read()

    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_returned = hashlib.md5(data).hexdigest()
        print(md5_returned)
        print(original_md5)

        if original_md5 == md5_returned:
            print("MD5 verified.")
        else:
            print("MD5 verification failed!.")

while True:
    print("\n")
    print("----------------------------------")
    print("Choose function")
    print("1. Readme")
    print("2. Print file")
    print("3. Add user to file")
    print("4. Delete user")
    print("5. Create MD5 from baza.txt, save to baza.sum")
    print("6. Check MD5 baza.txt <> baza.sum")
    print("Press enter or 0 to exit program")
    print("----------------------------------")
    print('\n')

    answer = input("Enter function number: ")
    if answer == '1':
        about()
    elif answer == '2':
        print_file()
    elif answer == '3':
        write()
    elif answer == '4':
        delete_user()
    elif answer == '5':
        create_md5()
    elif answer == '6':
        check_md5()
    else:
        break
