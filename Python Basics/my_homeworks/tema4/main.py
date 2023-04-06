import shutil
import os
import csv
import json
from uuid import uuid4

if __name__ == "__main__":
    json_dir = "json_data"
    split_column = "Brand"

    if os.path.exists(json_dir):
        shutil.rmtree(json_dir)

    os.makedirs(json_dir)

    cars = []
    with open("input.csv") as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            unique_id = str(uuid4())
            row["ID"] = unique_id
            cars.append(row)

    brands = {}
    for row in cars:
        brand = row[split_column]
        if brand not in brands:
            brands[brand] = []
        brands[brand].append(row)

    slow_cars_data = [elem for elem in cars if int(elem["Hp"]) < 120]
    fast_cars_data = [elem for elem in cars if 120 <= int(elem["Hp"]) < 180]
    sport_cars_data = [elem for elem in cars if int(elem["Hp"]) >= 180]

    cheap_cars_data = [elem for elem in cars if int(elem["Price"]) < 1000]
    medium_cars_data = [elem for elem in cars if 1000 <= int(elem["Price"]) < 5000]
    expensive_cars_data = [elem for elem in cars if int(elem["Price"]) >= 5000]

    for brand, data in brands.items():
        output_filename = os.path.join(json_dir, f"{brand}.json")
        with open(output_filename, "w") as brands_file:
            json.dump(data, brands_file, indent=4)

    if slow_cars_data:
        with open(os.path.join(json_dir, "slow_cars.json"), "w") as slow_cars:
            json.dump(slow_cars_data, slow_cars, indent=4)

    if fast_cars_data:
        with open(os.path.join(json_dir, "fast_cars.json"), "w") as fast_cars:
            json.dump(fast_cars_data, fast_cars, indent=4)

    if sport_cars_data:
        with open(os.path.join(json_dir, "sport_cars.json"), "w") as sport_cars:
            json.dump(sport_cars_data, sport_cars, indent=4)

    if cheap_cars_data:
        with open(os.path.join(json_dir, "cheap_cars.json"), "w") as cheap_cars:
            json.dump(cheap_cars_data, cheap_cars, indent=4)

    if medium_cars_data:
        with open(os.path.join(json_dir, "medium_cars.json"), "w") as medium_cars:
            json.dump(medium_cars_data, medium_cars, indent=4)

    if expensive_cars_data:
        with open(os.path.join(json_dir, "expensive_cars.json"), "w") as expensive_cars:
            json.dump(expensive_cars_data, expensive_cars, indent=4)