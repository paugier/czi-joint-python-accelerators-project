# Workplan

## Summary

The proposed technical work can be summarized in four points:

- Find the correct Transonic abstractions to represent most concepts available
in the accelerators. Design a good API for Transonic to express these concepts.

- Improve the accelerators when needed. Fix bugs and performance issues.
Implement new features when needed (better fused types in Cython, `dataclass`
in Pythran).

- Improve Transonic backends, i.e. write better/faster Cython/Numba/Pythran
code from Transonic code.

- Improve the integration and feature coverage of the Pythran support in
Cython. This has the potential to improve without modification already written
Cython codes. More standard NumPy/SciPy code gets vectorised and accelerated.
We should even be able to add support for vectorised binary operators on memory
views.

## Detailed tasks related to Transonic

We will continuously improve Transonic documentation during this project.

### Phase 0 (June-October 2020)

- Solve Cython issues that are blockers for Transonic-Cython. In particular,
improve and fix Cython's pure-Python mode (useful for Transonic and directly
for Cython users).

- Improve the Cython backend with support for `cast` and `nogil`. Demonstrate
that Transonic-Cython is as fast as Cython on most scikit-image numerical
kernels.

- Increase the robustness of Transonic. End-users should never be disturbed by
Transonic. This implies refactoring Transonic code and improving
dependencies used for code analyzes and transformations (Beniget and Gast).
This will also be achieved by increasing testing and writing a demo package
using Transonic as scikit-image would use it (with good documentation for
developers and for users).

- Pull-request in scikit-image with simple use of Transonic-Cython (replace
.pyx by .py using Transonic, but keeping the same accelerator).

### Phase 1 (November 2020 - February 2021)

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
languages to submit their own implementations for some functions.

- Improvement of Numba performance on high-level code.

- Pull-request in scikit-image for faster kernels (and/or cleaner code) with
alternative backends (Pythran and Numba).

### Phase 2 (March-May 2021)

- Making it easy to write a new backend to Transonic. Currently, it should be
possible to write a backend as a Transonic extension. We will improve the
documentation on this feature and contact developers of other accelerators (for
example Weld and Pyccel) to start to collaborate on their Transonic backend.

- Find the correct Transonic abstraction to represent PyCapsules (Pythran and
Cython) and cfunc (Numba) and be able to easily create scipy.LowLevelCallable.

- Find the correct Transonic abstraction to represent parallel instructions.
Cython and Numba use `prange` and Pythran uses OpenMP annotations.

- Find the correct Transonic abstraction to represent user-defined low-level
types (`cdef class` in Cython and `jitclass` in Numba). Support in Pythran for
`dataclass`.

## Dissemination of the results and communication

- Blog notes about the advancement of the project.

- One article presenting Transonic and the Joint Python Accelerators project
submitted to the Journal of Open Source Software.

- Documentation of Transonic and of the demo package, targeting both
developers of libraries and users (how to chose and specify the backends).

- Benchmark repository and website.

- Presentations and tutorials in Python conferences (in particular the annual
Scipy conference and Euroscipy).

- Organization of a workshop with participants of this project and
core-developers of other Python libraries to present the obtained results. We
will also invite to this workshop people involved in the HPy project (PyPy,
Numpy, Cython).
