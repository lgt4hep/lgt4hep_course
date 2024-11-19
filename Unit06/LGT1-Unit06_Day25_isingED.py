import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt  # Add this line to import matplotlib.pyplot

# Define the Pauli matrices
I = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

# Number of sites
N = 4
J = 1  # Coupling constant
h = 1.5  # Transverse field

def kron_n(*args):
    """Computes the Kronecker product of a list of matrices."""
    result = np.array([[1]], dtype=complex)
    for op in args:
        result = np.kron(result, op)
    return result

# Construct the interaction term H_zz = -J * sum(sigma^z_i * sigma^z_{i+1}) with PBC
H_zz = np.zeros((2**N, 2**N), dtype=complex)
for i in range(N):
    Z_i = [Z if j == i or j == (i + 1) % N else I for j in range(N)]
    H_zz -= J * kron_n(*Z_i)

# Construct the transverse field term H_x = -h * sum(sigma^x_i)
H_x = np.zeros((2**N, 2**N), dtype=complex)
for i in range(N):
    X_i = [X if j == i else I for j in range(N)]
    H_x -= h * kron_n(*X_i)

# Total Hamiltonian
H = H_zz + H_x

# Time evolution operator U(t) = exp(-i * H * t)
def time_evolution(H, t):
    return expm(-1j * H * t)

# Parameters for time evolution
time_steps = 100
total_time = 1
delta_t = total_time / time_steps

# Initial state |0000>
initial_state = np.zeros(2**N, dtype=complex)
initial_state[0] = 1.0

# Evolve the state over time
state = initial_state.copy()
evolution = [state]
for step in range(time_steps):
    U = time_evolution(H, delta_t)
    state = U @ state
    evolution.append(state)

# Print final evolved state (amplitude squared as percentages) with binary representation
print("Final state (amplitude squared as percentages):")
for i in range(2**N):
    percentage = np.abs(state[i])**2 * 100
    print(f"State |{format(i, f'0{N}b')}>: {percentage:.6f}%")

# Plot probabilities
probabilities = [np.abs(state)**2 for state in evolution]
times = np.linspace(0, total_time, time_steps + 1)
plt.figure(figsize=(12, 6))
for i in range(2**N):
    plt.plot(times, [prob[i] for prob in probabilities], label=f"State |{format(i, f'0{N}b')}")
plt.xlabel("Time")
plt.ylabel("Probability")
plt.title("Time Evolution of 4-Site Ising Model (PBC)")
plt.legend()
plt.show()
