# Conflict decision

Both proposals change the same ACTIVE tuple. Waiting tickets need follow-up and reopened tickets have returned to the queue. Both count as active. Closed tickets remain excluded. Selecting either entire side would discard a business requirement.

From the common base merge feature/waiting with --no-ff, then try feature/reopened. Use git status --short and git ls-files -u to locate the unresolved file. Inspect the base, current and incoming versions with git show :1:src/queue_summary.py, :2: and :3: respectively. Replace only the marked section with ACTIVE = ('open', 'waiting', 'reopened'). Stage the file, run all three tests, inspect git diff --cached and commit the resolution. Verify both tips with git merge-base --is-ancestor.
