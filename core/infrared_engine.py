class InfraredEngine:
    def scan(self, commits):
        heat_map = {}
        for file in commits.files:
            change_rate = commits.get_change_frequency(file)
            failure_rate = commits.get_failure_rate(file)

            heat_score = (change_rate * 0.6) + (failure_rate * 0.4)

            heat_map[file] = heat_score
        return heat_map
