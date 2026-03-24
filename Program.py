import tkinter as tk
from tkinter import messagebox
from functools import reduce


# --- 1. LOGIKA FUNKCYJNA (PURE FUNCTIONS) ---

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def arithmetic_seq(a1, r, n):
    if n <= 1: return a1
    return arithmetic_seq(a1, r, n - 1) + r


def geometric_seq(a1, q, n):
    if n <= 1: return a1
    return geometric_seq(a1, q, n - 1) * q


def get_analysis(limit, divisor):
    """
    Czysta transformacja danych (Pure Function):
    Wynik zależy wyłącznie od argumentów wejściowych, brak efektów ubocznych.
    """

    # 1. Tworzenie źródła danych:
    # Generujemy niemutowalny zakres liczb od 1 do limit.
    numbers = range(1, limit + 1)

    # 2. FILTER (Selekcja):
    # Wybieramy tylko te liczby, które spełniają warunek (dzielą się przez 'divisor').
    # Lambda to anonimowa funkcja logiczna sprawdzająca warunek "tu i teraz".
    filtered = list(filter(lambda x: x % divisor == 0, numbers))

    # 3. MAP (Transformacja):
    # Każdy element z przefiltrowanej listy podnosimy do kwadratu.
    # Oryginalna lista 'filtered' pozostaje niezmieniona (Immutability).
    squares = list(map(lambda x: x ** 2, filtered))

    # 4. REDUCE (Agregacja):
    # Sprowadzamy listę kwadratów do jednej wartości (ich sumy).
    # 'acc' to akumulator, który przechowuje wynik cząstkowy dodawania kolejnych 'x'.
    total_sum = reduce(lambda acc, x: acc + x, squares, 0)

    # Zwracamy wyniki jako krotkę (tuple) - czytelny podział etapów pracy potoku.
    return filtered, squares, total_sum


# reszta to już sam interface i nie ma znaczenia
# --- 2. OKNO ANALIZY (OSOBNE OKNO / TOPLEVEL) ---

def open_analysis_window():
    new_win = tk.Toplevel()
    new_win.title("Laboratorium: Map/Filter/Reduce")
    new_win.geometry("450x550")
    new_win.configure(bg="#34495e")

    tk.Label(new_win, text="POTOK PRZETWARZANIA DANYCH", font=("Arial", 12, "bold"), bg="#34495e", fg="#f1c40f").pack(
        pady=10)

    # Inputy
    tk.Label(new_win, text="Zakres (od 1 do X):", bg="#34495e", fg="white").pack()
    entry_lim = tk.Entry(new_win);
    entry_lim.insert(0, "100");
    entry_lim.pack(pady=5)

    tk.Label(new_win, text="Dzielnik (Modulo):", bg="#34495e", fg="white").pack()
    entry_div = tk.Entry(new_win);
    entry_div.insert(0, "7");
    entry_div.pack(pady=5)

    res_area = tk.Text(new_win, height=15, width=50, state='disabled', bg="#ecf0f1", font=("Courier", 9))
    res_area.pack(pady=10)

    def run():
        try:
            l, d = int(entry_lim.get()), int(entry_div.get())
            if d == 0: raise ZeroDivisionError

            # Wywołanie logiki funkcyjnej
            div_list, sq_list, total = get_analysis(l, d)

            # Formatowanie wyjścia z opisem narzędzi
            output = f"RAPORT OPERACJI FUNKCYJNYCH:\n"
            output += "=" * 30 + "\n"
            output += f"1. FILTER (Selekcja):\n   Liczby podzielne przez {d}:\n   {div_list[:15]}...\n\n"
            output += f"2. MAP (Transformacja):\n   Kwadraty tych liczb:\n   {sq_list[:10]}...\n\n"
            output += f"3. REDUCE (Agregacja):\n   Suma wszystkich kwadratów:\n   => {total}\n"
            output += "=" * 30 + "\n"
            output += "Status: Dane przetworzone bez użycia pętli for."

            res_area.config(state='normal');
            res_area.delete(1.0, tk.END)
            res_area.insert(tk.END, output);
            res_area.config(state='disabled')
        except:
            messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")

    tk.Button(new_win, text="URUCHOM POTOK (Pipeline)", command=run, bg="#e67e22", fg="white",
              font=("Arial", 10, "bold")).pack(pady=10)

