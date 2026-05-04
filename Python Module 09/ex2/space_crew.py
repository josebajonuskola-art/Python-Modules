from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class CrewRanks(Enum):

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_time: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def space_mission_validator(self) -> "SpaceMission":

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID should start with 'M' character")

        experienced_members = 0
        has_commander = False
        has_captain = False
        for member in self.crew:

            if member.rank == CrewRanks.COMMANDER:
                has_commander = True

            if member.rank == CrewRanks.CAPTAIN:
                has_captain = True

            if member.years_experience > 5:
                experienced_members += 1

            if not member.is_active:
                raise ValueError("All the crew members should be active")

        if not has_commander and not has_captain:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")

        if experienced_members < len(self.crew) / 2:
            raise ValueError("Mission must have at least a 50% "
                             "experienced crew")

        return self


def valid_mission() -> 'SpaceMission':

    sarah_connor = CrewMember(member_id="163A",
                              name="Sarah Connor",
                              rank=CrewRanks.COMMANDER,
                              age=35,
                              specialization="Mission Command",
                              years_experience=15)

    john_smith = CrewMember(member_id="235DF",
                            name="John Smith",
                            rank=CrewRanks.LIEUTENANT,
                            age=35,
                            specialization="Navigation",
                            years_experience=8)

    alice_johnson = CrewMember(member_id="166JK",
                               name="Alice Johnson",
                               rank=CrewRanks.OFFICER,
                               age=49,
                               specialization="Engineering",
                               years_experience=30)

    actual_crew = [sarah_connor, john_smith, alice_johnson]

    return SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 1, 10, 0, 0),
        duration_time=900,
        crew=actual_crew,
        budget_millions=2500.0,
     )


def invalid_mission() -> 'SpaceMission':

    sarah_connor = CrewMember(member_id="163A",
                              name="Sarah Connor",
                              rank=CrewRanks.CADET,
                              age=35,
                              specialization="Mission Command",
                              years_experience=15)

    john_smith = CrewMember(member_id="235DF",
                            name="John Smith",
                            rank=CrewRanks.LIEUTENANT,
                            age=35,
                            specialization="Navigation",
                            years_experience=8)

    alice_johnson = CrewMember(member_id="166JK",
                               name="Alice Johnson",
                               rank=CrewRanks.OFFICER,
                               age=49,
                               specialization="Engineering",
                               years_experience=30)

    actual_crew = [sarah_connor, john_smith, alice_johnson]

    return SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 1, 10, 0, 0),
        duration_time=900,
        crew=actual_crew,
        budget_millions=2500.0,
     )


def mission_printer(mission_to_print) -> None:

    print(f"Mission: {mission_to_print.mission_name}")
    print(f"ID: {mission_to_print.mission_id}")
    print(f"Destination: {mission_to_print.destination}")
    print(f"Duration: {mission_to_print.duration_time} days")
    print(f"Budget:  ${mission_to_print.budget_millions}M")
    print(f"Crew size: {len(mission_to_print.crew)}")
    print("Crew members:")
    for member in mission_to_print.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def main() -> None:

    print("Space Mission Crew Validation")
    print("=========================================")

    missions = [valid_mission, invalid_mission]

    i = 0
    for mission in missions:

        try:
            actual_mission = mission()
            print("Valid mission created:")
            mission_printer(actual_mission)

            if i < len(missions) - 1:
                print("\n=========================================")

        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"].replace("Value error, ", ""))

        i += 1


if __name__ == "__main__":

    main()
