---
title: Optional Attachments
lang: en
documentclass: article
numbersections: true
header-includes:
    - \include{header}
---

# Logos of the projects

\begin{figure}[!h]
\centering
\includegraphics[width=0.8\linewidth]{image_transonic_vision}
\end{figure}

Transonic accelerates Python-Numpy codes with the three accelerators Cython,
Numba and Pythran.

# References for the proposal

## Juan Nunez-Iglesias, on behalf of the scikit-image team

Just like NumPy, SciPy, and scikit-learn, scikit-image uses Cython to compile
critical algorithms to native code and obtain C speed in Python. For certain
algorithms though, different accelerators can obtain better performance than
Cython, or the same performance with simpler code. However, due to our position
near the base of the scientific Python ecosystem, we have been reluctant to
take on these new technologies until they are as tried and tested as Cython.

Long before we discovered Transonic, we had been exploring the possibility of
using Numba to accelerate our code. The topic came up repeatedly. As just one
example, 2.5 years ago Stéfan van der Walt, our founder, consulted the mailing
list about taking on Numba as a dependency [^1]. The outcome that time, as well
as the others, was that too many members saw a Numba dependency as a too high a
risk, and in the end, we have continued using Cython exclusively to this day.

We have also explored using Pythran [^2] [^3], and again those efforts languished
because we considered the technology too new, despite excellent results.

In those pull requests and in private conversations, we speculated about
creating a decorator that would allow us to switch seamlessly between Cython,
Numba, and Pythran, using the same code, and select the method that gave the
best performance, potentially on a per-algorithm, per-machine basis. Last year,
Stéfan discovered Transonic and pointed it out to the rest of the team. Indeed,
someone else had independently encountered the same roadblocks and was creating
exactly the tool we needed.

By allowing us and the rest of the scientific Python ecosystem the possibility
to experiment with different compilers/accelerators without the risk and
commitment of a heavyweight dependency, Transonic (which is pure Python) has
the potential to advance the state of high performance computing for all of
scientific computing in Python. Simultaneously, an influx of new users to Numba
and Pythran can result in major improvements in those libraries, benefiting all
users.

In short, the scikit-image team supports this application and would continue to
collaborate with these projects to accelerate scikit-image, simplify its code
base, and help ensure that the ease of use of these accelerators is suitable
for the ecosystem more widely.

Juan Nunez-Iglesias, CZI Imaging Software Fellow, Monash University

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

## Sylvain Corlay

The relative slowness of the Python programming language has forced the developers
of scientific applications to rely on high-level tools for array computing such
as NumPy, which delegates the bulk of the operations to a compiled module.
The fact that the entire community relied on a common abstraction layer
facilitated the use of other accelerators such as GPU-based solutions (such as
CuPy) and parallel computing frameworks (such as Dask).

For more ad-hoc applications, where custom operations are still required, C speed is
generally achieved using one of the most common accelerators such as Cython, Pythran,
and Numba. Cython is very heavily used in projects such as scikit-learn, while Pythran
and Numba are generally used by end-users to quickly accelerate performance-sensitive
parts of their applications.

For a major open-source project, adopting a specific accelerator rather than another
is a difficult decision. Numba relies on LLVM and a significant compiler
infrastructure while Pythran transpiles the code to C++ for greater speed, and Cython requires
type annotations in the codebase. The transonic abstraction layer mitigates that risk and
offers a common front-end to all accelerators. It may also correspond to the right level of
abstraction for Python accelerators.

I support this application that will help consolidate Python accelerators which are
already key to the Python scientific computing ecosystem and broaden their adoption.
I am especially excited to see more adoption of Pythran, which in my experience has shown
impressive performances across the board, especially in codes mixing classic loops and
vectorized operations.

Sylvain Corlay, Jupyter Core Developer, NumFOCUS Director, Founder and CEO of QuantStack

[^1]: <https://mail.python.org/archives/list/scikit-image@python.org/message/N5OQERDWVYZVVJVOPXXE7ISIIQB32BWG/>

[^2]: <https://github.com/scikit-image/scikit-image/issues/2956>

[^3]: <https://github.com/scikit-image/scikit-image/pull/3226>
