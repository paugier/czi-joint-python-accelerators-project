# The Joint Python accelerators project

The joint Python Accelerators project gathers developers of Transonic, Cython,
Pythran, Numba and scikit-image. The goal of our collaboration is to improve
the state of Python code acceleration so that clean and modern Python code can
very easily be accelerated to reach very high performances.

We propose to improve interoperability and compatibility between existing
accelerators. We will first improve the integration and feature coverage of the
Pythran support in Cython, which will have a strong impact on many Cython codes
already written.

Moreover, we will base our work on a new package called Transonic, which can
accelerate one code with different accelerators, with just-in-time and
ahead-of-time compilations. We propose to work on the usage of Transonic in
scikit-image, which is a good example of a widely used Python library that
relies a lot Cython while its developers would love to be able to write cleaner
and simpler Python and to also use Numba and Pythran.

While working on scikit-image code, we will improve its maintainability (by
replacing Cython code by simpler Python-Numpy code) but also the resulting
performance. We will also improve the accelerators by fixing bugs, implementing
missing features and increasing performances.

More generally, this one-year project will greatly improve the state of the
scientific Python ecosystem. There will be one tool adapted for both developers
of fundamental libraries (like scikit-image) and simple users, with a clean API
and good documentation.

Moreover, this short-term project will launch a long-term dynamics on
performance for scientific Python, based on compatibility, interoperability and
gentle competition between the accelerators. The Joint Python accelerators
project will for example be aware of the new project HPy, which would allow
scientific code using Numpy to be executed efficiently with PyPy. We will
dedicate part of our final workshop to study what need to be done in our
different projects to get good compatibility with PyPy.
