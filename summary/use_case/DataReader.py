from io import TextIOWrapper

from model.Risk import Risk
from model.Rows import Rows
from model.Reward import Reward

from model.DataTable import DataTable

class DataReader:

    @staticmethod
    def get_data_table(risk: TextIOWrapper, rows: TextIOWrapper, reward: TextIOWrapper) -> DataTable:
        res: DataTable = DataTable()

        def process_risks():
            nonlocal res
            nonlocal risk

            next(risk)
            for line in risk:
                [id,name] = line.split(",")
                
                id.strip()
                name.strip()

                tmp: Risk = Risk()
                tmp.id = int(id)
                tmp.risk = name

                res.add_risk(tmp)
        
        def process_rows():
            nonlocal res
            nonlocal rows

            next(rows)
            for line in rows:
                [id,count] = line.split(",")

                id.strip()
                count.strip()

                tmp: Rows = Rows()
                tmp.id = int(id)
                tmp.rows = count

                res.add_row(tmp)
        
        def process_rewards():
            nonlocal res
            nonlocal reward

            next(reward)
            for line in reward:
                [risk_id,rows_id,multiplier,prob] = line.split(",")

                risk_id.strip()
                rows_id.strip()
                multiplier.strip()
                prob.strip()

                tmp: Reward = Reward()
                tmp.risk = res.risks[int(risk_id)]
                tmp.rows = res.rows[int(rows_id)]
                tmp.reward = float(multiplier)
                tmp.probability = float(prob)

                res.add_reward(tmp)
        
        process_risks()
        process_rows()
        process_rewards()

        return res