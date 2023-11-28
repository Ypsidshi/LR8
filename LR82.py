import random
import time

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

# Генерация случайной матрицы смежности
def generate_random_adjacency_matrix(num_vertices):
    matrix = [[random.randint(0, 1) for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        matrix[i][i] = 0  # На главной диагонали будем всегда иметь нули
        for j in range(i + 1, num_vertices):
            matrix[i][j] = matrix[j][i]  # Симметричная матрица для неориентированного графа
    return matrix

# Обход в ширину для графа на основе матрицы смежности
def breadth_first_search(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    queue = Queue()

    visited[start] = True
    print(f"Посещенная вершина: {start}")
    queue.enqueue(start)

    start_time = time.time()  # Начало замера времени

    while not queue.is_empty():
        current_vertex = queue.dequeue()
        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                print(f"Посещенная вершина: {neighbor}")
                queue.enqueue(neighbor)

    end_time = time.time()  # Окончание замера времени
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")

# Ввод размерности матрицы
print('Введите размерность матрицы:')
num_vertices = int(input())  # размерность матрицы
adjacency_matrix = generate_random_adjacency_matrix(num_vertices)

# Вывод матрицы смежности на экран
print("Матрица смежности:")
for row in adjacency_matrix:
    print(' '.join(map(str, row)))

# Выбор вершины для обхода
print('Выберите вершину для обхода:')
start_vertex = int(input())  # Начальная вершина для обхода
print(f"Обход в ширину, начиная с вершины {start_vertex}:")
breadth_first_search(adjacency_matrix, start_vertex)
