from abc import ABC, abstractmethod
from typing import Any


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

    def output(self) -> tuple[int, str]:
        if self.processed_data:
            new_index = int(self.index)
            new_content = str(self.processed_data.pop(0))
            self.index += 1
            return new_index, new_content
        else:
            raise Exception("Not possible to return a output, there is "
                            "no processed data ...")


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


def data_processor() -> None:
    print("=== Code Nexus - Data Processor ===\n")

# Numeric Processor
    print("Testing Numeric Processor...")

    numeric_test_obj_1 = NumericProcessor()

    print(f"Trying to validate input '42': {numeric_test_obj_1.validate(42)}")
    print("Trying to validate input 'Hello': "
          f"{numeric_test_obj_1.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        numeric_test_obj_1.ingest('foo')

    except Exception as e:
        print(f"{e}")

    number_list = [1, 2, 3, 4, 5]
    print(f"Processing data: {number_list}")
    numeric_test_obj_1.ingest(number_list)

    print("Extracting 3 values ...")

    for i in range(3):
        try:
            num_test = (numeric_test_obj_1.output())
            print(f"Numeric value {num_test[0]}:", end='')
            print(f" {num_test[1]}")

        except Exception:
            print("Validate the inputs before ingesting them...")
    print("\n\n")

# Text Processor
    print("Testing Text Processor...")

    textual_test_obj_1 = TextProcessor()
    print(f"Trying to validate input '42': {textual_test_obj_1.validate(42)}")

    text_list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_list}")
    textual_test_obj_1.ingest(text_list)
    print("Extracting 1 values ...")

    for i in range(1):
        try:
            test_text = textual_test_obj_1.output()
            print(f"Text value "
                  f"{test_text[0]}:", end='')
            print(f" {test_text[1]}")

        except Exception:
            print("Validate the inputs before ingesting them ...")
    print("\n\n")

# Log Processor
    print("Testing Log Processor...")

    log_test_obj_1 = LogProcessor()
    print(f"Trying to validate input 'Hello': "
          f"{log_test_obj_1.validate('Hello')}")

    log_list = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {log_list}")
    log_test_obj_1.ingest(log_list)
    print("Extracting 2 values ...")

    for i in range(2):
        try:
            test_dictionary = log_test_obj_1.output()
            print(f"Log entry "
                  f"{test_dictionary[0]}:", end='')
            print(f" {test_dictionary[1]}")

        except Exception:
            print("Validate the inputs before ingesting them ...")


if __name__ == "__main__":
    data_processor()
