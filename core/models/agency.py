from dataclasses import dataclass, field
from datetime import datetime
from core.models.agent import Agent
from core.models.appartment import Appartment
from core.models.tenant import Tenant


__all__: list[str] = ["Agency"]


@dataclass
class Agency:
    agents: list[Agent] = field(default_factory=list)
    appartments: list[Appartment] = field(default_factory=list)

    def can_visit(
        self, local_date: datetime, appartment: Appartment, tenant: Tenant
    ) -> bool:
        can_visit: bool = all(
            [
                appartment.is_empty(),
                tenant.can_rent(),
                tenant.have_required_paycheck_amount(),
            ]
        )
        if not can_visit:
            return False
        for agent in self.agents:
            if not agent.can_visit(local_date):
                return False
        return True

    def show_appartment_in_city(self, city: str) -> Appartment | None:
        for appartment in self.appartments:
            if appartment.address.is_valid() and appartment.address.city == city:
                return appartment
        return None
