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
        """Determines if the agency can visit the apartment on the given date.

        Args:
            local_date: The date of the visit.
            appartment: The apartment that is going to be visited.
            tenant: The tenant who wants to visit the appartment.

        Returns:
            True if the agency can visit the apartment, False otherwise.
        """

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
        """Returns the first valid apartment in the given city.

        Args:
            city: The city to search for apartments in.

        Returns:
            The first valid apartment found in the given city, or None if no valid
            apartment is found.
        """

        for appartment in self.appartments:
            if appartment.address.is_valid() and appartment.address.city == city:
                return appartment
        return None
