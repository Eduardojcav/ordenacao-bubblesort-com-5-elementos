import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    swapped = True
    
    for i in range(n):
        if not swapped:
            break
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
    
    return arr, comparisons, swaps

def calculate_complexities(n):
    best_case = n - 1 
    worst_case = n * (n - 1) / 2
    average_case = n * (n - 1) / 4 
    return best_case, worst_case, average_case

def generate_random_elements(size):
    return [random.randint(1, 100) for _ in range(size)]

def plot_results(sizes, actual_ops, theoretical_ops):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, actual_ops, 'o-', label='Operações Reais')
    plt.plot(sizes, theoretical_ops, 's-', label='Complexidade Teórica (O(n²))')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Número de Operações')
    plt.title('Complexidade do Bubble Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_complexity_analysis(n, comparisons):
    best, worst, average = calculate_complexities(n)
    
    print("\n═"*50)
    print("ANÁLISE DE COMPLEXIDADE ASSINTÓTICA (Big O)")
    print("═"*50)
    print(f"\nPara n = {n} elementos:")
    print(f"\n1. MELHOR CASO (array já ordenado)")
    print(f"   - Comparações: {int(best)}")
    print(f"   - Complexidade: O(n) - linear")
    
    print(f"\n2. PIOR CASO (array em ordem inversa)")
    print(f"   - Comparações: {int(worst)}")
    print(f"   - Complexidade: O(n²) - quadrática")
    
    print(f"\n3. CASO MÉDIO (array aleatório)")
    print(f"   - Comparações esperadas: ~{int(average)}")
    print(f"   - Complexidade: O(n²) - quadrática")
    
    print("\n" + "═"*50)
    print(f"\nRESULTADO DESTE TESTE:")
    print(f"Comparações realizadas: {comparisons}")
    
    if comparisons <= best + 1:  
        print("Classificação: MELHOR CASO (O(n))")
    elif comparisons >= worst - 1:
        print("Classificação: PIOR CASO (O(n²))")
    else:
        print("Classificação: CASO MÉDIO (O(n²))")
    print("═"*50)

def main():
    
    n = 5  
    
    data = generate_random_elements(n)
    print("Array original:", data)
    
    start_time = time.time()
    sorted_data, comparisons, swaps = bubble_sort(data.copy())
    end_time = time.time()
    
    print("\nRESULTADOS DA ORDENAÇÃO:")
    print("Array ordenado:", sorted_data)
    print(f"Comparações: {comparisons}")
    print(f"Trocas: {swaps}")
    print(f"Tempo de execução: {(end_time - start_time) * 1000:.4f} ms")
    
    print_complexity_analysis(len(data), comparisons)
    
    sizes = list(range(1, 11))
    actual_ops_list = []
    theoretical_ops_list = []
    
    for size in sizes:
        test_data = generate_random_elements(size)
        _, comps, _ = bubble_sort(test_data.copy())
        actual_ops_list.append(comps)
        theoretical_ops_list.append(size * (size - 1) / 2)
    
    plot_results(sizes, actual_ops_list, theoretical_ops_list)

if __name__ == "__main__":
    main()
