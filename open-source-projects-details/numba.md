# Software Project Details

Complete the following for each software project that will be supported by the
grant:

- Software project name: Numba
- Homepage URL: https://numba.pydata.org
- Hosting platform (GitHub, GitLab, Bitbucket, Other): GitHub
- Main code repository (e.g. GitHub URL): https://github.com/numba/numba/
- DOI of major publication(s) describing software project (if applicable): 10.1145/2833157.2833162
- Social media handles (if applicable): Twitter @numba_jit
- Do you or software project key personnel have commit rights to the code repositories for this software project?: Yes, Val Haenel (key personnel for this grant) has commit rights
- Short description of the software project (maximum of 200 words):

Numba is a just-in-time compiler for Python functions based on the LLVM
compiler library. Numba is focused on numerical and scientific use cases,
supporting a subset of Python built-in types as well as NumPy arrays and
functions.  Numba can be used to generate and execute optimized machine code
on several CPU targets (x86, x86_64, ARMv7, ARMv8, PPC) and GPU targets
(NVIDIA and AMD).  Additionally, Numba supports more advanced code generation,
like automatic multithreading, generation of array functions for CPU and GPU
targets, and creation of C callbacks for external libraries.


# List of Known Key Personnel

- Name: Val Haenel
- Email address: vhaenel@anaconda.com
- Current employer: Anaconda
- Job title: Software Engineer
- Developer username if applicable (e.g., GitHub handle): esc
- Country of Residence: Germany
- Do any of the Key Personnel self-identify as one of the following? (optional): Male

# Software Project Metrics

## Quality (required)

- What is the software project license?
    - BSD 2-clause

- What is the main programming language?
    - Python

- Does the software project have a code of conduct?
    - It does not, currently.  This will be done during Q1 2020.

- Does the software project have end-user documentation?
    - http://numba.pydata.org/numba-doc/latest/index.html

- Does the software project have an issue tracker?
    - https://github.com/numba/numba/issues

- Does the software project have a community engagement/Q&A forum:
    - Mailing list: https://groups.google.com/a/continuum.io/forum/#!forum/numba-users
    - Gitter (realtime user Q&A): https://gitter.im/numba/numba
    - Gitter (realtime dev discussion): https://gitter.im/numba/numba-dev

- Does the software project have contribution/coding guidelines?:
    - http://numba.pydata.org/numba-doc/latest/developer/contributing.html

- Are there examples or demo notebooks, scripts, and datasets? If yes, provide a link.
    - https://mybinder.org/v2/gh/numba/numba-examples/master?filepath=notebooks

- Is there a corresponding package available in a package manager (PyPi, CRAN, etc.)?:
    - PyPI: https://pypi.org/project/numba/
    - conda: `numba` package in Anaconda Distribution and Conda-forge

- Does the software project use continuous integration for testing?
    - Yes, Azure Pipelines for rapid testing of pull requests and an internal
      system for full testing of different Python, NumPy and platform/OS
      combinations.

## Impact (optional)

### List the number and explanation for each, if needed:

- Number of scholarly paper(s) (including preprints) citing or mentioning the software project:
    - 60 paper citations (as per https://dl.acm.org/doi/10.1145/2833157.2833162)

- Number of monthly users
    - 800,327 PyPI package downloads (preceeding 30 days, from https://pypistats.org/packages/numba)
    - 314,687 conda package downloads (Dec 2019)

- Number of software projects that depend on the software project
    - 13,272 repositories and 579 packages on GitHub (https://github.com/numba/numba/network/dependents)

- Number of monthly visitors to software project’s website, discussion forum (e.g. Stack Overflow, Discourse), or similar
    - Gitter: 392 users in Numba Q&A channel and 46 users in Numba development channel

### Size of the largest potential user base:

- Estimate the potential number of unique users who could adopt this software project in the relevant field/discipline and explanation, if needed. You can use as guidance the number of users of comparable software projects, the number of papers published in the domain to which the software project is applicable, number of labs able to adopt the software project, etc.

    - Many users benefit from Numba when other Python projects use it to accelerate their implementations.  This puts Numba's potential indirect user base over 100,000 users.  Direct users of Numba are in the 10,001-100,000 scale, as suggested by the GitHub dependent repository count.

- List of upstream, downstream, or related software projects that the team is contributing to or receiving contributions from.
    - Numba is a core dependency for packages like:
        - UMAP
        - LibROSA
        - RAPIDS
        - Awkward Array
    - Numba will be an optional dependency of Pandas starting with the 1.0 release.