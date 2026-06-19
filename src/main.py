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
    ## Memuat Seluruh Dataset ##
    locations = load_locations("data/locations_dataset.csv")
    distance_matrix = load_distance_matrix("data/distance_matrix_dataset.csv")
    scenario_data = load_scenario("data/scenario.json")

    ## Menampilkan Data Input ##
    print("\nI. DATA INPUT\n")

    print("Locations Dataset:")
    for location in locations:
        print(location)

    print("\nDistance Matrix Dataset:")
    for row in distance_matrix:
        print(row)

    print("\n\nII. ALGORITHMS SIMULATION")

    ## MENYIMPAN DATA UNTUK GRAFIK Menyimpan Data untuk Grafik ##
    labels = []
    execution_times = []
    fuel_costs = []
    tco_values = []

    ## Simulasi Setiap Skenario ##
    for i, scenario in enumerate(
        scenario_data["scenarios"],
        start=1
    ):
        print(
            f"\n\n{i}. {scenario['name']} - "
            f"Harga BBM: Rp {scenario['fuel_price']}/liter"
        )


        ### ALGORITMA GREEDY ###
        start_time = time.perf_counter()
        route, total_distance = greedy_tsp(distance_matrix)
        end_time = time.perf_counter()
        execution_time = (end_time-start_time)

        # Menghitung Fuel Cost
        fuel_used_greedy, fuel_cost_greedy = (
            calculate_fuel_cost(
                route,
                distance_matrix,
                locations,
                scenario["fuel_price"]
            )
        )

        # Menghitung Server Cost
        server_cost_greedy = calculate_server_cost(execution_time)

        # Menghitung Total Cost of Ownership
        tco_greedy = calculate_tco(fuel_cost_greedy, server_cost_greedy)

        print(f"\n\n{i}a. Basic Heuristic Algorithm (Greedy NN)")
        print("\nRoute:")

        for j in range(len(route)):
            print(locations[route[j]]["name"], end="")

            if j != len(route)-1:
                print(" -> ", end="")
        
        print("\n\n- Performance Metrics -")
        print("Total Distance:", total_distance, "km")
        print("Execution Time:", f"{execution_time:.8f} sec")
        print("Fuel Used:", f"{fuel_used_greedy:.4f} liter")

        print("\n- Cost Breakdown -")
        print("Fuel Cost:", f"Rp {fuel_cost_greedy:,.2f}")
        print("Server Cost:", f"Rp {server_cost_greedy:,.2f}")
        print("TCO:", f"Rp {tco_greedy:,.2f}")


        ### ALGORITMA EXACT (HELD-KARP DP) ###
        start_time = time.perf_counter()
        route_exact, distance_exact = held_karp_tsp(distance_matrix)
        end_time = time.perf_counter()
        exact_execution_time = (end_time - start_time)

        # Menghitung Fuel Cost
        fuel_used_exact, fuel_cost_exact = (
            calculate_fuel_cost(
                route_exact,
                distance_matrix,
                locations,
                scenario["fuel_price"]
            )
        )   

        # Menghitung Server Cost
        server_cost_exact = calculate_server_cost(exact_execution_time)

        # Menghitung Total Cost of Ownership
        tco_exact = calculate_tco(fuel_cost_exact, server_cost_exact)

        # Menyimpan data untuk grafik
        labels.append(f"Greedy\n{scenario['name']}")
        execution_times.append(execution_time)
        fuel_costs.append(fuel_cost_greedy)
        tco_values.append(tco_greedy)
        labels.append(f"Exact\n{scenario['name']}")
        execution_times.append(exact_execution_time)
        fuel_costs.append(fuel_cost_exact)
        tco_values.append(tco_exact)

        print(f"\n\n{i}b. Algoritma Eksak (Held-Karp DP)")
        print("\nRoute:")

        for j in range(len(route_exact)):
            print(locations[route_exact[j]]["name"], end="")

            if j != len(route_exact)-1:
                print(" -> ", end="")

        print("\n\n- Performance Metrics -")
        print("Total Distance:", distance_exact, "km")
        print("Execution Time:", f"{exact_execution_time: .8f} sec")
        print("Fuel Used:", f"{fuel_used_exact:.4f} liter")

        print("\n- Cost Breakdown -")
        print("Fuel Cost:", f"Rp {fuel_cost_exact:,.2f}")
        print("Server Cost:", f"Rp {server_cost_exact:,.2f}")
        print("TCO:", f"Rp {tco_exact:,.2f}")

        print("\n\n--- PERBANDINGAN ---")
        print(f"Heuristic TCO: Rp {tco_greedy:,.2f}")
        print(f"Exact TCO: Rp {tco_exact:,.2f}")

        print("\nRecommendation:")
        if tco_greedy < tco_exact:
            print("Use Heuristic")
        elif tco_greedy > tco_exact:
            print("Use Exact")
        else:
            print("Use Anything You Want")


    ### VISUALISASI GRAFIK PERBANDINGAN EXECUTION TIME ###
    plt.figure(figsize=(8,5))
    plt.bar(labels, execution_times)
    plt.title("Execution Time Comparison")
    plt.ylabel("Time (seconds)")
    plt.tight_layout()
    plt.savefig("docs/execution_time.png")
    plt.close()


    ### VISUALISASI GRAFIK PERBANDINGAN FUEL COST ###
    plt.figure(figsize=(8,5))
    plt.bar(labels, fuel_costs)
    plt.title("Fuel Cost Comparison")
    plt.ylabel("Fuel Cost (Rp)")
    plt.tight_layout()
    plt.savefig("docs/fuel_cost.png")
    plt.close()

    ### VISUALISASI GRAFIK PERBANDINGAN TCO ###
    plt.figure(figsize=(8,5))
    plt.bar(labels, tco_values)
    plt.title("Total Cost of Ownership Comparison")
    plt.ylabel("TCO (Rp)")
    plt.tight_layout()
    plt.savefig("docs/tco.png")
    plt.close()

    print("\n\nConfirmation:")
    print("All graphic visualizations were successfully saved to the docs/ folder")

if __name__ == "__main__":
    main()