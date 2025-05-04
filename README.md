# SDT-Sig2
# GIT Project Report

This  process documents creating, developing, and managing a project using GIT commands. All steps were performed using both Terminal and IDE (Visual Studio Code) on macOS.

## a) Creating a Remote Repository (GitHub)

I created a new repository on GitHub.

<img width="1411" alt="Screenshot 2025-05-03 at 16 21 14" src="https://github.com/user-attachments/assets/d4a090ce-82c4-4b8c-8df9-df2d73a6878f" />

## b) Cloning the Empty Repository

Via Terminal:

```bash
git clone https://github.com/Tolga-Ertunc/SDT-Sig2.git
cd SDT-Sig2
```
<img width="596" alt="Screenshot 2025-05-03 at 16 22 25" src="https://github.com/user-attachments/assets/c8983148-4bee-42c7-ad0d-d961dd57a4bf" />

## c) Creating an Empty Project in the Local Repository

Preferred language: Python

<img width="719" alt="Screenshot 2025-05-03 at 16 28 16" src="https://github.com/user-attachments/assets/b1b2bddb-d950-4db8-8e46-db0efa5afb46" />


Creating project folder via Terminal:

```bash
mkdir src
touch src/main.py
```

Writing some example code:

<img width="491" alt="Screenshot 2025-05-03 at 16 29 30" src="https://github.com/user-attachments/assets/54d99e03-2c0f-4a58-af16-622eabd67c28" />

## d) Committing the Project to the Repository

Via Terminal:

```bash
git add .
git commit -m "Initial commit: Created a empty project"
```

<img width="683" alt="Screenshot 2025-05-03 at 16 32 04" src="https://github.com/user-attachments/assets/b79922b8-6fa8-4d3f-9405-4cddc24dbc2b" />


## e) Adding Simple Code (Creating a Table)

I edited the main.py file to add list creation code:

```python
def main():
    print("GIT Assignment Project-SDT")
    
    # Creating a basic list
    my_list = [0] * 10
    print(f"List created, size: {len(my_list)}")

if __name__ == "__main__":
    main()
```
<img width="436" alt="Screenshot 2025-05-03 at 16 34 38" src="https://github.com/user-attachments/assets/069f34f6-484c-4e99-b1c3-7995fd25df42" />

## f) Committing Changes

```bash
git add src/main.py
git commit -m "Added table creation code"
```

<img width="603" alt="Screenshot 2025-05-03 at 16 36 05" src="https://github.com/user-attachments/assets/bc4cee08-5442-47f4-b20e-2913c09e53e5" />

## g) Adding More Code (Initializing Table with Random Values)

```python
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
```

<img width="484" alt="Screenshot 2025-05-03 at 17 01 16" src="https://github.com/user-attachments/assets/3ed1cabb-0eee-4df4-9ba3-7fc589929a31" />

## h) Committing Changes

```bash
git add src/main.py
git commit -m "Table initialized with some random values"
```

<img width="690" alt="Screenshot 2025-05-03 at 17 00 43" src="https://github.com/user-attachments/assets/9e3d97e2-4d37-49ca-8f7d-5b73967ef2c1" />

## i) Adding More Code (Sorting Table Elements)

```python
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
```


## j) Committing Changes

```bash
git add src/main.py
git commit -m "Added table sorting code"
```

<img width="585" alt="Screenshot 2025-05-03 at 17 06 03" src="https://github.com/user-attachments/assets/233e7999-8489-4831-b770-71563af7f666" />

## k) Viewing Code History (git log)

```bash
git log
```
<img width="813" alt="Screenshot 2025-05-03 at 17 06 43" src="https://github.com/user-attachments/assets/9a3ff932-dfeb-439d-bf38-343578e89d00" />


## l) Viewing Code Annotations (git blame)

```bash
git blame src/main.py
```
<img width="691" alt="Screenshot 2025-05-03 at 17 08 26" src="https://github.com/user-attachments/assets/3a337b4f-a1ba-471c-bed1-09f3574f4a86" />


## m) Checking Out Different Revisions

```bash
git log --oneline
git checkout d635e70
```
<img width="671" alt="Screenshot 2025-05-03 at 17 10 25" src="https://github.com/user-attachments/assets/6d460c09-5ea7-402e-b7ca-1680b3dff81d" />


