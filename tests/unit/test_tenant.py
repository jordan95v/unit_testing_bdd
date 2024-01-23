from datetime import datetime, timedelta
from core.models.paycheck import Paycheck
from core.models.tenant import Tenant


class TestTenant:
    def test_have_required_paycheck_amount(self, tenant: Tenant) -> None:
        """Etant donnée un locataire avec le nombre de fiche de paye requis
        Lorsque je vérifie si il a le nombre de fiche de paye requis
        Alors il a le nombre de fiche de paye requis
        """

        tenant.paychecks = [
            Paycheck(datetime(2021, 1, 1), "SACEM")
        ] * Tenant.NB_PAYCHECK_MONTH
        assert tenant.have_required_paycheck_amount() is True

    def test_have_not_required_paycheck_amount(self, tenant: Tenant) -> None:
        """Etant donnée un locataire sans le nombre de fiche de paye requis
        Lorsque je vérifie si il a le nombre de fiche de paye requis
        Alors il n'a pas le nombre de fiche de paye requis
        """

        tenant.paychecks = [Paycheck(datetime(2021, 1, 1), "SACEM")] * (
            Tenant.NB_PAYCHECK_MONTH - 1
        )
        assert tenant.have_required_paycheck_amount() is False

    def test_rent_ok(self) -> None:
        """Etant donnée un locataire qui a un métier
        Et qui a le bon nomnbre de bulletin de paie
        Et qui a l'age requis
        Lorsque je vérifie si il peut louer
        Alors il peut louer
        """

        tenant: Tenant = Tenant(
            "romain@gmail.com",
            "Romain",
            "Lancelot",
            datetime.now() - timedelta(days=365 * Tenant.MINIMUM_REQUIRED_AGE),
            "AWS Enjoyer",
            [Paycheck(datetime(2021, 1, 1), "SACEM")] * Tenant.NB_PAYCHECK_MONTH,
        )
        assert tenant.can_rent() is True

    def test_rent_not_minimum_age(self) -> None:
        """Etant donnée un locataire qui a un métier
        Et qui a le bon nomnbre de bulletin de paie
        Et qui n'a pas l'age requis
        Lorsque je vérifie si il peut louer
        Alors il ne peut pas louer
        """

        tenant: Tenant = Tenant(
            "romain@gmail.com",
            "Romain",
            "Lancelot",
            datetime.now(),
            "AWS Enjoyer",
            [Paycheck(datetime(2021, 1, 1), "SACEM")] * Tenant.NB_PAYCHECK_MONTH,
        )
        assert tenant.can_rent() is False

    def test_rent_not_enough_paycheck(self) -> None:
        """Etant donnée un locataire qui a un métier
        Et qui n'a pas le bon nomnbre de bulletin de paie
        Et qui a l'age requis
        Lorsque je vérifie si il peut louer
        Alors il ne peut pas louer
        """

        tenant: Tenant = Tenant(
            "romain@gmail.com",
            "Romain",
            "Lancelot",
            datetime.now() - timedelta(days=365 * Tenant.MINIMUM_REQUIRED_AGE),
            "AWS Enjoyer",
            [Paycheck(datetime(2021, 1, 1), "SACEM")] * (Tenant.NB_PAYCHECK_MONTH - 1),
        )
        assert tenant.can_rent() is False

    def test_rent_no_job(self) -> None:
        """Etant donnée un locataire qui n'a pas de métier
        Et qui a le bon nomnbre de bulletin de paie
        Et qui a l'age requis
        Lorsque je vérifie si il peut louer
        Alors il ne peut pas louer
        """

        tenant: Tenant = Tenant(
            "romain@gmail.com",
            "Romain",
            "Lancelot",
            datetime.now() - timedelta(days=365 * Tenant.MINIMUM_REQUIRED_AGE),
            "",
            [Paycheck(datetime(2021, 1, 1), "SACEM")] * (Tenant.NB_PAYCHECK_MONTH - 1),
        )
        assert tenant.can_rent() is False
