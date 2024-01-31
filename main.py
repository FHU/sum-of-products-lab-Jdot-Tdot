#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    pass

# Uses list comprehension to check for errors and returns a list with integers
def get_input_to_list():
    the_input = input().split()
    listing = True
    while(listing):
        try:
            input_ready = [int(number) for number in the_input]
            listing = False
        except TypeError:
            print("Try again with only numbers and letters")
            the_input = input().split()
    return input_ready


# Remind students that this makes it to where it only happens if it is not a module.
# It's how the entire thing is tested.
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    
    list1 = get_input_to_list()
    list2 = get_input_to_list()

    the_sum = sum_of_products(list1,list2)