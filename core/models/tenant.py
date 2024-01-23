from datetime import datetime
from typing import ClassVar
from core.models.user import User
from core.models.paycheck import Paycheck

__all__: list[str] = ["Tenant"]


class Tenant(User):
    NB_PAYCHECK_MONTH: ClassVar[int] = 3
    MINIMUM_REQUIRED_AGE: ClassVar[int] = 21

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        birth_date: datetime,
        job: str,
        paychecks: list[Paycheck],
    ) -> None:
        super().__init__(email, last_name, first_name)
        self.birth_date: datetime = birth_date
        self.job = job
        self.paychecks: list[Paycheck] = paychecks

    def can_rent(self) -> bool:
        """Determines whether the tenant is eligible to rent a property.

        Returns:
            True if the tenant is eligible to rent, False otherwise.
        """

        age: int = datetime.now().year - self.birth_date.year
        if age < self.MINIMUM_REQUIRED_AGE:
            return False
        if not self.have_required_paycheck_amount():
            return False
        if not self.job:
            return False
        return True

    def have_required_paycheck_amount(self) -> bool:
        """Checks if the tenant has the required number of paychecks.

        Returns:
            True if the tenant has the required number of paychecks, False otherwise.
        """
        return len(self.paychecks) >= self.NB_PAYCHECK_MONTH
