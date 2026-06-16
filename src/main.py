from loader import (
    load_locations,
    load_distance_matrix,
    load_scenario
)

def main():
    # Load seluruh dataset #
    locations = load_locations("../data/locations.csv")

    distance_matrix = load_distance_matrix(
        "../data/distance_matrix.csv"
    )

    scenario_data = load_scenario(
        "../data/scenario.json"
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

    # ==========================
    # Nanti lanjut di sini
    # ==========================

    # for scenario in scenario_data["scenarios"]:
    #
    #     route_greedy = greedy(...)
    #
    #     route_exact = backtracking(...)
    #
    #     fuel_cost = calculate_fuel(...)
    #
    #     server_cost = calculate_server(...)
    #
    #     tco = calculate_tco(...)
    #
    #     print hasil


if __name__ == "__main__":
    main()