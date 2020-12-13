import math

print("So we know that if you need to do 100 things, and you do seven things a week, then you'll take 100 days to do it")
print("But what if you didn't just do 1 thing a day?")
print("here is where this program comes in handy!")
print("Just tell me how many activities you need to do, and then how many times a week you'll do it, and I'll tell you how many days it'll take")
input("\nPress anything to proceed")

print("\n"*5)
while True:
    try:
        activities = int(input("So how many things do you need to do? Write a whole number\n"))

        frequency = int(input("How many times a week will you do it? write a whole number\n"))
        break
    except:
        print("\nPlease type a whole number.\n")
#Now we divided days by number of times a week, and then multiply all that by 7 to get our answer!

final_answer = (activities / frequency) * 7

#And now we round up, as half a day is still another day you have to do stuff

final_answer = math.ceil(final_answer)

print(f"\n\n\nIt'll take you {final_answer} days to complete {activities} tasks, doing them {frequency} times a week.")
print("\nGood luck doing that!")
