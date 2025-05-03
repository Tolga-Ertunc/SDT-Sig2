import random

def main():
    print("GIT Assignment Project-SDT")
    
    # Creating a list
    my_list = [0] * 10
    print(f"List created, size: {len(my_list)}")
    
    # Filling list with some random values
    for i in range(len(my_list)):
        my_list[i] = random.randint(1, 100)
        print(f"my_list[{i}] = {my_list[i]}")
    
    # Sorting list elements for task I/i    
    print("\nBefore sorting:")
    print_list(my_list)
    
    my_list.sort()
    
    print("\nAfter sorting:")
    print_list(my_list)

def print_list(lst):
    print(' '.join(map(str, lst)))

if __name__ == "__main__":
    main()