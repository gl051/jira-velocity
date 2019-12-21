import pandas as pd
from pathlib import Path

# Edit this parameters
JIRA_INPUT_FILE = "platform-sprint-19.11.2.csv"
SPRINT_VERSION = "19.11.2"
JIRA_MASTER_FILE = "platform-jira.csv"

p = Path(__file__)
new_export_file = p.cwd() / "jira-exports" / JIRA_INPUT_FILE


df_master = pd.read_csv(JIRA_MASTER_FILE)
df_input = pd.read_csv(new_export_file)
df_input['sprint_completed'] = SPRINT_VERSION
frames = [df_master, df_input]
result = pd.concat(frames, sort=False)
result.to_csv(JIRA_MASTER_FILE, index=False)
