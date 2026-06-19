import time
import matplotlib.pyplot as plt

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

    # Data untuk grafik

    labels = []

    execution_times = []

    fuel_costs = []

    tco_values = []

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

        tco_greedy = calculate_tco(
            fuel_cost_greedy,
            server_cost_greedy
        )

        print("\nGREEDY RESULT")

        print("\nRoute:")

        for i in range(len(route)):
            print(locations[route[i]]["name"], end="")

            if i != len(route)-1:
                print(" -> ", end="")

        print()

        print("\nTotal Distance:")
        print(total_distance, "km")

        print("\nExecution Time:")
        print(f"{execution_time:.8f} sec")

        print("\nFuel Used:")
        print(f"{fuel_used_greedy:.4f} liter")

        print("\nFuel Cost:")
        print(f"Rp {fuel_cost_greedy:,.2f}")

        print("\nServer Cost:")
        print(f"Rp {server_cost_greedy:,.2f}")

        print("\nTCO:")
        print(f"Rp {tco_greedy:,.2f}")

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

        # Simpan data untuk grafik

        labels.append(
            f"Greedy\n{scenario['name']}"
        )

        execution_times.append(
            execution_time
        )

        fuel_costs.append(
            fuel_cost_greedy
        )

        tco_values.append(
            tco_greedy
        )

        labels.append(
            f"Exact\n{scenario['name']}"
        )

        execution_times.append(
            exact_execution_time
        )

        fuel_costs.append(
            fuel_cost_exact
        )

        tco_values.append(
            tco_exact
        )

        print("\nEXACT RESULT")

        print("\nRoute:")

        for i in range(len(route_exact)):
            print(locations[route_exact[i]]["name"], end="")

            if i != len(route_exact)-1:
                print(" -> ", end="")

        print()

        print("\nTotal Distance:")
        print(distance_exact, "km")

        print("\nExecution Time:")
        print(f"{exact_execution_time: .8f} sec")

        print("\nFuel Used:")
        print(f"{fuel_used_exact:.4f} liter")

        print("\nFuel Cost:")
        print(f"Rp {fuel_cost_exact:,.2f}")

        print("\nServer Cost:")
        print(f"Rp {server_cost_exact:,.2f}")

        print("\nTCO:")
        print(f"Rp {tco_exact:,.2f}")

        print("\n===========================")
        print("PERBANDINGAN")
        print("===========================")

        print(f"Greedy TCO : Rp {tco_greedy:,.2f}")
        print(f"Exact TCO  : Rp {tco_exact:,.2f}")

        if tco_greedy < tco_exact:
            print("\nRekomendasi: Gunakan Greedy")
        else:
            print("\nRekomendasi: Gunakan Exact")

    # GRAFIK EXECUTION TIME

    plt.figure(figsize=(8,5))

    plt.bar(labels, execution_times)

    plt.title("Execution Time Comparison")

    plt.ylabel("Time (seconds)")

    plt.tight_layout()

    plt.savefig(
        "docs/execution_time.png"
    )

    plt.close()

    # GRAFIK FUEL COST

    plt.figure(figsize=(8,5))

    plt.bar(labels, fuel_costs)

    plt.title("Fuel Cost Comparison")

    plt.ylabel("Fuel Cost (Rp)")

    plt.tight_layout()

    plt.savefig(
        "docs/fuel_cost.png"
    )

    plt.close()

    # GRAFIK TCO

    plt.figure(figsize=(8,5))

    plt.bar(labels, tco_values)

    plt.title(
        "Total Cost of Ownership Comparison"
    )

    plt.ylabel("TCO (Rp)")

    plt.tight_layout()

    plt.savefig(
        "docs/tco.png"
    )

    plt.close()

    print(
        "\nSemua grafik berhasil disimpan di folder docs/"
    )

if __name__ == "__main__":
    main()