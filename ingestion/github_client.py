class GitHubClient:
    def get_recent_activity(self):
        # Temporary mock data (replace later with real API)
        return MockCommits()


class MockCommits:
    def __init__(self):
        self.files = ["app.py", "utils.py"]

    def get_change_frequency(self, file):
        return 0.5

    def get_failure_rate(self, file):
        return 0.2
