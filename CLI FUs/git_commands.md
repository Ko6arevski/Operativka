
# Common Git Commands

This document lists common Git commands, their usage, and examples to help you work with Git repositories effectively.

## 1. git init
Initialize a new Git repository.

**Usage:**
```bash
git init
```

**Example:**
```bash
mkdir my_project
cd my_project
git init
```

---

## 2. git clone
Clone an existing repository from a remote server.

**Usage:**
```bash
git clone <repository-url>
```

**Example:**
```bash
git clone https://github.com/user/repo.git
```

---

## 3. git status
Check the status of the working directory and staging area.

**Usage:**
```bash
git status
```

**Example:**
```bash
git status
```

---

## 4. git add
Add changes to the staging area.

**Usage:**
```bash
git add <file>           # Add a specific file
git add .                # Add all files in the current directory
```

**Example:**
```bash
git add index.html
git add .
```

---

## 5. git commit
Commit staged changes with a message.

**Usage:**
```bash
git commit -m "Your commit message"
```

**Example:**
```bash
git commit -m "Add new feature"
```

---

## 6. git push
Push local changes to a remote repository.

**Usage:**
```bash
git push <remote> <branch>
```

**Example:**
```bash
git push origin main
```

---

## 7. git pull
Fetch and integrate changes from a remote repository into the current branch.

**Usage:**
```bash
git pull <remote> <branch>
```

**Example:**
```bash
git pull origin main
```

---

## 9. git checkout
Switch to a different branch or restore files.

**Usage:**
```bash
git checkout <branch-name>    # Switch to a branch
git checkout -- <file>        # Discard changes to a file
git checkout <branch-name> <file>  # Restore a file from another branch
```

**Example:**
```bash
git checkout main
git checkout -- index.html
git checkout other_branch ./file_that_is_needed  # Restore a file from another branch
```

---

## 8. git branch
List, create, or delete branches.

**Usage:**
```bash
git branch                # List all branches
git branch <branch-name>   # Create a new branch
git checkout -b <branch-name> # Create and switch to a new branch
git branch -d <branch-name> # Delete a branch
```

**Example:**
```bash
git branch
git branch feature-branch
git checkout -b feature-branch
git branch -d feature-branch
```

---

## 10. git merge
Merge changes from one branch into another. Below is my explanation of how it works as it took me so,me time to understand. 
1. You are working in your branch, so the one with the new changes.
2. You checkout to the branch you want to merge the changes into.
3. BEST PRACTICE - pull at this point to get the latest changes from the branch you are merging into.
4. You merge the branch with the new changes into the branch you are currently in.

**Usage:**
```bash
git merge <branch-name>
```

**Example:**
```bash
git checkout main
git pull
git merge feature-branch
```

---

## 11. git fetch
Fetch changes from a remote repository without merging them.

**Usage:**
```bash
git fetch <remote>
```

**Example:**
```bash
git fetch origin
```

---

## 12. git log
Show the commit history for the current branch.

**Usage:**
```bash
git log
```

**Example:**
```bash
git log
```

---

## 13. git reset
Unstage or reset changes in your working directory.

**Usage:**
```bash
git reset <file>           # Unstage a file
git reset --hard <commit>  # Reset to a specific commit
```

**Example:**
```bash
git reset index.html
git reset --hard HEAD~1
```

---

## 14. git stash
Save changes that you don't want to commit immediately.

**Usage:**
```bash
git stash                 # Stash changes
git stash apply           # Apply stashed changes
```

**Example:**
```bash
git stash
git stash apply
```

---

## 15. git remote
Manage remote repositories.

**Usage:**
```bash
git remote -v             # List remote repositories
git remote add <name> <url>  # Add a new remote repository
```

**Example:**
```bash
git remote -v
git remote add origin https://github.com/user/repo.git
```

---

## 16. git rebase
Reapply commits on top of another base branch.

**Usage:**
```bash
git rebase <branch>
```

**Example:**
```bash
git checkout feature-branch
git rebase main
```

---

## 17. git diff
Show changes between commits, branches, or working directory files.

**Usage:**
```bash
git diff <file>           # Show changes in a file
git diff <branch1> <branch2>  # Show differences between branches
```

**Example:**
```bash
git diff index.html
git diff main feature-branch
```
