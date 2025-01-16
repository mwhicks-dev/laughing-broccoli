from .Risk import Risk
from .Rows import Rows

class DataSummary:

    risk: Risk
    rows: Rows
    expected_value: float
    standard_deviation: float

    def __str__(self):
        res: str = f"Risk: {self.risk.risk}; Rows: {self.rows.rows}\n"
        res += f"Expected Value: {self.expected_value}\n"
        res += f"Standard Deviation: {self.standard_deviation}"

        return res