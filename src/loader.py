import csv
import json

# Membaca data lokasi #
def load_locations(filename):
    locations = []

    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            locations.append({
                "id": int(row["id"]),
                "name": row["locations"],
                "weight": float(row["weight (kg)"])
            })

    return locations


# Membaca matriks jarak #
def load_distance_matrix(filename):
    matrix = []

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Lewati header pertama
        next(reader)

        for row in reader:
            # Ambil mulai kolom kedua (skip ID)
            matrix.append([float(x) for x in row[1:]])

    return matrix


# Membaca skenario ekonomi #
def load_scenario(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)