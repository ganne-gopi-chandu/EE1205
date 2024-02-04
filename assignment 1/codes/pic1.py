import matplotlib.pyplot as plt
import numpy as np

def ap_general_term(a, d, n):
    if n>=1:
        return a+(n-1)*d
    else:
        return 0

def plot_ap_general_term(a, d, start, end):
    n_values = np.arange(start, end + 1, 1)
    ap_values = [ap_general_term(a, d, n) for n in n_values]

    plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
    plt.title('General Term of Arithematic Progression')
    plt.xlabel('n')
    plt.ylabel('Term Value')
    plt.grid(True)
    plt.show()

a = 1  
d = 2
start_n = 0
end_n = 8
plot_ap_general_term(a, d, start_n, end_n)
