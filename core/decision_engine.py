class DecisionEngine:
    def evaluate(self, impact_map):
        actions = []

        for file, score in impact_map.items():
            if score > 0.8:
                actions.append({
                    "type": "ALERT",
                    "file": file,
                    "severity": "HIGH"
                })

        return actions
