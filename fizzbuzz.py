import sys

def main():
    argv = sys.argv
    argc = len(argv)

    if(argc != 2):
        print ("Usage: python %s max_number")
        exit()

    num = int(argv[1])+1

    for i in range(1,num):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()
