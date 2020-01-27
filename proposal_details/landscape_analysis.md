A particularity of the Joint Python Accelerators project is to gather different
Python accelerators for better interoperability and compatibility in particular
with the Transonic package, which allows one code to be run with different
accelerators. We are not aware of other projects similar to Transonic and the
Joint Python Accelerators project.

There are of course several projects whose goal is to run Python codes
efficiently. A serious review on this topic <http://tiny.cc/transonic-vision>
has been written by Transonic developers.

With the Joint Python Accelerators project, we focus on accelerating numerical
Python codes using the Numpy API. On the one hand, this API is used in several
numerical Python projects and on the other hand, it is very difficult for
alternative Python implementations (for example PyPy) to accelerate Numpy
code because Numpy uses internally the C-API of CPython, which exposes a lot of
internal details of CPython.

A new project called [HPy](https://github.com/pyhandle/hpy) has the goal to
design a new API more friendly for other implementations. A [proof of
concept](https://morepypy.blogspot.com/2019/12/hpy-kick-off-sprint-report.html)
demonstrates that HPy is very promising. Accelerators participant to our
project (in particular Cython) will have to be able to use this new C-API so
that the resulting extensions could be efficient with different Python
implementations. However, HPy has to mature a lot before anything can be done
on Cython side and in Numpy code.

Travis Oliphant just announced the creation of a new project called
[EPython](https://github.com/epython-dev/epython) to write using the Python
language extensions efficient with different Python implementations.
