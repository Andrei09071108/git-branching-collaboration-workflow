# Branch strategy

main is the integration target. feature/waiting and feature/reopened start at the same commit so each proposal can be reviewed independently. Use git merge --no-ff to retain the branch tip and a two-parent integration record. Inspect it with git log --graph --oneline --all.

Rebase replays commits on a new base and changes their identifiers. It is suitable for cleaning up an unpublished personal branch. For a shared feature, merge current main into it and resolve differences together. Rewriting published history can invalidate another contributor’s work. During an unfinished operation use git merge --abort or git rebase --abort as appropriate, after protecting any unrelated edits.
