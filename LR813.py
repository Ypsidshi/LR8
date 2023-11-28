# Функция для добавления ребра между вершинами u и v
def add_edge(adjacency_list, u, v):
    adjacency_list[u][v] = 1
    adjacency_list[v][u] = 1  # Для ненаправленного графа

# Процедура для вывода списка смежности графа
def print_adjacency_list(adjacency_list, num_vertices):
    print("Список смежности графа:")
    for i in range(num_vertices):
        print(f"Вершина {i}: ", end='')
        for j in range(num_vertices):
            if adjacency_list[i][j] == 1:
                print(f"{j} ", end='')
        print()

# Процедура обхода в ширину
def breadth_first_search(adjacency_list, start_vertex, num_vertices):
    visited = [False] * num_vertices
    queue = []
    front, rear = 0, 0

    visited[start_vertex] = True
    print(f"Посещенная вершина: {start_vertex}")
    queue.append(start_vertex)
    rear += 1

    while front < rear:
        current_vertex = queue[front]
        front += 1
        for neighbor in range(num_vertices):
            if adjacency_list[current_vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                print(f"Посещенная вершина: {neighbor}")
                queue.append(neighbor)
                rear += 1

# Главная функция
def main():
    print('Введите необходимое кол-во вершин:')
    n = int(input()) #кол-во вершин
    adjacency_list = [[0 for _ in range(7)] for _ in range(7)]

    # Добавление рёбер между вершинами (пример)
    add_edge(adjacency_list, 0, 1)
    add_edge(adjacency_list, 0, 2)
    add_edge(adjacency_list, 1, 3)
    add_edge(adjacency_list, 2, 3)
    add_edge(adjacency_list, 3, 4)
    add_edge(adjacency_list, 4, 5)

    print_adjacency_list(adjacency_list, n)

    start_vertex = int(input(f"Введите начальную вершину для обхода (от 0 до {n - 1}): "))
    if start_vertex < 0 or start_vertex >= n:
        print(f"Недопустимая начальная вершина. Пожалуйста, введите вершину между 0 и {n - 1}.")
        return 1  # Выход с кодом ошибки

    print(f"Обход в ширину, начиная с вершины {start_vertex}:")
    breadth_first_search(adjacency_list, start_vertex, n)

if __name__ == "__main__":
    main()