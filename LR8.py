import random
import time


# Функция для генерации случайной матрицы смежности
def generate_random_adjacency_matrix(num_vertices):
    matrix = [[random.randint(0, 1) for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        matrix[i][i] = 0  # На главной диагонали будем всегда иметь нули
        for j in range(i + 1, num_vertices):
            matrix[i][j] = matrix[j][i]  # Симметричная матрица для неориентированного графа
    return matrix


# Функция для обхода в ширину
def breadth_first_search(graph, start_vertex):
    visited = [False] * len(graph)
    queue = [0] * len(graph)
    front, rear = 0, 0

    visited[start_vertex] = True
    print(f"Посещенная вершина: {start_vertex}")
    queue[rear] = start_vertex
    rear += 1

    while front != rear:
        current_vertex = queue[front]
        front += 1
        for neighbor in range(len(graph)):
            if graph[current_vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                print(f"Посещенная вершина: {neighbor}")
                queue[rear] = neighbor
                rear += 1


# Главная функция
def main():
    random.seed()

    print('Введите необходимое кол-во вершин:')
    num_vertices = int(input())  # кол-во вершин

    #print('Введите необходимое кол-во ребер:')
    #num_edges = int(input())  # Желаемое количество рёбер

    adjacency_matrix = generate_random_adjacency_matrix(num_vertices)

    print("Матрица смежности:")
    for row in adjacency_matrix:
        print(" ".join(map(str, row)))

    start_vertex = int(input(f"Введите начальную вершину для обхода (от 0 до {num_vertices - 1}): "))
    if start_vertex < 0 or start_vertex >= num_vertices:
        print(f"Недопустимая начальная вершина. Пожалуйста, введите вершину между 0 и {num_vertices - 1}.")
        return 1  # Выход с кодом ошибки

    start_time = time.time()  # Начало замера времени выполнения
    print(f"Обход в ширину, начиная с вершины {start_vertex}:")
    breadth_first_search(adjacency_matrix, start_vertex)
    end_time = time.time()  # Окончание замера времени выполнения

    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")


if __name__ == "__main__":
    main()
