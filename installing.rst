.. _installing:


Installing
==========

python.org
----------

You can get far with Python 3.6 or 3.7, installed from python.org:

https://www.python.org/downloads/

Once you have that installed, you can get the extra add-on packages you need with the Python package installer: ``pip``.

You should be able to do::

    pip install numpy
    pip install scipy
    pip install jupyter
    pip install pandas

You can also use pip to install a wide variety of other extra packages for Python -- web development frameworks, what have you.

An introduction on how to do this all this installing is available here:

https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/index.html

However, once you get beyond the core "scipy stack", a number of scientific computing packages cannot be easily installed with pip. (because they require compiling, or external third party libraries, etc.) So a full-service option is in order:


Anaconda / conda
----------------

https://www.anaconda.com/distribution/

"conda" is a general purpose package manager. It is written in Python, and has many python-focused features, but it can be used to manage virtually type of software package, including PYthon and conda itself. As such it is very useful for scientific computing, as it can handle not only the Python packages, but also third-party libraries and utilities you need for your work. As many of these extras need to be compiled and installed in special ways, conda makes it much easier than installing by hand.

In addition, conda provides isolated "environments", which allow you to have different versions of software for different projects.

"Anaconda" is a full-featured distribution of Python and many conda packages required for scientific computing. It is a large install, but makes it easy to get started with everything you are likely to need all at once. As it is based on the conda system, it can be extended and used in the same way as your needs grow.












