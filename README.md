# Git Branching & Collaboration Workflow

Independent, AI-assisted single-author portfolio demonstration. A fictional support queue needed two concurrent changes. Separate feature branches proposed counting waiting and reopened tickets, respectively. Both pull requests were opened before either was integrated.

[PR #1](https://github.com/Andrei09071108/git-branching-collaboration-workflow/pull/1) and [PR #2](https://github.com/Andrei09071108/git-branching-collaboration-workflow/pull/2) were integrated through merge commits. Updating the second feature with main produced a conflict in the active-status rule. The resolution retains open, waiting and reopened and excludes closed. Three regression tests cover the resulting behaviour.

Follow the [setup guide](docs/setup.md) to run the tests. See the [collaboration workflow](docs/collaboration-workflow.md), [conflict decision](docs/conflict-resolution.md) and [acceptance record](docs/acceptance-checklist.md) for the review and handover.
