from dataclasses import dataclass
from datetime import datetime
from core.models.address import Address
from core.models.tenant import Tenant

__all__: list[str] = ["Appartment"]


@dataclass
class Appartment:
    address: Address
    tenant: Tenant | None = None
    tenant_exit_day: datetime | None = None

    def is_empty(self) -> bool:
        """Check if the apartment is empty.

        Returns:
            True if the apartment is empty, False otherwise.
        """
        return self.tenant is None

    def is_empty_soon(self) -> bool:
        """Checks if the apartment will be empty soon.

        Returns:
            True if the tenant exit day is not None, indicating that the apartment will
            be empty soon. False otherwise.
        """

        return self.tenant_exit_day is not None

    def can_be_visited(self) -> bool:
        """Checks if the apartment can be visited.

        Returns:
            True if the apartment can be visited, False otherwise.
        """

        if self.is_empty() or self.is_empty_soon():
            return True
        return False
