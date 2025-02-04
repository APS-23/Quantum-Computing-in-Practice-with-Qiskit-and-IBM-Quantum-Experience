#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020

@author: hassi
"""

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

from IPython.display import display

import matplotlib
matplotlib.use("Qt5Agg")

print("Ch 4: Quantum coin tosses")
print("-------------------------")

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.measure(q, c)
#display(qc.draw('mpl'))

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=20000)
result = job.result()
counts = result.get_counts(qc)
print(counts)

display(plot_histogram(counts))


