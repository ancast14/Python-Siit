import random
import os
import csv
import json

#from uuid import uuid4

if __name__ == "__main__":

    json_dir = "json_data"

    split_column = "Brand"

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    for filename in os.listdir(json_dir):
        os.remove(os.path.join(json_dir, filename))

    with open("input.csv") as csv_input:
        reader = csv.DictReader(csv_input)

        brands = {}

        for row in reader:
            brand = row[split_column]
            if brand not in brands:
                brands[brand] = []
            brands[brand].append(row)

    for brand, data in brands.items():
        output_filename = "json_data//" + brand + ".json"

        with open(output_filename, "w") as brands_file:
            json.dump(data, brands_file, indent=4)

    with open("input.csv") as csv_input:
        reader = csv.DictReader(csv_input)
        cars = list(reader)

        for car in cars:
            #unique_id = str(uuid4())
            #result = [dict(item, **{"ID":unique_id}) for item in cars]
            unique_id = random.sample((range(0, len(cars))), len(cars))
            for d, v in zip (cars, unique_id):
                d["ID"] = v

        slow_cars_data = [elem for elem in cars if int(elem["Hp"]) < 120]
        fast_cars_data = [elem for elem in cars if 120 <= int(elem["Hp"]) < 180]
        sport_cars_data = [elem for elem in cars if int(elem["Hp"]) >= 180]

        cheap_cars_data = [elem for elem in cars if int(elem["Price"]) < 1000]
        medium_cars_data = [elem for elem in cars if 1000 <= int(elem["Price"]) < 5000]
        expensive_cars_data = [elem for elem in cars if int(elem["Price"]) >= 5000]

    if slow_cars_data:
        with open("json_data//slow_cars.json", "w") as slow_cars:
            json.dump(slow_cars_data, slow_cars, indent=4)

    if fast_cars_data:
        with open("json_data//fast_cars.json", "w") as fast_cars:
            json.dump(fast_cars_data, fast_cars, indent=4)

    if sport_cars_data:
        with open("json_data//sport_cars.json", "w") as sport_cars:
            json.dump(sport_cars_data, sport_cars, indent=4)

    if cheap_cars_data:
        with open("json_data//cheap_cars.json", "w") as cheap_cars:
            json.dump(cheap_cars_data, cheap_cars, indent=4)

    if medium_cars_data:
        with open("json_data//medium_cars.json", "w") as medium_cars:
            json.dump(medium_cars_data, medium_cars, indent=4)

    if expensive_cars_data:
        with open("json_data//expensive_cars.json", "w") as expensive_cars:
            json.dump(expensive_cars_data, expensive_cars, indent=4)