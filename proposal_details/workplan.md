# Workplan

The proposed work can be summarized in nine points:

1. scikit-image numerical kernels ported to Transonic with serious comparison
between the existing Cython solutions and the different Transonic backends.
These benchmarks should be reproducible on different platforms and the results
will be made available on a website. We will propose to developers using other
languages to submit their own implementations for comparison.

2. Find the correct Transonic abstractions to represent most concepts available
in the accelerators (`cast`, `nogil`, PyCapsules/cfunc/scipy.LowLevelCallable,
parallel instructions, user-defined low-level types, fused types/multiple
signatures, fastmath). Design a good API for Transonic to express these
concepts.

3. Improve Transonic backends, i.e. write better/faster Cython/Numba/Pythran
code from Transonic code. Demonstrate that Transonic-Cython is as fast as
Cython on most scikit-image numerical kernels.

4. Increase the robustness of Transonic. End-users should never be disturbed by
Transonic. This implies refactoring Transonic code and improving dependencies
used for code analyzes and transformations (Beniget and Gast). We will also
increase testing and write a demo package using Transonic as scikit-image would
use it (with good documentation for developers and for users).

5. Other Transonic improvements:

   - Making it easy to write a new backend to Transonic. Currently, it should
   already be possible to write a backend as a Transonic extension. We will
   improve the documentation on this feature and contact developers of other
   accelerators (for example Weld and Pyccel) to collaborate on their Transonic
   backend. We plan to propose an internship on this subject.

   - Find good solutions for how the Transonic backend in chosen by the user.

   - Transonic API to define alternative implementations of a function for
   different backends.

6. Pull-requests on scikit-image and skimage-experiments repositories to use the
accelerators via Transonic. First, Cython to Transonic-Cython, then faster
kernels (and/or cleaner code) with alternative backends (Pythran and Numba).

7. Improve the accelerators when needed. Fix bugs, performance issues and new
features (better fused types in Cython, improve Cython's pure-Python mode,
`dataclass` in Pythran, improvement of Numba performance on high-level code).

8. Improve the integration and feature coverage of the Pythran support in
Cython. This has the potential to improve without modification already written
Cython codes. More standard NumPy/SciPy code gets vectorised and accelerated.
We should even be able to add support for vectorised binary operators on memory
views.

9. Beside these enhancements, we will also dedicate time and energy for community
engagement, documentation and maintenance. For example, Cython has more than
700 opened issues and 77 pull requests! Taking care of users and contributors
is also an important task.

The deeper improvements of the accelerators with be performed by core
developers of these projects, namely Serge Guelton for Pythran, Stefan Behnel
for Cython and Stanley Seibert and Valentin Haenel for Numba. Stefan will also
solve Cython known issues that are blockers for Transonic-Cython (see
<https://transonic.readthedocs.io/en/latest/backends/cython.html>). Serge will
be implied in the tasks on Transonic/Gast/Beniget refactoring and
Pythran/Cython integration.

A full-time developer hired for the project will work with Pierre Augier
(creator for Transonic) and in closed collaboration with the other members of
the projects. Her/His tasks will be about (points 1 to 6 and 9):

- scikit-image and Transonic,

- the benchmarks and the associated website,

- report issues and work on the simplest ones,

- improve the documentation of the accelerators targetting the users.

## Dissemination of the results and communication

Good communication, targeting both developers of libraries and simple users,
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
possible in our communication.

Finally, we plan to organize after the end of this one-year grant a workshop
with tutorials and sprints. We will invite developers of libraries which could
use the products that will be built during this project. Part of this workshop
will be dedicated to work on the PyPy, HPy and EPython projects, which may
become important for the future of efficient computing with Python. This event
will be organized in Europe and may be coupled with EuroScipy or EuroPython.
