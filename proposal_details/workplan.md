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

Beside these enhancements, we will also dedicate time and energy for community
engagement, documentation and maintenance. For example, Cython has more than
700 opened issues and 77 pull requests! Taking care of users and contributors
is also an important task.

## Detailed tasks

### Phase 0 (June-October 2020)

- Solve Cython issues that are blockers for Transonic-Cython. In particular,
improve Cython's pure-Python mode (useful for Transonic and Cython users).

- Improve the Cython backend with support for `cast` and `nogil`. Demonstrate
that Transonic-Cython is as fast as Cython on most scikit-image numerical
kernels.

- Increase the robustness of Transonic. End-users should never be disturbed by
Transonic. This implies refactoring Transonic code and improving dependencies
used for code analyzes and transformations (Beniget and Gast). We will also
increase testing and write a demo package using Transonic as scikit-image would
use it (with good documentation for developers and for users).

- Pull-requests in scikit-image with simple use of Transonic-Cython (replace
.pyx by .py using Transonic, but keeping the same accelerator).

### Phase 1 (November 2020 - February 2021)

- Improve the 3 main backends. Involvement of developers of the accelerators to
get better performance with Transonic. Extend Transonic API if needed.

- Improve fused types in Transonic and in the accelerators (work needed in
Cython).

- Find good solutions for how the Transonic backend in chosen by the user.

- Transonic API to define alternative implementations of a function for
different backends.

- More scikit-image ported to Transonic with serious benchmarks. These
benchmarks should be reproducible on different platforms and the results will
be made available on a website. We will propose to developers using other
languages to submit their own implementations for comparison.

- Improvement of Numba performance on high-level code.

- Pull-requests in scikit-image for faster kernels (and/or cleaner code) with
alternative backends (Pythran and Numba).

### Phase 2 (March-May 2021)

- Making it easy to write a new backend to Transonic. Currently, it should
already be possible to write a backend as a Transonic extension. We will
improve the documentation on this feature and contact developers of other
accelerators (for example Weld and Pyccel) to collaborate on their Transonic
backend. We plan to propose an internship on this subject.

- Find the correct Transonic abstraction to represent:

  - PyCapsules (Pythran and Cython) and cfunc (Numba) and to easily
  create scipy.LowLevelCallable,

  - parallel instructions. Cython and Numba use `prange` and Pythran uses
  OpenMP annotations,

  - user-defined low-level types (`cdef class` in Cython and `jitclass` in
  Numba). Support in Pythran for `dataclass`.

## Dissemination of the results and communication

A good documentation, targeting both developers of libraries and simple users,
is a key factor for the success of Transonic and of this project. We will
therefore be very careful to spent time on the documentations of Transonic and
of the accelerators, and more generally on communication through other channels:

- Dedicated online chat service and social media,

- Blog notes about the advancement of the project,

- One article presenting Transonic and the Joint Python Accelerators project
submitted to the Journal of Open Source Software,

- Benchmark repository and website,

- Presentations and tutorials in Python conferences (in particular the annual
Scipy conference and Euroscipy).

One goal of this project is to allow every simple user of Python to easily get
very good performance. We will try to be as inclusive and accessible as
possible.

## Final workshop

We plan to organize a workshop with tutorials and sprints. We will invite
developers of libraries which could use the products that will be built during
this project. Part of this workshop will be dedicated to work on the PyPy, HPy
and EPython projects, which may become important for the future of efficient
computing with Python.
