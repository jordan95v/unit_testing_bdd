from dataclasses import dataclass, field
from datetime import datetime, timedelta
from core.models.user import User

__all__: list[str] = ["Agent"]


@dataclass
class Agent(User):
    day_off: list[datetime] = field(default_factory=list)

    def can_visit(self, local_date: datetime) -> bool:
        """Checks if the agent is available to visit on the given date.

        Args:
            local_date: The date to check if the agent is available.

        Returns:
            True if the agent is available, False otherwise.
        """

        for day_off in self.day_off:
            if day_off.date() == local_date.date():
                return False
        return True

    def get_next_availability(self) -> datetime | None:
        """Get the next availability date for the agent.

        Returns:
            The next availability date if found, None otherwise.
        """

        for i in range(1, 30):
            local_date: datetime = datetime.now() + timedelta(days=i)
            for day_off in self.day_off:
                if local_date.date() == day_off.date():
                    break
            else:
                return local_date
        return None
