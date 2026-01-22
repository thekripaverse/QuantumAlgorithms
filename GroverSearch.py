import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
with st.sidebar:
    st.title("Grover’s Algorithm - Learn It")
    
    st.subheader("What is it?")
    st.markdown("""
    Grover’s Algorithm is a **quantum search algorithm** that finds a specific item in an unsorted list **faster** than classical search.

    - Classical Search:  ~N steps  
    - Quantum Grover:  ~√N steps  
    """)

    st.subheader("Real-life Example:")
    st.markdown("""
    Suppose you have 8 lockers, and **only 1 has the prize**.  
    - Classical method checks 1 by 1.  
    - Grover’s quantum magic can find it in just 2 tries.
    """)

    st.subheader(" How It Works (Simplified):")
    st.markdown("""
    1. **Create Superposition** – All lockers opened at once  
    2. **Oracle** – Marks the right locker 
    3. **Amplify** – Increases chance for marked one 
    4. **Measure** – Most likely, the correct answer   
    """)

    st.subheader(" Your Role Here")
    st.markdown("""
    You give a binary string (like `101`) = the target.  
    Grover builds a quantum circuit to **find it**.
    """)

    st.subheader(" Why It Matters")
    st.markdown("""
    - Works on **unsorted data**
    - Powerful for **security, AI, optimization**
    - Shows real **quantum advantage**
    """)

    st.markdown("---")
    st.markdown("Built using Qiskit + Streamlit")

# Title
st.title("Grover's Algorithm - Custom Oracle")

# Input binary string
target_binary = st.text_input("Enter target binary string (e.g. 101):", "101")

# Validate input
if not all(bit in "01" for bit in target_binary):
    st.error("Please enter a valid binary string using only 0s and 1s.")
    st.stop()

n = len(target_binary)
qc = QuantumCircuit(n, n)

# Step 1: Initialize to superposition
qc.h(range(n))

# Step 2: Oracle - mark the target state
for i, bit in enumerate(target_binary):
    if bit == '0':
        qc.x(i)

qc.h(n - 1)
if n == 2:
    qc.cx(0, 1)
else:
    qc.mcx(list(range(n - 1)), n - 1)
qc.h(n - 1)

for i, bit in enumerate(target_binary):
    if bit == '0':
        qc.x(i)

# Step 3: Diffusion operator
qc.h(range(n))
qc.x(range(n))

qc.h(n - 1)
if n == 2:
    qc.cx(0, 1)
else:
    qc.mcx(list(range(n - 1)), n - 1)
qc.h(n - 1)

qc.x(range(n))
qc.h(range(n))

# Step 4: Measurement
qc.measure(range(n), range(n))

# Simulate
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()

# Show circuit
st.subheader("Grover Circuit")
st.text(qc.draw(output='text'))


# Show result
st.subheader("Measurement Histogram")
fig = plot_histogram(counts, bar_labels=False, figsize=(8, 5))
st.pyplot(fig)

# Display raw counts
st.subheader("Raw Output Counts")
st.json(counts)

