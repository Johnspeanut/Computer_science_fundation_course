"""Student name: Qiong Peng
CS 5001 Section 4 
Instructor: Dr.Abi
Homework 1 written component
"""
# Question 1
def main1(a):
    print("The type of {} is".format(a), type(a))


main1(a = 48.25)
main1(a = 48)
main1(a = -1)
main1(a = True)
main1(a = "False")
main1(a = -5.0)
main1(a = 'hello')
main1(a = 0)


"""Question 2
"""
def main2():
    print("The value of 7/5 is ", 7 / 5)
    print("The value of 7.0/5.0 is ", 7.0 / 5.0)
    print("The value of 14//10 is ", 14 // 10)
    print("The value of 14%10 is ", 14 % 10)
    print("The value of 6**2 is ", 6 ** 2)
    print("The value of 6%2 is ", 6 % 2)
    print("The value of 'red'+'1234' is ", "red" + "1234")
    print("The value of 'yellow'*2 is ", "yellow"*2)

if __name__=="__main__":
    main2()

user_number = int(input("Enter a whole number greater than 0"))
x =  user_number // 3
x = x ** 2
print(x)