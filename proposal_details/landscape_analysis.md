# Landscape analysis

A distinguishing feature of the Joint Python Accelerators project is to gather different
Python accelerators for better interoperability and compatibility, in particular
using the Transonic package, which allows one code to be run with different
accelerators. We are not aware of other projects similar to Transonic and the
Joint Python Accelerators project.

There are several projects whose goal is to run Python code
efficiently. A serious review on this topic <http://tiny.cc/transonic-vision>
has been written by the Transonic developers.

With the Joint Python Accelerators project, we focus on accelerating numerical
Python codes using the NumPy API. We chose this because this API is used in
most numerical Python projects. Furthermore, it is very difficult for
alternative Python implementations (such as PyPy) to accelerate NumPy
code, because NumPy internally uses the C-API of CPython, which exposes a lot of
internal details of CPython.

A new project called [HPy](https://github.com/pyhandle/hpy) has the goal to
design a new API more friendly for other implementations. A [proof of
concept](https://morepypy.blogspot.com/2019/12/hpy-kick-off-sprint-report.html)
demonstrates that HPy is very promising. Accelerators participant to our
project (in particular Cython) will have to be able to use this new C-API so
that the resulting extensions could be efficient with different Python
implementations. However, HPy has to mature a lot before anything can be done
on Cython side and in NumPy code.

Travis Oliphant just announced the creation of a new project called
[EPython](https://github.com/epython-dev/epython) to write efficient extensions
in pure Python that work with different Python implementations. Again, this
project needs more time to mature to be considered as a target for this
proposal.
