# Setup

Install Git and Python 3. From an empty parent directory:

```sh
git clone https://github.com/Andrei09071108/git-branching-collaboration-workflow.git
cd git-branching-collaboration-workflow
python -m unittest discover -s tests -v
git status --porcelain
```

Expect three passing tests and an empty status. No external packages are needed.

## Reproduce the private baseline audit

From the extracted review package, run `git clone repository.bundle queue-demo` and enter queue-demo. Its main retains the original open-only rule. Switch to the combined rehearsal with `git switch --detach origin/rehearsal/integrated` and run the same three tests. The rehearsal ref is supplied in the private bundle.
