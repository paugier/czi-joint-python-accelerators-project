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


## Summary

- Find the correct Transonic abstraction to represent a concept available in
(some of) the backend(s). Define a good API for Transonic to express these
concepts.

- Improve the accelerators when needed. Fix bugs and performance issues.
Implement new features when needed (better fused types in Cython, dataclasses
in Pythran).

- Improve Transonic backends, i.e. write better/faster Cython/Numba/Pythran
code from Transonic code.

- Improve the integration and feature coverage of the Pythran support in
Cython. This has the potential to improve without modification already written
Cython code. More standard NumPy/SciPy code gets vectorised and accelerated. We
should even be able to add support for vectorised binary operators on memory
views.

#### Dissemination of the results and communication

- One article.

- Transonic's documentation.

- Documentation of a demo package.

- Benchmark repository and website.

- Organization of a workshop with participants of this project and
core-developers of other Python libraries to present the results obtained.

We will also invite to this workshop people involved in the HPy project (PyPy,
Numpy, Cython).

## Detailed tasks for Transonic

### Phase 0

- Solve Cython issues that are blockers for Transonic-Cython. In particular,
improve and fix Cython's pure-Python mode (useful for Transonic and directly
for Cython users).

- Improve the Cython backend with support for `cast` and `nogil`. Demonstrate
that Transonic-Cython is as fast as Cython on most scikit-image numerical
kernels.

- Increase the robustness of Transonic. End-users should never be disturbed by
Transonic. This implies refactoring Transonic code and improving
dependencies used for code analyzes and transformations (Beniget and Gast).
This will also be achieved by increasing testing and writting a demo package
using Transonic as scikit-image would use it (with good documentation for
developers and for users).

- Pull-request in scikit-image with simple use of Transonic-Cython (replace
.pyx by .py using Transonic, but keeping the same accelerator).

### Phase 1

- Improve the 3 main backends. Involvement of developers of the accelerators to
get better performance with Transonic. Do we need to extend Transonic API?

- Improve fused types in Transonic backends and in the accelerators (work
needed in Cython).

- Find good solutions for how the Transonic backend in chosen by the user.

- Transonic API to define alternative implementations of a function for
different backends.

- More scikit-image ported to Transonic with serious benchmarks. These
benchmarks should be reproducible on different platforms and the results will
be made available on a website. We will propose to developers using other
langages to submit their own implementations for some functions.

- Improvement of Numba performance on high-level code.

- Pull-request in scikit-image for faster kernels (and/or cleaner code) with
alternative backends (Pythran and Numba).

### Phase 2

- Making it easy to write a new backend to Transonic. It should be possible to
write a backend as a Transonic extension. We will improve the documentation on
this possibility and contact developers of other accelerators (?) to start to
collaborate on their Transonic backend.

- Transonic's documentation on how to use what we learned in other projects.

- Find the correct Transonic abstraction to represent PyCapsules (Pythran and
Cython) and cfunc (Numba) and be able to easily create scipy.LowLevelCallable.

- Find the correct Transonic abstraction to represent parallel instructions.
Cython and Numba use prange and Pythran uses OpenMP annotations.

- Find the correct Transonic abstraction to represent user-defined low-level
types (`cdef class` in Cython and `jitclass` in Numba). Support in Pythran for
dataclasses.