# --- 3. GŁÓWNE OKNO ---

def run_main():
    root = tk.Tk()
    root.title("Kalkulator Funkcyjny")
    root.geometry("400x700")
    root.configure(bg="#2c3e50")

    # Wyświetlacz
    display = tk.Entry(root, font=("Arial", 20), justify='right', bd=10, bg="#ecf0f1")
    display.pack(pady=10, padx=10, fill='x')

    # Kalkulator
    calc_frame = tk.Frame(root, bg="#2c3e50")
    calc_frame.pack()

    def c_click(v):
        display.insert(tk.END, v)

    def c_eval():
        try:
            res = eval(display.get()); display.delete(0, tk.END); display.insert(0, res)
        except:
            messagebox.showerror("Błąd", "Błędne działanie")

    btns = [('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)]
    for (t, r, c) in btns:
        cmd = c_eval if t == '=' else (lambda: display.delete(0, tk.END)) if t == 'C' else (lambda x=t: c_click(x))
        tk.Button(calc_frame, text=t, width=5, height=2, command=cmd, bg="#34495e", fg="white").grid(row=r, column=c,
                                                                                                     padx=2, pady=2)

    # Sekcja Ciągów
    tk.Label(root, text="CIĄGI REKURENCYJNE", bg="#2c3e50", fg="#3498db", font=("Arial", 12, "bold")).pack(pady=15)

    seq_frame = tk.Frame(root, bg="#2c3e50")
    seq_frame.pack()

    def add_inp(label):
        f = tk.Frame(seq_frame, bg="#2c3e50");
        f.pack(side=tk.LEFT, padx=5)
        tk.Label(f, text=label, fg="white", bg="#2c3e50").pack()
        e = tk.Entry(f, width=5);
        e.pack();
        return e

    e_a1 = add_inp("a1");
    e_a1.insert(0, "1")
    e_rq = add_inp("r / q");
    e_rq.insert(0, "2")
    e_n = add_inp("n");
    e_n.insert(0, "10")

    res_log = tk.Text(root, height=5, width=45, bg="#ecf0f1", state='disabled')
    res_log.pack(pady=10)

    def log(msg):
        res_log.config(state='normal');
        res_log.delete(1.0, tk.END);
        res_log.insert(tk.END, msg);
        res_log.config(state='disabled')

    # Przyciski akcji
    tk.Button(root, text="Ciąg Arytmetyczny", command=lambda: log(
        f"Arytmetyczny(n={e_n.get()}): a{e_n.get()} = {arithmetic_seq(float(e_a1.get()), float(e_rq.get()), int(e_n.get()))}"),
              bg="#27ae60", fg="white", width=30).pack(pady=2)
    tk.Button(root, text="Ciąg Geometryczny", command=lambda: log(
        f"Geometryczny(n={e_n.get()}): a{e_n.get()} = {geometric_seq(float(e_a1.get()), float(e_rq.get()), int(e_n.get()))}"),
              bg="#2980b9", fg="white", width=30).pack(pady=2)
    tk.Button(root, text=f"Fibonacci", command=lambda: log(f"Fibonacci(n={e_n.get()}): {fibonacci(int(e_n.get()))}"),
              bg="#9b59b6", fg="white", width=30).pack(pady=2)

    tk.Label(root, text="---", bg="#2c3e50", fg="white").pack()
    tk.Button(root, text="OTWÓRZ LABORATORIUM ANALIZY", command=open_analysis_window, bg="#f1c40f", fg="black",
              font=("Arial", 10, "bold"), width=30).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_main()