# Milestones

TODO: refactor that!

## Phase 0 (June-December 2020)

- Solve Cython issues that are blockers for Transonic-Cython.

- New releases of Beniget, Gast and Transonic (cleaner and more robust
implementation).

- Demo package transonic_demo (repository and documentation).

- Pull-requests in skimage-experiments and scikit-image with simple use of
Transonic-Cython.

## Phase 1 (January 2020 - April 2021)

- Benchmarks on many numerical kernels (from scikit-image and other projects).
These benchmarks should be reproducible on different platforms and the results
will be made available on a website. We will propose to developers using other
languages to submit their own implementations for comparison. This website
should become a reference for comparison of performances on real scientific
algorithms of different technical solutions (using Python and other langages).

- Releases of new Cython and Pythran versions with bugfixes, better Cython's
pure-Python mode and interoperativity.

- Pull-requests in skimage-experiments and scikit-image for faster kernels
using alternative backends.

## Dissemination of the results and communication

Good communication, targeting both developers of libraries and simple users, is
a key factor for the success of this project.  We will be very careful to spent
time on the documentations of Transonic and of the accelerators, and more
generally on communication through other channels:

- Dedicated online chat service and social media,

- Blog notes about the advancement of the project,

- One article presenting Transonic and the Joint Python Accelerators project
  submitted to the Journal of Open Source Software,

- Benchmark repository and website,

- Presentations and tutorials in Python conferences (in particular the SciPy
  conference, EuroSciPy, EuroPython, etc.).

It is a declared goal of this project to allow every simple user of Python
to easily get very good performance.  We will try to be as inclusive and
accessible as possible in our communication, and listen closely to our users
needs, above all (but not limited to) the ``scikit-image`` project.

Finally, we plan to organize a workshop after the end of this grant, featuring
tutorials and sprints.  We will invite developers of libraries which could use
our accelerators.  Part of this workshop will be dedicated to work on the PyPy,
HPy and EPython projects, which may become important for the future of
efficient computing with Python.  This event will be organized in Europe and may
be coupled with EuroSciPy or EuroPython to make it easy for interested people to
attend.
