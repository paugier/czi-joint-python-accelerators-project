# Abstract

The joint Python Accelerators project gathers developers of Transonic, Cython,
Pythran, Numba and scikit-image. Our collaboration aims at improving the state
of Python acceleration so that clean and modern Python code can easily be
accelerated to reach high performance.

We propose to improve interoperability and compatibility between existing
accelerators. We will improve the integration and feature coverage of the
Pythran support in Cython, which will impact much existing Cython code.

We will base our work on Transonic, a new package that accelerates
the same code with different accelerators, using just-in-time and ahead-of-time
compilations. We propose to work on usage of Transonic in scikit-image,
which is a good example of a widely used library relying a lot on Cython while
its developers would love to be able to write simpler Python and to also use
Numba and Pythran as accelerators.

While working on scikit-image code, we will improve its maintainability and
performance. We will also improve the accelerators by fixing bugs, implementing
missing features and increasing performance. This will have a direct impact on
the life sciences through the improvement of many downstream Python packages.

More generally, this project will greatly improve the state of the scientific
Python ecosystem. There will be one tool adapted for both developers of
fundamental libraries (like scikit-image) and end users (such as scientists and
students), with a clean API and good documentation. Moreover, this project will
launch long-term dynamics on performance for scientific Python, based on
compatibility, interoperability and gentle competition between the
accelerators.
