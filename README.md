# SDT-Sig2
# GIT Project Report

This report documents the process of creating, developing, and managing a project using GIT commands. All steps were performed using both Terminal and IDE (Visual Studio Code) on macOS.

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
touch src/Main.java
```

Writing some example code:

<img width="491" alt="Screenshot 2025-05-03 at 16 29 30" src="https://github.com/user-attachments/assets/54d99e03-2c0f-4a58-af16-622eabd67c28" />

## d) Committing the Project to the Repository

Via Terminal:

```bash
git add .
git commit -m "Initial commit: Created a empty project"
```

*[Screenshot: First commit in Terminal]*
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
git add src/Main.java
git commit -m "Added table creation code"
```

<img width="603" alt="Screenshot 2025-05-03 at 16 36 05" src="https://github.com/user-attachments/assets/bc4cee08-5442-47f4-b20e-2913c09e53e5" />

## g) Adding More Code (Initializing Table with Random Values)

```java
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("GIT Assignment Project");
        
        // Creating table
        int[] table = new int[10];
        System.out.println("Table created, size: " + table.length);
        
        // Filling table with random values
        Random random = new Random();
        for (int i = 0; i < table.length; i++) {
            table[i] = random.nextInt(100);
            System.out.println("table[" + i + "] = " + table[i]);
        }
    }
}
```

*[Screenshot: Random values code in editor]*

## h) Committing Changes

```bash
git add src/Main.java
git commit -m "Table initialized with random values"
```

*[Screenshot: Random values commit]*

## i) Adding More Code (Sorting Table Elements)

```java
import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("GIT Assignment Project");
        
        // Creating table
        int[] table = new int[10];
        System.out.println("Table created, size: " + table.length);
        
        // Filling table with random values
        Random random = new Random();
        for (int i = 0; i < table.length; i++) {
            table[i] = random.nextInt(100);
            System.out.println("table[" + i + "] = " + table[i]);
        }
        
        // Sorting table elements
        System.out.println("\nBefore sorting:");
        printArray(table);
        
        Arrays.sort(table);
        
        System.out.println("\nAfter sorting:");
        printArray(table);
    }
    
    private static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
```

*[Screenshot: Sorting code in editor]*

## j) Committing Changes

```bash
git add src/Main.java
git commit -m "Added table sorting code"
```

*[Screenshot: Sorting commit]*

## k) Viewing Code History (git log)

```bash
git log
```

*[Screenshot: git log output]*

## l) Viewing Code Annotations (git blame)

```bash
git blame src/Main.java
```

*[Screenshot: git blame output]*

## m) Checking Out Different Revisions

```bash
git log --oneline
git checkout <commit-hash>
```

*[Screenshot: git checkout process]*

## n-o) Making Changes and Reverting

I made changes to the file without committing:

```java
// Increased table capacity (will not commit)
int[] table = new int[20];
```

Reverting changes:

```bash
git restore src/Main.java
```

*[Screenshot: git restore process]*

## p) Pushing the Project to the Remote Repository

```bash
git push origin main
```

*[Screenshot: git push process]*

## r) Deleting Local Project and Repository

```bash
cd ..
rm -rf SDT-Sig2
```

*[Screenshot: deleting local repository]*

## s) Cloning Project from Remote Repository

```bash
git clone https://github.com/Tolga-Ertunc/SDT-Sig2.git
```

*[Screenshot: re-cloning process]*

## t) Creating Tag/Release and Switching Between Tag and Master Branch

```bash
git tag v1.0
git tag
git checkout v1.0
git checkout main
```

*[Screenshot: git tag process]*

## u-w) Creating a New Branch and Switching to It

```bash
git branch development
git checkout development
# or
git checkout -b development
```

*[Screenshot: git branch process]*

## x) Improving Code in a Branch

I improved the sorting algorithm by adding bubble sort:

```java
private static void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

*[Screenshot: code improvement in development branch]*

## y) Merging the Branch into the Master Branch

```bash
git checkout main
git merge development
```

*[Screenshot: git merge process]*

## z) Sharing Repository URL with a Friend

I gave my friend access to the repository on GitHub.

*[Screenshot: adding collaborator on GitHub]*

## z1-z2) Creating and Resolving Conflicts

My friend and I edited the same file, creating a conflict.

*[Screenshot: git conflict message]*

Resolving the conflict:

*[Screenshot: conflict resolution editor]*

```bash
git add src/Main.java
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
