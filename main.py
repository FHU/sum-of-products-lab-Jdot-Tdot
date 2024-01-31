#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    pass

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

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    pass