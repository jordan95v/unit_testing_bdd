from datetime import datetime
import pytest
from core.models.address import Address
from core.models.appartment import Appartment
from core.models.paycheck import Paycheck
from core.models.tenant import Tenant


@pytest.fixture
def tenant() -> Tenant:
    return Tenant(
        "romain@gmail.com",
        "Romain",
        "Lancelot",
        datetime(2000, 2, 28),
        "AWS Enjoyer",
        [Paycheck(datetime(2021, 1, 1), "SACEM")],
    )


@pytest.fixture
def appartment() -> Appartment:
    return Appartment(Address("10 Rue de Jordanie", 60000, "Lyon"), None, None)
