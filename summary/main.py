from model.DataTable import DataTable
from model.DataSummary import DataSummary

from use_case.DataReader import DataReader
from use_case.DataProcessor import DataProcessor

risk_file = open("../data/risk.csv", "r")
rows_file = open("../data/rows.csv", "r")
reward_file = open("../data/reward.csv", "r")

data: DataTable = DataReader.get_data_table(risk_file, rows_file, reward_file)

risk_file.close()
rows_file.close()
reward_file.close()

summaries: list[DataSummary] = DataProcessor.summarize_all_data(data)

summaries.sort(key=lambda x : x.expected_value)

for summary in summaries:
    print(f"{summary}\n")
