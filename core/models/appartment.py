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
        return self.tenant is None

    def is_empty_soon(self) -> bool:
        return self.tenant_exit_day is not None

    def can_be_visited(self) -> bool:
        if self.is_empty() or self.is_empty_soon():
            return True
        return False
