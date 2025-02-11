def print_even(nums):
    for i in nums:
        if int(i) % 2 == 0:
            print(i)

numbers = [1,2,3,4,5,6,7] #СПИСОК
print_even(numbers)
print_even([10,15,20,25])
print("---")
print_even(range(10))
print("---")
r = range(12)
print_even(r)


s = ["1","2","3"]
print_even(s)
