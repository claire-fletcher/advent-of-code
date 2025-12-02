def calculate_password_1(dial_instructions):
    """ 
    Calculate the password based on dial instructions where only ending on a 0 counts 
    """

    dial = 50
    count = 0

    for instruction in dial_instructions:
        # split the number and direction
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'L':
           remainder = distance % 100 # All above 100 are just rotations around, therefore irrelevant
           dial -= remainder
           if dial < 0:
               dial += 100 # Wrap around

        elif direction == 'R':
            remainder = distance % 100 # All above 100 are just rotations around, therefore irrelevant
            dial += remainder
            if dial >= 100:
                dial -= 100 # Wrap around
            
        if dial == 0:
            count += 1
    
    return count

def calculate_password_2(dial_instructions):
    """ 
    Calculate the password based on dial instructions where every 0 we pass counts
    """

    dial = 50
    count = 0

    for instruction in dial_instructions:
        # split the number and direction
        direction = instruction[0]
        distance = int(instruction[1:])

        print(f"Current dial before move: {dial}")
        print(f"Current count before move: {count}")

        if direction == 'L':
            print(f"Moving L by {distance}, which is {distance // 100} full rotations and {distance % 100} extra")

            remainder = distance % 100 
            count += distance // 100 # Every rotation goes past 0
            dial -= remainder

            if dial < 0:
               count += 1 
               dial += 100

        elif direction == 'R':
            print(f"Moving R by {distance}, which is {distance // 100} full rotations and {distance % 100} extra")
        
            remainder = distance % 100 
            count += distance // 100 # Every rotation goes past 0
            dial += remainder
            

            if dial >= 100:
                count += 1 
                dial -= 100 

        print("ending dial: ", dial)
    
    return count

# TODO: adjust to stream in the info instead for better memory!
def main():
    print("Reading input file...")
    dial_instructions = []
    with open("./input.txt", "r") as file:
        for line in file:
            dial_instructions.append(line.strip())

    result = calculate_password_1(dial_instructions)
    result_b = calculate_password_2(dial_instructions)

    print(
        "Final Result Part A: ",
        result
    )

    print(
        "Final Result Part B: ",
        result_b
    )

if __name__ == "__main__":
    main()