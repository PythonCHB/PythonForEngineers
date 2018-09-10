.. _getting_started:

###############
Getting Started
###############

One of the tricky things with Python is getting started.

There are many pieces that must come together in order to get anything done, including:

* Getting Python and the libraries you need installed
* Figuring out how to edit and run your code
* Figuring out how to manage your own collection of code

And all that has nothing to do with the Python Language or libraries. For that you need:

* A basic understanding of the language

 - defining variables

 - how types work in Python

 - basic logical constructs:

   - looping

   - if/then

 - Defining functions


Installing
==========

The first step is getting everything installed. Try this page for some tips: :ref:`installing`


For the rest of this document, I'm going to assume that you have Python, iPython, Jupyter, and a programmers text editor all installed and working.


How to run Python Code
======================

There are a number of ways to run Python code -- here is a brief introduction:


iPython
-------

iPython is an "enhanced" interactive interpreter (REPL) for Python. It provides some very nice features that make it easy to experiment with little snippets of code.

`iPython introduction <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/IPythonIntroduction.html>`_

Running a python script
-----------------------

Once you get beyond experimentation, you'll want to put your code in a file so you can use ot over and over again, rather than retyping things in iPython.

A file with python code in it is a 'module' or 'script'

(more on the distinction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

If you want to run the code directly (it is a script), you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python3 the_name_of_the_script.py

2) On \*nix (linux, OS-X, Windows bash), you can make the file "executable"::

       $ chmod +x the_file.py

   And make sure it has a "shebang" line at the top::

       #!/usr/bin/env python

   Then you can run it directly::

       ./the_file.py

3) On Windows, the `.py` extensions can be associated with the python interpreter, so it can be run directly. This is clunkier than the \*nix "shebang line" approach, so I don't recommend it -- but it is an option.

4) run ``ipython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

5) Various IDEs (PyCharm, IDLE, etc) have a way to run the module you are currently editing -- if you use one of these tools, learn how to do that. Make sure that it is using the version of Python that you want it to be.

Jupyter Notebooks
-----------------

A Jupyter Notebook (http://jupyter.org/) is a browser-based system that allows you to intermix Python (and other languages) code and documentation, and graphical output in one place. Being browser based, notebooks can be run on your own system, or published on the web for others to see and use.

Notebooks are an excelent tool for interactive data analysis and learning and experimenting with python.

There ae many tutorials on the web -- here is just one:

https://www.dataquest.io/blog/jupyter-notebook-tutorial/


Basic Python Constructs
=======================

There are many tutorials on the internet to get started. Here is a brief overview:

https://uwpce-pythoncert.github.io/PythonCertDevel/modules/BasicPython.html

And here is more on function definitions:

https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Functions.html

"dictionaries" are a very useful built-in Python data structure:

https://uwpce-pythoncert.github.io/PythonCertDevel/modules/DictsAndSets.html


How to manage your own Code
===========================

Once you start doing something useful with Python, you will likely find that you have a small collection of code that you want to be able to re-use in multiple projects.

**Do not copy and paste that code all over the place**

Try this instead:

`Where to put your custom code <http://pythonchb.github.io/PythonTopics/where_to_put_your_code.html>`_





