Architecture
============

The [repository of this documentation](https://github.com/weber-s/code_example_ige)
use sphinx-gallery to build html page from python code. The repo has the
following architecture:

```
├── CONTRIBUTING.md
├── README.md
├── docs
│   ├── Makefile
│   ├── _build
│   ├── _static
│   ├── auto_examples_code
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── examples_code
│   ├── README.txt
│   ├── basic
│   │   ├── README.txt
│   │   ├── ...
│   ├── time
│   │   ├── README.txt
│   │   ├── ...
│   └── ...
└── requirements.txt
```

Every example (notebook or python) are stored in `examples_code/<something>`.
The html page are stored into the `docs/` folder.

How to contribute?
==================

There is **no need to be an expert in python** nor in sysadmin to easily contribute
to this documentation. Indeed, you can simply upload a jupyter-notebook into the
[examples_code](https://github.com/weber-s/code_example_ige/examples_code)
folder in github and *tada*, it will work.


For those who don't like jupyter, you can also upload a `.py` file. However, the
format is a bit special. Follow the
[sphinx-gallery documentation](https://sphinx-gallery.readthedocs.io/en/latest/syntax.html#)
or see the code of
[examples_code/basic/plot_basic.py](https://github.com/weber-s/code_example_ige/examples_code/basic/plot_basic.py).

To sum up:

1. create your example either with jupyter-notebook or directly in python
2. upload your example to `examples_code/<yourfavoritepath>` (mannualy via [github](https://github.com/weber-s/code_example_ige/) or git)
3. (optional) create a new example and go to 2.

How to build the documentation?
===============================

If you want to build locally the documentation, you will need some python tools.
First, get the repository

    git clone https://github.com/weber-s/code_example_ige/

Then, go to this folder, create a virtual environment and populate it with
the requirements.

    cd code_example_ige
    python3 -m venv
    source venv/bin/activate
    pip3 install -r requirements.txt

To build the documentation, go to the `docs` folder and run the makefile with
the html option.

    cd docs
    make html

You should now have a `_build/` folder into `docs/`. Open `_build/html/index.html`
with your favorite browser:

    firefox _build/html/index.html

and *Tada*.

Every time you add something to `examples_code`, don't forget to re-build the docs
with `make html` (in the `docs` folder). 
