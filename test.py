#!/usr/bin/env python3
"""
Проверка работоспособности библиотек для анализа данных.
Запуск: poetry run python check_libs.py
"""

import sys
import importlib

# Список библиотек для проверки (название пакета, имя для импорта, ожидаемая версия)
libs = [
    ("numpy", "numpy", "1.26.4"),
    ("pandas", "pandas", "2.2.2"),
    ("matplotlib", "matplotlib", "3.8.4"),
    ("seaborn", "seaborn", "0.13.2"),
    ("scikit-learn", "sklearn", "1.5.1"),
    ("scipy", "scipy", "1.13.1"),
    ("statsmodels", "statsmodels", "0.14.2"),
    ("jupyter", "jupyter", "1.0.0"),          # для проверки импорта (но не обязательно)
    ("notebook", "notebook", "7.2.1"),
]

print("=" * 60)
print("ПРОВЕРКА УСТАНОВЛЕННЫХ БИБЛИОТЕК")
print("=" * 60)

# 1. Проверка импорта и версий
print("\n1. Проверка наличия и версий:")
failed = []
for pkg_name, import_name, expected_ver in libs:
    try:
        module = importlib.import_module(import_name)
        # Получаем версию (у разных пакетов может быть __version__ или version)
        if hasattr(module, "__version__"):
            ver = module.__version__
        elif hasattr(module, "version"):
            ver = module.version
        else:
            ver = "unknown"
        status = "✓" if ver == expected_ver else "⚠ (ожидалась {})".format(expected_ver)
        print(f"  {pkg_name:15} {ver:12} {status}")
    except ImportError as e:
        print(f"  {pkg_name:15} НЕ УСТАНОВЛЕН     ✗")
        failed.append(pkg_name)

if failed:
    print("\n❌ Ошибка: не найдены библиотеки:", ", ".join(failed))
    sys.exit(1)
else:
    print("\n✅ Все библиотеки импортируются успешно.")

# 2. Базовые функциональные проверки
print("\n2. Выполнение базовых операций:")

try:
    # NumPy
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  NumPy:     массив {arr}, сумма = {np.sum(arr)}")
except Exception as e:
    print(f"  NumPy:     ошибка - {e}")

try:
    # Pandas
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(f"  Pandas:    DataFrame (2x3), среднее A = {df['A'].mean():.1f}")
except Exception as e:
    print(f"  Pandas:    ошибка - {e}")

try:
    # Matplotlib (без вывода на экран, просто создадим фигуру)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    plt.close(fig)
    print("  Matplotlib: создание графика успешно")
except Exception as e:
    print(f"  Matplotlib: ошибка - {e}")

try:
    # Seaborn (проверка наличия набора данных)
    import seaborn as sns
    # просто загрузим встроенные данные (не обязательно)
    # если загрузка не сработает, просто проверим импорт
    print("  Seaborn:    импорт успешен")
except Exception as e:
    print(f"  Seaborn:    ошибка - {e}")

try:
    # Scikit-learn
    from sklearn.linear_model import LinearRegression
    X = [[1], [2], [3]]
    y = [2, 4, 6]
    model = LinearRegression().fit(X, y)
    pred = model.predict([[4]])
    print(f"  Sklearn:    линейная регрессия предсказание для 4 = {pred[0]:.2f}")
except Exception as e:
    print(f"  Sklearn:    ошибка - {e}")

try:
    # SciPy
    from scipy import stats
    data = [1, 2, 3, 4, 5]
    mean = stats.tmean(data)
    print(f"  SciPy:      среднее = {mean:.1f}")
except Exception as e:
    print(f"  SciPy:      ошибка - {e}")

try:
    # Statsmodels
    import statsmodels.api as sm
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    X_sm = sm.add_constant(X)
    model = sm.OLS(y, X_sm).fit()
    print(f"  Statsmodels: OLS R² = {model.rsquared:.4f}")
except Exception as e:
    print(f"  Statsmodels: ошибка - {e}")

try:
    # Jupyter (просто проверяем, что можно импортировать)
    import jupyter
    print("  Jupyter:    импорт успешен")
except Exception as e:
    print(f"  Jupyter:    ошибка - {e}")

try:
    import notebook
    print("  Notebook:   импорт успешен")
except Exception as e:
    print(f"  Notebook:   ошибка - {e}")

print("\n" + "=" * 60)
print("ПРОВЕРКА ЗАВЕРШЕНА")
print("=" * 60)