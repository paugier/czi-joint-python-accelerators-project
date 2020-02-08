# Joint Python Accelerators Project application (CZI program)

The Joint Python Accelerators project gathers developers of
[Transonic](transonic.readthedocs.io/), Cython, Pythran and Numba namely:

- Pierre Augier (Transonic)
- Serge Guelton (Pythran)
- Stefan Behnel (Cython)
- Stanley Seibert (Numba)

This project has been initiated by core-developers of scikit-image (Juan
Nunez-Iglesias, Emmanuelle Gouillart and Stéfan van der Walt).

## Abstract

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

See also the [detailed work
plan](https://github.com/paugier/czi-joint-python-accelerators-project/blob/master/proposal_details/workplan.md).

## Application

Here is the call for proposals for the CZI program:

https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/

Lots of info on that site. There is also a SciPy 2019 talk about the program by
Jeremy Freeman, who leads the computational biology division at CZI:

https://www.youtube.com/watch?v=Zu_MmxdEW0M

For administrative and programmatic inquiries pertaining to this RFA, please
contact sciencegrants@chanzuckerberg.com.

This proposal has been submitted on Feb. 4 2020 (application ID number
EOSS2-0000000137).

## Dates

Portal opening date
Mid-December 2019

Application due date
February 3, 2020

Notification of decisions
Late April 2020

Earliest start date of grant
June 1, 2020

## Detailed Application Instructions

The Chan Zuckerberg Initiative uses SurveyMonkey Apply (SMApply) as its grants
management portal. All applications must be submitted through this portal
(https://apply.chanzuckerberg.com). SMApply is configured to work best using
the Google Chrome browser. It is recommended that you familiarize yourself with
this portal well in advance of any deadlines. Deadline extensions will not be
granted.

For the purpose of the application, we will use the following terms:

- Applicant: The person submitting the application materials on behalf of the software project(s)

- Organization: The organization directly receiving and distributing funding

- Software Project(s): The software project(s) that will be supported by the funding

- Proposal: The proposed use of funding

- Key Personnel: People involved in the software project(s) described in the
proposal and supported by the funding

The application consists of the following sections (called tasks in the grants
portal): Applicant Details Part I, Applicant Details Part 2, Organization
Details, Proposal Details, Optional Attachments, CV of Applicant, Budget
Description, Number of Open Source Software Project(s), Open Source Software
Project Details