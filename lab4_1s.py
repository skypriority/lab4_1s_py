import sys
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

def fact_recursive(n):
    """Факториал через рекурсию."""
    if n <= 1:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n):
    """Факториал через цикл."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

ns = [10, 50, 100, 200, 300, 400, 500, 700, 900]   # ось X
REPEAT = 5        # сколько раз повторяем замер, чтобы усреднить
NUMBER = 1000     # сколько вызовов внутри одного замера


def bench(func, n):
    """
    Возвращает среднее время ОДНОГО вызова func(n) в микросекундах.
    timeit.repeat делает REPEAT прогонов по NUMBER вызовов,
    берём минимум (самый "чистый" прогон без помех ОС) и делим на NUMBER.
    """
    times = timeit.repeat(lambda: func(n), repeat=REPEAT, number=NUMBER)
    best = min(times)                 # самый чистый прогон
    return best / NUMBER * 1_000_000  # секунды -> микросекунды


rec_times = []
it_times = []

print(f"{'n':>5} | {'рекурсия, мкс':>14} | {'цикл, мкс':>10} | {'во сколько раз':>14}")
print("-" * 55)

for n in ns:
    t_rec = bench(fact_recursive, n)
    t_it = bench(fact_iterative, n)

    rec_times.append(t_rec)
    it_times.append(t_it)

    print(f"{n:>5} | {t_rec:>14.2f} | {t_it:>10.2f} | {t_rec / t_it:>13.2f}x")


plt.figure(figsize=(9, 5))
plt.plot(ns, rec_times, 'o-', label='fact_recursive (рекурсия)')
plt.plot(ns, it_times, 's-', label='fact_iterative (цикл)')

plt.xlabel('n (входное число)')
plt.ylabel('Время одного вызова, мкс')
plt.title('Факториал: рекурсия vs цикл')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('factorial_benchmark.png', dpi=120)  
plt.show()
