def greedy_tsp(distance_matrix):

    # Jumlah total node pada graf
    n = len(distance_matrix)

    # Hub selalu berada di node 0
    current = 0

    # Menandai node yang sudah dikunjungi
    visited = [False] * n
    visited[current] = True

    # Menyimpan rute perjalanan
    route = [current]

    # Menyimpan total jarak tempuh
    total_distance = 0

    ### GREEDY NEAREST NEIGHBOR ###
    # Kunjungi semua node dengan memilih tetangga terdekat
    for _ in range(n - 1):

        nearest_node = -1
        nearest_distance = float("inf")

        # Cari node terdekat yang belum dikunjungi
        for next_node in range(n):

            if not visited[next_node]:

                if distance_matrix[current][next_node] < nearest_distance:
                    nearest_distance = distance_matrix[current][next_node]
                    nearest_node = next_node

        # Pindah ke node tersebut
        visited[nearest_node] = True
        route.append(nearest_node)
        total_distance += nearest_distance
        current = nearest_node

    # Menambahkan perjalanan kembali ke Hub
    total_distance += distance_matrix[current][0]
    route.append(0)

    return route, total_distance