## n-o) Making Changes and Reverting

I made changes to the file without committing:

```python
# Increased table capacity (will not commit)
 my_list = [0] * 12
```
<img width="574" alt="Screenshot 2025-05-03 at 17 12 01" src="https://github.com/user-attachments/assets/77daaf0f-c66b-431c-aada-e7d01f363dd5" />

Reverting changes:

```bash
git restore src/main.py
```
<img width="440" alt="Screenshot 2025-05-03 at 17 13 22" src="https://github.com/user-attachments/assets/b98fd408-34a1-46b7-818b-2443ef40d15f" />


## p) Pushing the Project to the Remote Repository

```bash
git push origin main
```
<img width="557" alt="Screenshot 2025-05-03 at 17 16 24" src="https://github.com/user-attachments/assets/01872b0e-4fb6-49c6-af4e-31f364dbfbf1" />


## r) Deleting Local Project and Repository

```bash
cd ..
rm -rf SDT-Sig2
```
<img width="360" alt="Screenshot 2025-05-03 at 17 18 57" src="https://github.com/user-attachments/assets/b21e2f06-b17e-4c63-b0b0-9a444fec6f2d" />


## s) Cloning Project from Remote Repository

```bash
git clone https://github.com/Tolga-Ertunc/SDT-Sig2.git
```
<img width="654" alt="Screenshot 2025-05-03 at 17 20 30" src="https://github.com/user-attachments/assets/4dbbd41c-4570-4cf7-8af5-e01a78b37316" />

## t) Creating Tag/Release and Switching Between Tag and Master Branch

```bash
git tag v1.0
git tag
git checkout v1.0
git checkout main
```
<img width="697" alt="Screenshot 2025-05-03 at 17 22 19" src="https://github.com/user-attachments/assets/6175d324-1576-4606-85af-18cfafa5ae8b" />


## u-w) Creating a New Branch and Switching to It

```bash
git branch development
git checkout development
```
<img width="511" alt="Screenshot 2025-05-03 at 17 23 20" src="https://github.com/user-attachments/assets/d09c5137-2f53-4d36-9945-3fd5197b2786" />


<img width="468" alt="Screenshot 2025-05-03 at 17 24 50" src="https://github.com/user-attachments/assets/3f21e651-5021-4f36-8d40-92c25537ae73" />



## x) Improving Code in a Branch

I added some changes to my python code.

```python
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
    
    # Sorting list elements for taks I/i
    print("\nBefore sorting:")
    print_list(my_list)
    
    # Change: adding a message about the sorting algorithm
    print("\nSorting using Python's built-in sort (development branch)")
    my_list.sort()
    
    print("\nAfter sorting:")
    print_list(my_list)

def print_list(lst):
    print(' '.join(map(str, lst)))

if __name__ == "__main__":
    main()
```
<img width="695" alt="Screenshot 2025-05-03 at 17 28 25" src="https://github.com/user-attachments/assets/4f28841f-b607-4400-8d35-798439612085" />



## y) Merging the Branch into the Master Branch

```bash
git checkout main
git branch
git pull origin main
git merge development
git push origin main
```

<img width="658" alt="Screenshot 2025-05-03 at 17 32 34" src="https://github.com/user-attachments/assets/5d6609a4-0b9a-465f-8ddf-d8e385f6a7da" />


## z) Sharing Repository URL with a Friend

I gave my friend access to the repository on GitHub.

*[Screenshot: adding collaborator on GitHub]*

## z1-z2) Creating and Resolving Conflicts

My friend and I edited the same file, creating a conflict.

*[Screenshot: git conflict message]*

Resolving the conflict:

*[Screenshot: conflict resolution editor]*

```bash
git add src/main.py
git commit -m "Conflict resolved"
git push origin main
```

*[Screenshot: conflict resolution commit]*

## z3) Sending Repository URL to Teacher

I gave my teacher access to the repository and sent the URL via email.

*[Screenshot: adding teacher access on GitHub]*

## Tools Used

- macOS Terminal
- Visual Studio Code
- Git
- GitHub

## Repository URL

- GitHub: https://github.com/Tolga-Ertunc/SDT-Sig2
