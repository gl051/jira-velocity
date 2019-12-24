# jira-velocity
Build custom velocity charts, work in progress ..

## Getting exports from JIRA
1. Look at the velocity chart
2. Select a sprint closed
3. Click on _View on issue navigator_
4. Select the following columns (order does not matter): Key, Status, Workstream, Project, Story Point
5. Export as CSV (selected columns)
6. Save the file as `platform-sprint-<sprint name>`.csv
7. Move the file to ./jira-exports
