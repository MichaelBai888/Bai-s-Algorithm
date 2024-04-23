import math
import time

def gcd(a,b):
    while b!= 0:
        a,b =b, a%b
    return a
def check_factors(number):
    factors = []
    if number in {2, 3, 5, 7}:
        return False
    if number % 2 == 0:
        factors.extend([2, number // 2])
        print("Factors:", factors)
        return True
    if number % 5 == 0:
        factors.extend([5, number // 5])
        print("Factors:", factors)
        return True
        
    if sum(map(int, str(number))) % 3 == 0:
        factors.append(3)
        factors.append(number//3)
        print("Factors:", factors)
        return True
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if sum(map(int, str(i))) % 3 == 0:
            continue
        if i % 5 == 0:  # Skip multiples of 5
            continue
        if gcd(i, number)>1:
            factors.append(i)
            factors.append(number//i)
            print("Factors:", factors)
            return True 
    return False

                
    

def play_game():
    user_input = input("Enter a number greater than or equal to 2: ")

    if user_input.isdigit() and int(user_input) >= 2:
        number = int(user_input)

        if not check_factors(number):
            print("It is prime")
            
        else:
            print("It is not prime")
            
    else:
        print("Invalid input. Please enter a valid number greater than or equal to 2.")

def play_again():
    play_choice = input("Do you want to play again? (yes/no): ").lower()
    return play_choice == 'yes'

while True:
    start_time = time.time()
    play_game()
    end_time = time.time()
    
    print("Elpased time = " + str(end_time - start_time))
    if not play_again():
        break
