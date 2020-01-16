# Software Project Details

Complete the following for each software project that will be supported by the
grant:

- Software project name: Pythran
- Homepage URL: https://pythran.readthedocs.io
- Hosting platform: GitHub
- Main code repository: https://github.com/serge-sans-paille/pythran
- DOI of major publication(s) describing software project: 10.1088/1749-4680/8/1/014001, 10.1109/MCSE.2018.021651342
- Social media handles: None
- Do you or software project key personnel have commit rights to the code repositories for this software project? yes
- Short description of the software project (maximum of 200 words)

  Pythran is an ahead of time compiler for a subset of the Python language, with a focus on scientific computing. It takes a Python module annotated with a few interface description and turns it into a native Python module with the same interface, but (hopefully) faster.
  It is meant to efficiently compile scientific programs, and takes advantage of multi-cores and SIMD instruction units

# List of Known Key Personnel

Key personnel are people involved in the software project who will be supported by the grant if the application is successful. Complete the following for each (up to 5) (required); enter n/a if any field is not applicable. Personnel to be hired that has not been identified at this time can be listed in the budget section. You may need to use the scroll bar at the bottom of the table to scroll right to view and to complete all fields. Alternatively, you can tab to move through and complete the fields. To add another person/row (up to five), click the box at the end of the row. We collect (optional) gender statistics about the applicant team in order to study the gender diversity of teams applying for funding and to learn about diversity trends in the field. We will not consider these gender statistics as part of final grantmaking decisions.

- Name: Serge Guelton
- Email address: serge.guelton@telecom-bretagne.eu
- Current employer: n/a
- Job title: Compiler engineer
- Developer username if applicable: serge-sans-paille
- Country of Residence: France

- Do any of the Key Personnel self-identify as one of the following? Male

# Software Project Metrics

## Quality (required)

- What is the software project license? BSD 3-Clause

- What is the main programming language? Python, C++

- Does the software project have a code of conduct? No

- Does the software project have end-user documentation? https://pythran.readthedocs.io

- Does the software project have an issue tracker? https://github.com/serge-sans-paille/pythran/issues

- Does the software project have a community engagement/Q&A forum (self-hosted, on Stack Exchange, etc.)?
    https://stackoverflow.com/questions/tagged/pythran
    https://www.freelists.org/archive/pythran/

- Does the software project have contribution/coding guidelines? https://pythran.readthedocs.io/en/latest/DEVGUIDE.html

- Are there examples or demo notebooks, scripts, and datasets? https://github.com/serge-sans-paille/pythran/tree/master/pythran/tests/cases

- Is there a corresponding package available in a package manager (PyPi, CRAN, etc.)?
    PyPI: https://pypi.org/project/pythran/
    Conda: https://anaconda.org/conda-forge/pythran

- Does the software project use continuous integration for testing? yes

## Impact (optional)

PyPI download stats: https://pypistats.org/packages/pythran
Conda download stats: https://anaconda.org/conda-forge/pythran/files
Github used-by stats: https://github.com/serge-sans-paille/pythran/network/dependents?package_id=UGFja2FnZS01MjYyODI5Mg%3D%3D
Github stargazers stats: https://github.com/serge-sans-paille/pythran/stargazers

### List the number and explanation for each, if needed:

- Number of scholarly paper(s) (including preprints) citing or mentioning the software project:
    Citing "Pythran: Enabling static optimization of scientific python programs": 23 (source: https://scholar.google.com/scholar?cites=17616677777113619733)
    Citing "Pythran: Crossing the Python Frontier": 7 (source: https://scholar.google.com/scholar?cites=1751600828312689671)

- Number of monthly users, if applicable (based on one or more of the
following: monthly downloads from websites, monthly downloads from package
managers, monthly unique requests for updates, actual tracked usage, etc.)
    PyPi: ~2200 (based on https://pypistats.org/packages/pythran, 2020/01/16)
    Conda: ~500 (based on https://anaconda.org/conda-forge/pythran/files, 2020/01/16)

- Number of software projects that depend on the software project (if applicable)
    28 repo, 7 packages (based on https://github.com/serge-sans-paille/pythran/network/dependents?package_id=UGFja2FnZS01MjYyODI5Mg%3D%3D, 2020/01/16)

- Number of monthly visitors to software project’s website, discussion forum (e.g. Stack Overflow, Discourse), or similar
    n/a

### Size of the largest potential user base:

- Estimate the potential number of unique users who could adopt this software project in the relevant field/discipline and explanation, if needed. You can use as guidance the number of users of comparable software projects, the number of papers published in the domain to which the software project is applicable, number of labs able to adopt the software project, etc.

   over 100,000 (based on the monthly stats of scikit-image, https://pypistats.org/packages/scikit-image, 2020/01:16)


List of upstream, downstream, or related software projects that the team is contributing to or receiving contributions from.

- gast (main author, https://github.com/serge-sans-paille/gast)
- beniget (main author, https://github.com/serge-sans-paille/beniget)
- xtensor stack (contributor, https://github.com/xtensor-stack/)

Additional metrics from software project code repositories and package managers:

Provide a short description of any considerations or caveats we should be aware of when computing metrics (e.g., a recent change in the name or hosting of the repository), or any additional information you would like to share about the software project’s impact and quality (maximum of 500 words)

http://pythonhosted.org/pythran/ used to host python homepage, it has been dismissed two years ago in favor of https://pythran.readthedocs.io
