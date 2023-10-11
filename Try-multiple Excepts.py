#One Try_block Multiple Except_blocks
l=[10,20,30,"banglur","chennai"]
print("Before Error finding")
try:
    index=int(input("Enter:"))
    print(l[index])
    print(10/index)
except ValueError:
    index=int(input("Enter currectly:"))
    print(index)
    name(index)
except IndexError:
    print("Value Error occured")
except ZeroDivisionError:
    print("Zero Division Error occured")
finally:
    print("process is ended")
