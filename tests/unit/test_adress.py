from core.models.address import Address


class TestAdress:
    def test_address_is_valid(self) -> None:
        """Etant donnée que la voie de l'adresse est "1 Rue de la Paix"
        Et que le code postal est "75000"
        Et que la ville est "Paris"
        Quand je vérifie si l'adresse est valide
        Alors l'adresse est valide
        """

        address: Address = Address("1 Rue de la Paix", 75000, "Paris")
        assert address.is_valid() is True

    def test_address_city_is_empty(self) -> None:
        """Etant donnée que la voie de l'adresse est "1 Rue de la Paix"
        Et que le code postal est "75000"
        Et que la ville est vide
        Quand je vérifie si l'adresse est valide
        Alors l'adresse n'est pas valide
        """

        address: Address = Address("1 Rue de la Paix", 75000, None)
        assert address.is_valid() is False

    def test_way_code_is_empty(self) -> None:
        """Etant donnée que la voie de l'adresse est "1 Rue de la Paix"
        Et que le code postal est vide
        Et que la ville est "Paris"
        Quand je vérifie si l'adresse est valide
        Alors l'adresse n'est pas valide
        """

        address: Address = Address("1 Rue de la Paix", None, "Paris")
        assert address.is_valid() is False

    def test_address_street_is_empty(self) -> None:
        """Etant donnée que la voie de l'adresse est vide
        Et que le code postal est "75000"
        Et que la ville est "Paris"
        Quand je vérifie si l'adresse est valide
        Alors l'adresse n'est pas valide
        """

        address: Address = Address(None, 75000, "Paris")
        assert address.is_valid() is False

    def test_address_is_in_city(self) -> None:
        """Etant donnée que la voie de l'adresse est "1 Rue de la Paix"
        Et que le code postal est "75000"
        Et que la ville est "Paris"
        Quand je vérifie si l'adresse est dans la ville "Paris"
        Alors l'adresse est dans la ville "Paris"
        """

        address: Address = Address("1 Rue de la Paix", 75000, "Paris")
        assert address.is_in_city("Paris") is True

    def test_address_is_not_in_city(self) -> None:
        """Etant donnée que la voie de l'adresse est "1 Rue de la Paix"
        Et que le code postal est "75000"
        Et que la ville est "Paris"
        Quand je vérifie si l'adresse est dans la ville "Lyon"
        Alors l'adresse n'est pas dans la ville "Lyon"
        """

        address: Address = Address("1 Rue de la Paix", 75000, "Paris")
        assert address.is_in_city("Lyon") is False
