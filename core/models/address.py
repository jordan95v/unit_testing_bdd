from dataclasses import dataclass

__all__: list[str] = ["Address"]


@dataclass
class Address:
    way: str | None = None
    postal_code: int | None = None
    city: str | None = None

    def is_valid(self) -> bool:
        """Check if the address is valid.

        Returns:
            True if the address is valid, False otherwise.
        """

        return all([self.way, self.postal_code, self.city])

    def is_in_city(self, city: str) -> bool:
        """Check if the address is in the specified city.

        Args:
            city: The city to check against.

        Returns:
            True if the address is in the specified city, False otherwise.
        """

        return self.city == city
