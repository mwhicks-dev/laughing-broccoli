from model.Risk import Risk
from model.Rows import Rows
from model.Reward import Reward

from model.DataTable import DataTable
from model.DataSummary import DataSummary

class DataProcessor:

    @staticmethod
    def summarize_data(risk: Risk, rows: Rows, rewards: list[Reward]) -> DataSummary:
        res: DataSummary = DataSummary()
        res.risk = risk
        res.rows = rows

        def find_ev():
            nonlocal res
            nonlocal rewards
            
            ev: float = 0
            for reward in rewards:
                ev += reward.probability * reward.reward
            res.expected_value = ev
        
        def find_stdev():
            nonlocal res
            nonlocal rewards

            stdev: float = 0
            for reward in rewards:
                stdev += reward.probability * ((res.expected_value - reward.reward) ** 2)
            res.standard_deviation = stdev ** 0.5
        
        find_ev()
        find_stdev()

        return res

    @staticmethod
    def summarize_all_data(data: DataTable) -> list[DataSummary]:
        res: list[DataSummary] = []

        for risk in data.risks:
            for rows in data.rows:
                key: str = data.key_risk_rows(risk, rows)
                res.append(DataProcessor.summarize_data(risk, rows, data.rewards[key]))
        
        return res