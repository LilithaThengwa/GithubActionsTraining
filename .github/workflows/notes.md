# For echo_to_console

- **`name`**: The name of the workflow, this will appear in the GitHub Actions dashboard.
- **`on`**: The triggers for the workflow:
  - **`push`**: Will trigger the workflow when code is pushed to specified branch.
  - **`workflow_dispatch`**: This allows the workflow to be triggered manually through the GitHub UI.
- **`jobs`**: Lists all the jobs that will run as part of this workflow. The job name in this case is `echo-job`.
  - **`runs-on`**: The OS to run the job on. `ubuntu-latest` is used in this case.
  - **`steps`**: The actions that will be executed in the job:
    - **`actions/checkout@v3`**: Checks out the code from the repository, this makes it available for the workflow access to work with.
    - **`run: echo "statement here"`**: Specifies a shell command or series of commands to execute within a workflow step.

When this file is pushed to your repository (inside the `.github/workflows/` directory), the workflow will run on every push to the specified branch or when manually triggered from GitHub.