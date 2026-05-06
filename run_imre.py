from core.respiratory_engine import RespiratoryEngine
from ingestion.github_client import GitHubClient

repo = GitHubClient()
engine = RespiratoryEngine(repo)

commits = repo.get_recent_activity()
actions = engine.run_cycle(commits)

for action in actions:
    print(action)
