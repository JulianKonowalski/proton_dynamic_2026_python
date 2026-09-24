import DataProcessor as dp

import json
import pathlib

ROOT_PATH     = pathlib.Path(__file__).parent.parent.resolve()
OUTPUT_PATH   = ROOT_PATH.joinpath("resources/output_data.json")
RESOURCE_PATH = ROOT_PATH.joinpath("resources/test_data.txt")

if __name__ == "__main__":
    data_processor = dp.DataProcessor(
        ROOT_PATH.joinpath("resources/test_data.txt").resolve())
    result = data_processor.process()
    with open(str(OUTPUT_PATH), "w+") as output_file:
        output_file.seek(0)
        output_file.truncate()
        json.dump(result, output_file)
