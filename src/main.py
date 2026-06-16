from loader import (
    load_locations,
    load_distance_matrix,
    load_scenario
)

from cost import (
    calculate_fuel_cost,
    calculate_server_cost,
    calculate_tco
)

from heuristic import greedy_tsp
import time
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

        start_time = time.perf_counter()

        route, total_distance = greedy_tsp(distance_matrix)

        end_time = time.perf_counter()

        execution_time = (end_time-start_time)

        fuel_used_greedy, fuel_cost_greedy = (
            calculate_fuel_cost(
                route,
                distance_matrix,
                locations,
                scenario["fuel_price"]
            )
        )

        server_cost_greedy = calculate_server_cost(
            execution_time
        )

        tco_cost_greedy = calculate_tco(
            fuel_cost_greedy,
            server_cost_greedy
        )

        print("\nGREEDY RESULT")

        print("Route (ID):")
        print(route)

        print("\nTotal Distance:")
        print(total_distance, "km")

        print("\nExecution Time:")
        print(f"{execution_time:.8f} sec")

        print("\nFuel Used:")
        print(f"{fuel_used_greedy:.4f} liter")

        print("\nFuel Cost:")
        print(f"Rp {fuel_cost_greedy:,.2f}")


        # Menjalankan Dynamic Programming (Exact)

        start_time = time.perf_counter()

        route_exact, distance_exact = held_karp_tsp(distance_matrix)

        end_time = time.perf_counter()
        exact_execution_time = (end_time - start_time)

        fuel_used_exact, fuel_cost_exact = (
            calculate_fuel_cost(
                route_exact,
                distance_matrix,
                locations,
                scenario["fuel_price"]
            )
        )   

        server_cost_exact = calculate_server_cost(
            exact_execution_time
        )

        tco_exact = calculate_tco(
            fuel_cost_exact,
            server_cost_exact
        )

        print("\nEXACT RESULT")

        print("Route (ID):")
        print(route_exact)

        print("\nTotal Distance:")
        print(distance_exact, "km")

        print("\nExecution Time:")
        print(f"{exact_execution_time: .8f} sec")

        print("\nFuel Used:")
        print(f"{fuel_used_exact:.4f} liter")

        print("\nFuel Cost:")
        print(f"Rp {fuel_cost_exact:,.2f}")

if __name__ == "__main__":
    main()