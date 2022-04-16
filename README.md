https://stackoverflow.com/questions/14848274/git-log-to-get-commits-only-for-a-specific-branch

```git
git cherry -v develop UI-5636
```
https://stackoverflow.com/questions/38495989/how-to-get-git-parent-branch-name-from-current-branch
```git
git merge-base UI-5636 develop
```
