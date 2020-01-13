# The Join Python accelerators project

We create for this grant a collaboration between developers working on
different Python accelerators. This group aims at improving the situation of
Python developers and users in terms of performance of scientific Python codes.

Currently, there are many interesting projects but we also see a fragmented
situation, with incompatible accelerators.

- High-level and low-level codes. Numpy needs vectorized code but some
accelerators are very ineffective with such style of coding.

- A community split between expert developers and simple users.

- Libraries (for example Scipy, Pandas and the scikits) discuss about using
alternative accelerators internally, but...

We, participants to the Join Python accelerators project, think that it should
be able to write very effective scientist library and applications just in
clean and modern Python.

For this grant, we propose to improve the situation by (i) providing one modern
Python API (in a package called transonic) to accelerate numerical Python code
with different accelerators and (ii) improving interoperability and
compatibility between the different Python accelerators.

For this grant, we will specifically work with scikit-image core developers on
real-world numerical codes taken from scikit-image. Direct improvements of
scikit-image and of the accelerators. Indirect impacts in the whole scientific
Python ecosystem.

Future, HPy and Pypy...


## Phase 0

- Solve Cython issues that are blockers for Transonic-Cython. In particular,
improve and fix Cython's pure-Python mode (useful for Transonic and directly
for Cython users)

- Improve Transonic backends, in particular Cython (cast, nogil). Demonstrate
that Transonic-Cython is as fast as Cython on real scikit-image code.

- Increase the robustness of Transonic. End-users should never be disturbed by
Transonic.

- Pull-request simple use of Transonic-Cython in scikit-image (replace .pyx by
.py using Transonic, but keeping the same accelerator)

## Phase 1

- Improve the integration and feature coverage of the Pythran support in
Cython. This has the potential to improve without modification already written
Cython code. More standard NumPy/SciPy code gets vectorised and accelerated.
Adding support for vectorised binary operators on memory views would be great.

- Mature the 3 transonic's builtin banckends.

  * Improve fused types in Transonic backends and in the accelerators (work needed in Cython).

  * Involvement of Numba developer to get better performance with Transonic-Numba.

- Maturation for how the Transonic backend in chosen by the user.

- More scikit-image ported to Transonic with serious benchmarks.

- Implementation on non-supported features in the accelerators (Pythran, Numba
and Cython). Fix bugs and performance issues.

- Improvement of Numba performance on high-level code.

- Transonic API to define alternative implementations of a function for
different backends.

- Pull-request in scikit-image for faster kernels (or cleaner code) with
alternative backends (Pythran and Numba).

## Phase 2

- Lower the barrier for other accelerators to write their own Transonic
backend.

- Transonic's documentation on how to use what we learned in other projects.

- Support in Transonic and Pythran for dataclass

- Support in Transonic for PyCapsules / cfunc / LowLevelCallable

- Organization of a workshop with participants of this project, core-developers
of other Python libraries and people involved in the HPy project (PyPy, Numpy,
Cython).
