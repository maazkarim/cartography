import json
import logging

from typing import Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MyStats:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.stats = {}
        return cls._instance

    def add_stat(self, service: str, stat_heading: str, stat: Any) -> None:
        if service not in self.stats:
            self.stats[service] = {}
        if "errors" not in self.stats[service]:
            self.stats[service]["errors"] = set()
        if "skipped regions" not in self.stats[service]:
            self.stats[service]["skipped regions"] = set()
        if stat_heading == "errors":
            self.stats[service][stat_heading].add(stat)
        elif stat_heading == "skipped regions":
            self.stats[service][stat_heading].add(stat)
        else:
            self.stats[service][stat_heading] = stat

    def export_stats(self, file_path: str) -> None:
        """
        Exports the stats dictionary to a JSON file.

        :param file_path: The path to the file where the JSON should be saved.
        """

        for service in self.stats:
            self.stats[service]["errors"] = list(self.stats[service]["errors"])
            self.stats[service]["skipped regions"] = list(self.stats[service]["skipped regions"])
        logger.info("Exporting stats for All AWS modules")

        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.stats, json_file, indent=4)
            logger.info(f"Stats successfully exported to {file_path}")
        except Exception as e:
            logger.warning(f"An error occurred while exporting stats: {e}")

    def export_service_stats(self, file_path: str, service: str) -> None:
        """
        Exports the stats for a specific service to a JSON file.

        :param file_path: The path to the file where the JSON should be saved.
        """
        # print(service)
        self.stats[service]["errors"] = list(self.stats[service]["errors"])
        self.stats[service]["skipped regions"] = list(self.stats[service]["skipped regions"])
        # print(self.stats[service])
        logger.info(f"Exporting stats for AWS {service}")
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.stats[service], json_file, indent=4)
            logger.info(f"Stats successfully exported to {file_path}")
        except Exception as e:
            logger.warning(f"An error occurred while exporting stats: {e}")


# Testing before getting credentials
if __name__ == "__main__":
    stats = MyStats()
    stats.add_stat("S3", "Time Taken", "5 sec")
    stats.export_stats("log_check.json")
