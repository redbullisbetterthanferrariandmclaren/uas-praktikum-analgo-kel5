def calculate_fuel_cost(
    route,
    distance_matrix,
    locations,
    fuel_price
):
    # Menghitung total berat paket awal
    initial_weight = 0

    for location in locations:
        initial_weight += location["weight"]

    # Berat paket saat kurir mulai berangkat
    current_weight = initial_weight

    # Total konsumsi bahan bakar
    total_fuel_used = 0

    # Menghitung konsumsi BBM pada setiap perjalanan antar node
    for i in range(len(route) - 1):
        from_node = route[i]
        to_node = route[i + 1]
        distance = distance_matrix[from_node][to_node]

        # Semakin berat beban, semakin besar rasio konsumsi BBM
        fuel_ratio = (
            0.02
            + 0.03 *
            (current_weight / initial_weight)
        )

        fuel_used = distance * fuel_ratio
        total_fuel_used += fuel_used

        # Mengurangi berat paket setelah paket dikirim
        if to_node != 0:
            current_weight -= locations[to_node]["weight"]

    # Menghitung biaya BBM berdasarkan total konsumsi
    fuel_cost = total_fuel_used * fuel_price

    return total_fuel_used, fuel_cost

# Menghitung biaya komputasi server berdasarkan waktu eksekusi
def calculate_server_cost(execution_time):
    return execution_time * 50

# Menghitung Total Cost of Ownership (TCO)
def calculate_tco(fuel_cost, server_cost):
    return fuel_cost + server_cost