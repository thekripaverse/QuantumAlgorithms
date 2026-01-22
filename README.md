# Grover’s Algorithm Visualizer

**Interactive Quantum Search Demonstration using Qiskit and Streamlit**

This project is an interactive web application that demonstrates **Grover’s Algorithm**, a fundamental quantum search algorithm, using a custom oracle. Built with **Qiskit** and **Streamlit**, the app allows users to input any binary target state and observe how a quantum circuit amplifies its probability, along with real-time circuit visualization and measurement histograms.

---

## Overview

Grover’s Algorithm provides a quadratic speedup for searching an unsorted database. This application simplifies the concept by allowing users to:

* Define a target binary string
* Automatically construct a Grover quantum circuit
* Simulate the circuit using a quantum simulator
* Visualize both the circuit and the measurement results

The sidebar explains the theory, intuition, and real-world relevance of Grover’s Algorithm, making the app suitable for both **learning and demonstration purposes**.

---

## Key Features

* Custom binary input for target state
* Automatic construction of Grover’s oracle
* Full Grover diffusion operator implementation
* Real-time quantum circuit generation
* Measurement histogram visualization
* Educational sidebar with algorithm explanation
* Quantum simulation using AerSimulator

---

## Technology Stack

* Python
* Streamlit
* Qiskit
* Qiskit Aer
* NumPy
* Matplotlib (via Qiskit visualization)

---

## Application Workflow

1. User enters a binary target string (example: `101`).
2. The system initializes qubits into superposition.
3. A custom oracle marks the target state.
4. Grover’s diffusion operator amplifies the marked state.
5. The circuit is simulated using Qiskit Aer.
6. The quantum circuit, histogram, and raw counts are displayed.

---

## Installation and Execution

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

Make sure Python 3.9+ is installed.

---

## Educational Value

* Demonstrates real quantum advantage
* Helps understand superposition, oracle design, and amplitude amplification
* Useful for quantum computing beginners and academic demos
* Bridges theoretical concepts with hands-on visualization

---

## Future Enhancements

* Step-by-step circuit animation
* Adjustable number of Grover iterations
* Noise model simulation
* Comparison with classical linear search
* Deployment to Streamlit Cloud

---
