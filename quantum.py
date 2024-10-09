# Importing necessary libraries from Qiskit
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to put the qubit into a superposition state
qc.h(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Draw the circuit
x = qc.draw('mpl')

