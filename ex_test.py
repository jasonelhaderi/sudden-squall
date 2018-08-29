import pypsqueak.api as sq
import pypsqueak.gates
import numpy as np

p = sq.Program()

def my_gate(theta):
    rep = [[np.cos(theta/2), -np.sin(theta/2)],
           [np.sin(theta/2), np.cos(theta/2)]]

    return rep

rotation = p.gate_def("CLS_ROT", my_gate)
p.add_instr(rotation(0), theta=np.pi)
p.measure(0, 0)
print(p)

qcvm = sq.qcVirtualMachine()
print('Classical register: ', qcvm.execute(p))
print('Quantum register: ', qcvm.quantum_state(p))
