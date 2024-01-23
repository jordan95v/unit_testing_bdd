from datetime import datetime, timedelta
from core.models.agent import Agent


class TestAgent:
    def test_can_visit(self) -> None:
        """Etant donnée un agent disponible à la date demandé
        Lorsque je vérifie sur l'agent est disponible pour une visite
        Alors il est disponible pour une visite
        """

        agent: Agent = Agent("jordan@gmail.com", "Jordan", "Dufresne", [])
        assert agent.can_visit(datetime.now())

    def test_can_not_visit(self) -> None:
        """Etant donnée un agent non disponible à la date demandé
        Lorsque je vérifie sur l'agent est disponible pour une visite
        Alors il n'est pas disponible pour une visite
        """

        agent: Agent = Agent("jordan@gmail.com", "Jordan", "Dufresne", [datetime.now()])
        assert not agent.can_visit(datetime.now())

    def test_get_next_availability(self) -> None:
        """Etant donnée un agent non disponible le lendemain
        Lorsque je vérifie sa prochaine disponibilité
        Alors il est disponible le surlendemain
        """

        agent: Agent = Agent(
            "jordan@gmail.com",
            "Jordan",
            "Dufresne",
            [datetime.now() + timedelta(days=1)],
        )
        next_availability: datetime | None = agent.get_next_availability()
        assert next_availability is not None
        assert next_availability.date() == (datetime.now() + timedelta(days=2)).date()

    def test_get_next_availability_none(self) -> None:
        """Etant donnée un agent non disponible pendant 30 jours
        Lorsque je vérifie sa prochaine disponibilité
        Alors il n'est plus disponible
        """

        days_off: list[datetime] = []
        for i in range(1, 31):
            days_off.append(datetime.now() + timedelta(days=i))
        agent: Agent = Agent("jordan@gmail.com", "Jordan", "Dufresne", days_off)
        assert agent.get_next_availability() is None
