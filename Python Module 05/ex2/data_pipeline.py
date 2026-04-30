from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.processed_data: list[Any] = []
        self.index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, nb: int) -> list[tuple[int, str]]:
        result: list[tuple[int, str]] = []
        for i in range(nb):
            if self.processed_data:
                new_index = int(self.index)
                new_content = str(self.processed_data.pop(0))
                self.index += 1
                tuple1 = (new_index, new_content)
                result.append(tuple1)
        return result


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)):
            return True

        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True

        else:
            return False

    def ingest(self, data: list[float] | list[int] | float | int) -> None:

        if self.validate(data) is True:
            if isinstance(data, list):
                for element in data:
                    self.processed_data.append(element)
            else:
                self.processed_data.append(data)

        else:
            raise Exception("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True

        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True

        else:
            return False

    def ingest(self, data: list[str] | str) -> None:

        if self.validate(data) is True:
            if isinstance(data, list):
                for element in data:
                    self.processed_data.append(element)
            else:
                self.processed_data.append(data)

        else:
            raise Exception("Got exception: Improper text data")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
            return True

        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, (dict)):
                    return False
                for key, value in element.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
            return True

        else:
            return False

    def ingest(self, data: list[dict[str, str]] | dict[str, str]) -> None:

        if not self.validate(data):
            raise Exception("Got exception: Improper log data")

        if isinstance(data, dict):
            values = list(data.values())
            self.processed_data.append(f"{values[0]}: {values[1]}")

        elif isinstance(data, list):
            for item in data:
                values = list(item.values())
                self.processed_data.append(f"{values[0]}: {values[1]}")


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        first = True
        for element in data:
            if not first:
                print(",", end='')
            first = False
            print(f"{element[1]}", end='')
        print("")


class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        first = True
        print("{", end='')
        for element in data:
            if not first:
                print(", ", end='')
            first = False
            print(f'"item_{element[0]}": "{element[1]}"', end='')
        print("}", end='')
        print("")


class DataStream():

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        for process in self.processors:
            if type(process) is type(proc):
                print(f"{type(proc).__name__} has already been registered")
                return

        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            process_ok = False

            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    process_ok = True
                    break

            if process_ok is False:
                print(f"DataStream error - Can't process element in "
                      f"stream: {element}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data\n")

        for processor in self.processors:
            processed = len(processor.processed_data) + processor.index
            remaining = len(processor.processed_data)

            name = type(processor).__name__.replace("Processor", " Processor")

            print(f"{name}: total {processed} items processed, remaining "
                  f"{remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data = processor.output(nb)
            plugin.process_output(data)


def data_pipeline() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream ...")

    ds = DataStream()
    ds.print_processors_stats()

    print("Registering processors\n")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! "
             "Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
                ]
    print(f"Send first batch of data on stream: {stream}")
    ds.process_stream(stream)

    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVPlugin())

    ds.print_processors_stats()

    stream2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires"
             " in 10 days"}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
            ]
    print(f"Send another batch of data: {stream2}")
    ds.process_stream(stream2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONPlugin())

    ds.print_processors_stats()


if __name__ == "__main__":
    data_pipeline()
