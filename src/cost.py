# cost.py

def calculate_fuel_cost(
    route,
    distance_matrix,
    locations,
    fuel_price
):

    initial_weight = 0

    for location in locations:
        initial_weight += location["weight"]

    current_weight = initial_weight

    total_fuel_used = 0

    for i in range(len(route) - 1):

        from_node = route[i]
        to_node = route[i + 1]

        distance = distance_matrix[from_node][to_node]

        fuel_ratio = (
            0.02
            + 0.03 *
            (current_weight / initial_weight)
        )

        fuel_used = distance * fuel_ratio

        total_fuel_used += fuel_used

        if to_node != 0:
            current_weight -= locations[to_node]["weight"]

    fuel_cost = total_fuel_used * fuel_price

    return total_fuel_used, fuel_cost


def calculate_server_cost(execution_time):

    return execution_time * 50


def calculate_tco(
    fuel_cost,
    server_cost
):

    return fuel_cost + server_cost