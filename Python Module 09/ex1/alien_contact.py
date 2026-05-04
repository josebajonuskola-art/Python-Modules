from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):

    RADIO = "radio"
    PHYSICAL = "physical"
    VISUAL = "visual"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def alien_contact_validator(self) -> 'AlienContact':

        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID should start with "AC" characters')

        if (
            self.contact_type == ContactType.PHYSICAL
            and self.is_verified is False
        ):
            raise ValueError("Physical contact must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC and
            self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if (
            self.signal_strength > 7.0 and
            not self.message_received
        ):
            raise ValueError("Strong signals should include "
                             "a received message")

        return self


def create_valid_alien() -> AlienContact:

    return AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 1, 10, 0, 0),
        location="Urduliz 42",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from juskola-",
    )


def create_invalid_alien() -> AlienContact:

    return AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 1, 10, 0, 0),
        location="Urduliz 42",
        contact_type=ContactType.TELEPATHIC,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=2,
        message_received="Greetings from juskola-",
    )


def info_printer(info) -> None:

    print(f"ID: {info.contact_id}")
    print(f"Type: {info.contact_type.value}")
    print(f"Location: {info.location}")
    print(f"Signal: {info.signal_strength}/10")
    print(f"Duration: {info.duration_minutes} minutes")
    print(f"Witnesses: {info.witness_count}")

    if info.message_received:
        print(f"Message: '{info.message_received}'")


def main() -> None:

    print("Alien Contact Log Validation")
    print("======================================")

    contacts = [create_valid_alien, create_invalid_alien]

    i = 0
    for contact in contacts:

        try:
            actual_contact = contact()
            print("Valid contact report:")
            info_printer(actual_contact)

            if i < len(contacts) - 1:
                print("\n======================================")

        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"].replace("Value error, ", ""))

        i += 1


if __name__ == "__main__":

    main()
