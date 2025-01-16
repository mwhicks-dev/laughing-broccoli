from .Risk import Risk
from .Rows import Rows
from .Reward import Reward

class DataTable:

    def __init__(self):
        self.risks: list[Risk] = []
        self.rows: list[Rows] = []
        self.rewards: dict[str, list[Reward]] = {}

    def key_risk_rows(self, risk: Risk, rows: Rows) -> None:
        return f"{risk.id}-{rows.id}"
    
    def _add_risk_rows(self, risk: Risk, rows: Rows) -> None:
        self.rewards[self.key_risk_rows(risk, rows)] = []

    def add_risk(self, risk: Risk) -> None:
        self.risks.append(risk)
        for item in self.rows:
            self._add_risk_rows(risk, item)

    def add_row(self, rows: Rows) -> None:
        self.rows.append(rows)
        for item in self.risks:
            self._add_risk_rows(item, rows)
    
    def add_reward(self, reward: Reward) -> None:
        self.rewards[self.key_risk_rows(reward.risk, reward.rows)].append(reward)