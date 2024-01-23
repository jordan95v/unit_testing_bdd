from dataclasses import dataclass
from datetime import datetime

__all__: list[str] = ["Paycheck"]


@dataclass
class Paycheck:
    date: datetime
    company_name: str
