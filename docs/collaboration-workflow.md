# Collaboration workflow

From an up-to-date main, use git switch -c feature/name in a separate clone. Make a focused change and add a regression test. Review git diff, stage the intended files and inspect git diff --cached before committing. Compare the proposal using git diff main...HEAD.

For hosted review, push the feature, open a pull request targeting main and complete the template. Check the base and head, read the diff and reproduce the tests locally. Merge the waiting proposal first. For the reopened proposal, incorporate main, resolve the status rule and run the combined tests before completing the second pull request.

## Recovery

Before switching tasks use git stash push -u to save tracked and untracked edits. Inspect git stash list and use git stash apply to retain the backup while checking the result. For a lost local commit, locate it with git reflog and preserve it with git branch rescue/work COMMIT. On a shared branch undo an ordinary commit through a reviewed git revert COMMIT. For a merge revert, inspect both parents and agree which parent represents the integration line before selecting a mainline.
