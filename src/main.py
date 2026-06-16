from loader import (
    load_locations,
    load_distance_matrix,
    load_scenario
)

from heuristic import greedy_tsp
from exact import held_karp_tsp

def main():
    # Load seluruh dataset #
    locations = load_locations(
        "data/locations_dataset.csv"
    )

    distance_matrix = load_distance_matrix(
        "data/distance_matrix_dataset.csv"
    )

    scenario_data = load_scenario(
        "data/scenario.json"
    )

    # Menampilkan data #
    print("\nDATA BERHASIL DIINPUT\n")

    print("DATA LOKASI")
    for location in locations:
        print(location)

    print("\nDISTANCE MATRIX")
    for row in distance_matrix:
        print(row)

    print("\nSCENARIO EKONOMI")

    for scenario in scenario_data["scenarios"]:
        print(
            f"{scenario['name']} - "
            f"Harga BBM: Rp {scenario['fuel_price']}/liter"
        )

    # Menjalankan Greedy #

    route, total_distance = greedy_tsp(distance_matrix)

    print("\nGREEDY RESULT")

    print("Route (ID):")
    print(route)

    print("\nTotal Distance:")
    print(total_distance, "km")


    # Menjalankan Dynamic Programming (Exact)

    route_exact, distance_exact = held_karp_tsp(distance_matrix)

    print("\nEXACT RESULT")

    print("Route (ID):")
    print(route_exact)

    print("\nTotal Distance:")
    print(distance_exact, "km")

if __name__ == "__main__":
    main()