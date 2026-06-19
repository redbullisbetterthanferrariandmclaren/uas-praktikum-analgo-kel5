def held_karp_tsp(distance_matrix):

    # Jumlah total node pada graf
    n = len(distance_matrix)

    # DP table untuk menyimpan biaya minimum setiap state
    dp = {}

    # Parent untuk rekonstruksi rute
    parent = {}

    ### BASE CASE ###
    # Inisialisasi perjalanan langsung dari Hub (0) ke setiap node
    for k in range(1, n):
        mask = (1 << 0) | (1 << k)
        dp[(mask, k)] = distance_matrix[0][k]
        parent[(mask, k)] = 0

    ### DYNAMIC PROGRAMMING ###
    # Membangun solusi untuk subset yang semakin besar
    for subset_size in range(3, n + 1):

        for mask in range(1 << n):

            # Hub harus selalu berada di dalam subset
            if not (mask & 1):
                continue

            # Memastikan jumlah node sesuai ukuran subset
            if bin(mask).count("1") != subset_size:
                continue

            for current in range(1, n):

                # Skip jika current tidak ada di subset
                if not (mask & (1 << current)):
                    continue

                prev_mask = mask ^ (1 << current)
                best_cost = float("inf")
                best_prev = -1

                # Mencari node sebelumnya dengan biaya minimum
                for prev in range(1, n):

                    if not (prev_mask & (1 << prev)):
                        continue

                    if (prev_mask, prev) not in dp:
                        continue

                    cost = (
                        dp[(prev_mask, prev)]
                        + distance_matrix[prev][current]
                    )

                    if cost < best_cost:
                        best_cost = cost
                        best_prev = prev

                # Menyimpan hasil terbaik ke DP
                if best_prev != -1:
                    dp[(mask, current)] = best_cost
                    parent[(mask, current)] = best_prev


    ### MENENTUKAN SOLUSI OPTIMAL ###
    # Semua node telah dikunjungi
    full_mask = (1 << n) - 1
    best_cost = float("inf")
    last_node = -1

    # Menentukan node terakhir sebelum kembali ke Hub
    for k in range(1, n):

        if (full_mask, k) not in dp:
            continue

        cost = (
            dp[(full_mask, k)]
            + distance_matrix[k][0]
        )

        if cost < best_cost:
            best_cost = cost
            last_node = k


    ### REKONSTRUKSI RUTE OPTIMAL ###
    route = [0]
    mask = full_mask
    current = last_node
    reverse_path = []

    # Menelusuri parent hingga kembali ke Hub
    while current != 0:
        reverse_path.append(current)
        next_node = parent[(mask, current)]
        mask ^= (1 << current)
        current = next_node

    # Membalik urutan hasil rekonstruksi
    reverse_path.reverse()
    route.extend(reverse_path)

    # Kembali ke Hub
    route.append(0)

    return route, best_cost