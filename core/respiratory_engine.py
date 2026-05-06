from core.infrared_engine import InfraredEngine
from core.magnetic_engine import MagneticEngine
from core.decision_engine import DecisionEngine

class RespiratoryEngine:
    def __init__(self, repo):
        self.repo = repo
        self.ir = InfraredEngine()
        self.mag = MagneticEngine()
        self.decision = DecisionEngine()

    def run_cycle(self, commits):
        heat_map = self.ir.scan(commits)
        dependency_impact = self.mag.analyze(heat_map)
        actions = self.decision.evaluate(dependency_impact)
        return actions
