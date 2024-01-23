from datetime import datetime
import pytest
from pytest_mock import MockerFixture
from core.models.address import Address
from core.models.agency import Agency
from core.models.agent import Agent
from core.models.appartment import Appartment
from core.models.paycheck import Paycheck
from core.models.tenant import Tenant


@pytest.fixture
def agent() -> Agent:
    return Agent("jordan@gmail.com", "Jordan", "Dufresne", [datetime(2000, 2, 28)])


class TestAgence:
    def test_show_appartment_in_city_ok(self) -> None:
        """Etant donnée qu'il y a dans l'agence un appartement situé sur Paris
        Et que cet appartement est vide
        Et qu'il y a un autre appartement vide qui n'est pas à Paris
        Lorsque je veux proposer un appartement dans la ville de Paris
        Alors l'appartement situé dans Paris est proposé
        """

        appartments: list[Appartment] = [
            Appartment(Address("1 Rue de la Paix", 75001, "Paris"), None, None),
            Appartment(Address("10 Rue de Jordanie", 60000, "Lyon"), None, None),
        ]
        agency: Agency = Agency([], appartments)
        proposed_appartment: Appartment | None = agency.show_appartment_in_city("Paris")
        assert proposed_appartment is not None
        assert proposed_appartment.address.city == "Paris"

    def test_show_appartment_in_city_ko(self) -> None:
        """Etant donnée qu'il n'y a dans l'agence aucun appartement situé sur Paris
        Et qu'il y a un autre appartement vide qui n'est pas à Paris
        Lorsque je veux proposer un appartement dans la ville de Paris
        Alors aucun appartement ne m'est proposé
        """

        appartments: list[Appartment] = [
            Appartment(Address("10 Rue de Romanie", 93200, "Saint-Denis"), None, None),
            Appartment(Address("10 Rue de Jordanie", 60000, "Lyon"), None, None),
        ]
        agency: Agency = Agency([], appartments)
        proposed_appartment: Appartment | None = agency.show_appartment_in_city("Paris")
        assert proposed_appartment is None

    def test_can_visit(
        self,
        mocker: MockerFixture,
        agent: Agent,
        appartment: Appartment,
        tenant: Tenant,
    ) -> None:
        """Etant donné que l'agence a un agent disponible à la date demandée
        Et que l'appartement est vide
        Et que le locataire peut louer
        Et que le locataire a un nombre de bulletins de salaire suffisant
        Lorsque je veux visiter l'appartement
        Alors je ne peux pas le visiter
        """

        agency: Agency = Agency([agent], [appartment])
        mocker.patch.object(Appartment, "is_empty", return_value=True)
        mocker.patch.object(Tenant, "can_rent", return_value=True)
        mocker.patch.object(Tenant, "have_required_paycheck_amount", return_value=True)
        mocker.patch.object(Agent, "can_visit", return_value=True)
        assert agency.can_visit(datetime(2021, 1, 1), appartment, tenant)

    def test_can_visit_appartment_not_empty(
        self,
        mocker: MockerFixture,
        agent: Agent,
        appartment: Appartment,
        tenant: Tenant,
    ) -> None:
        """Etant donné que l'agence a un agent disponible à la date demandée
        Et que l'appartement n'est pas vide
        Et que le locataire peut louer
        Et que le locataire a un nombre de bulletins de salaire suffisant
        Lorsque je veux visiter l'appartement
        Alors je ne peux pas le visiter
        """

        agency: Agency = Agency([agent], [appartment])
        mocker.patch.object(Appartment, "is_empty", return_value=False)
        mocker.patch.object(Tenant, "can_rent", return_value=True)
        mocker.patch.object(Tenant, "have_required_paycheck_amount", return_value=True)
        mocker.patch.object(Agent, "can_visit", return_value=True)
        assert not agency.can_visit(datetime(2021, 1, 1), appartment, tenant)

    def test_can_visit_tenant_cannot_rent(
        self,
        mocker: MockerFixture,
        agent: Agent,
        appartment: Appartment,
        tenant: Tenant,
    ) -> None:
        """Etant donné que l'agence a un agent disponible à la date demandée
        Et que l'appartement est vide
        Et que le locataire ne peut pas louer
        Et que le locataire a un nombre de bulletins de salaire suffisant
        Lorsque je veux visiter l'appartement
        Alors je ne peux pas le visiter
        """

        agency: Agency = Agency([agent], [appartment])
        mocker.patch.object(Appartment, "is_empty", return_value=True)
        mocker.patch.object(Tenant, "can_rent", return_value=False)
        mocker.patch.object(Tenant, "have_required_paycheck_amount", return_value=True)
        mocker.patch.object(Agent, "can_visit", return_value=True)
        assert not agency.can_visit(datetime(2021, 1, 1), appartment, tenant)

    def test_can_visit_tenant_not_enough_paycheck(
        self,
        mocker: MockerFixture,
        agent: Agent,
        appartment: Appartment,
        tenant: Tenant,
    ) -> None:
        """Etant donné que l'agence a un agent disponible à la date demandée
        Et que l'appartement est vide
        Et que le locataire peut louer
        Et que le locataire n'a pas un nombre de bulletins de salaire suffisant
        Lorsque je veux visiter l'appartement
        Alors je ne peux pas le visiter
        """

        agency: Agency = Agency([agent], [appartment])
        mocker.patch.object(Appartment, "is_empty", return_value=True)
        mocker.patch.object(Tenant, "can_rent", return_value=True)
        mocker.patch.object(Tenant, "have_required_paycheck_amount", return_value=False)
        mocker.patch.object(Agent, "can_visit", return_value=True)
        assert not agency.can_visit(datetime(2021, 1, 1), appartment, tenant)

    def test_can_visit_agent_unavailable(
        self,
        mocker: MockerFixture,
        agent: Agent,
        appartment: Appartment,
        tenant: Tenant,
    ) -> None:
        """Etant donné que l'agence a un agent indisponible à la date demandée
        Et que l'appartement est vide
        Et que le locataire peut louer
        Et que le locataire a un nombre de bulletins de salaire suffisant
        Lorsque je veux visiter l'appartement
        Alors je ne peux pas le visiter
        """

        agency: Agency = Agency([agent], [appartment])
        mocker.patch.object(Appartment, "is_empty", return_value=True)
        mocker.patch.object(Tenant, "can_rent", return_value=True)
        mocker.patch.object(Tenant, "have_required_paycheck_amount", return_value=True)
        mocker.patch.object(Agent, "can_visit", return_value=False)
        assert not agency.can_visit(datetime(2021, 1, 1), appartment, tenant)
