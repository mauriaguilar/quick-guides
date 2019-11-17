# GIT TIPS TO SOLVE DISASTERS (Be careful)

# re-commit
git commit --amend

# untrack files
git reset <file>

# uncommit
# 1 commit
git reset --hard HEAD^
# 2 commits
git reset --hard HEAD~2
# 2 commits without delete changes
git reset HEAD~2

# force push to remote repo
git push origin -f
