from datetime import datetime
from core.models.appartment import Appartment
from core.models.tenant import Tenant


class TestAppartment:
    def test_is_empty(self, appartment: Appartment) -> None:
        """Etant donnée un appartement vide
        Lorsque je vérifie si il est vide
        Alors il est vide
        """

        assert appartment.is_empty() is True

    def test_is_not_empty(self, appartment: Appartment, tenant: Tenant) -> None:
        """Etant donnée un appartement non vide
        Lorsque je vérifie si il est vide
        Alors il n'est pas vide
        """
        appartment.tenant = tenant
        assert appartment.is_empty() is False

    def test_is_empty_soon(self, appartment: Appartment) -> None:
        """Etant donnée un appartement non vide
        Et que son locataire part bientôt
        Lorsque je vérifie si il est vide bientôt
        Alors il est vide bientôt
        """

        appartment.tenant_exit_day = datetime(2021, 1, 1)
        assert appartment.is_empty_soon() is True

    def test_is_not_empty_soon(self, appartment: Appartment) -> None:
        """Etant donnée un appartement non vide
        Et que son locataire ne part pas
        Lorsque je vérifie si il est vide bientôt
        Alors il n'est pas vide bientôt
        """

        appartment.tenant_exit_day = None
        assert appartment.is_empty_soon() is False
