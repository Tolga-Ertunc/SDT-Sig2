import random

def main():
    print("GIT Assignment Project-SDT")
    
    # Creating a list
    my_list = [0] * 10
    print(f"List created, size: {len(my_list)}")
    
    # Adding some random values for task G
    for i in range(len(my_list)):
        my_list[i] = random.randint(1, 100)
        print(f"my_list[{i}] = {my_list[i]}")

if __name__ == "__main__":
    main()