---
title: Optional Attachments
lang: en
documentclass: article
numbersections: true
header-includes:
    - \include{header}
---

# References for the proposal

## Ralf Gommers

The scientific Python ecosystem has become the number one choice for
researchers and practitioners in scientific computing, data science and AI, and
now has an estimated ten million users. Core projects of that ecosystem, such
as NumPy, SciPy and Scikit-learn, have been searching for better ways to
improve performance of numerical Python code since their inception. Besides
writing in straight C/C++, which is hard for most contributors and users, the
main accelerator technologies of choice are Cython, Numba, and Pythran.

Cython is the oldest and most mature project, and is fairly heavily used. Its
also the slowest of the three options though, and it’s a mix of Python and C
syntax which makes it less accessible. Therefore we, as maintainers of core
projects, are interested in Numba and Pythran. Numba’s strength is that it’s
very easy to get started with as a user - often all it takes is adding a single
decorator - but for library code it lacks the ahead-of-time compilation needed
for large-scale use and distribution. Pythran does offer that, but is harder to
experiment with because it requires a C++ compilation step. Transonic looks
promising because it allows us to combine the best of both worlds: ease of
experimenting with Numba, and robust performance to distribute to end users.
Maturing Transonic and its integration with Pythran, Numba and Cython is likely
to have a significant impact on the whole ecosystem.

Ralf Gommers, SciPy Steering Council Chair & Director, Quansight Labs
