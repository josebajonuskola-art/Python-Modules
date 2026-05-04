from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def spatial_info_printer(data_to_print) -> None:

    if data_to_print.is_operational:
        op = "Operational"
    else:
        op = "Not operative"

    print(f"ID: {data_to_print.station_id}")
    print(f"Name: {data_to_print.name}")
    print(f"Crew: {data_to_print.crew_size} people")
    print(f"Power: {data_to_print.power_level}%")
    print(f"Oxygen: {data_to_print.oxygen_level}%")
    print(f"Status: {op}\n")


def create_valid_station() -> SpaceStation:

    return SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 1, 10, 0, 0),
        is_operational=True,
        notes=None
    )


def create_invalid_station() -> SpaceStation:

    return SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=34,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 1, 10, 0, 0),
        is_operational=True,
        notes=None
    )


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")

    datas = [create_valid_station, create_invalid_station]

    i = 0
    for data in datas:

        try:
            station = data()
            print("Valid station created:")
            spatial_info_printer(station)

            if i < len(datas) - 1:
                print("========================================")

        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])

        i += 1


if __name__ == "__main__":

    main()
