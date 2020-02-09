.. --------------------------------License Notice----------------------------------
.. Python Project Boilerplate - A boilerplate project for python packages
..
.. Written in 2018 by Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>
..
.. To the extent possible under law, the author(s) have dedicated all copyright
.. and related and neighboring rights to this software to the public domain
.. worldwide. This software is distributed without any warranty.
..
.. You should have received a copy of the CC0 Public Domain Dedication along
.. with this software. If not, see
.. <http://creativecommons.org/publicdomain/zero/1.0/>.
.. --------------------------------License Notice----------------------------------

A boilerplate project for python packages
#########################################

A boilerplate project to use when bootstrapping new Python 3 projects.
Copy the source code (no need to fork it), edit all occurrences of ``project_name``, tweak the
``setup.py`` file to suit your needs and start doing things.

Features
********

* Test automation and environment provisioning using `Tox <https://tox.readthedocs.io/>`_
* Static code analysis using `Flake8 <http://flake8.pycqa.org/en/latest/>`_ with useful plugins and
  sane defaults
* Static type checking using `Mypy <http://mypy-lang.org/>`_
* Unit testing using `pytest <https://docs.pytest.org/en/latest/>`_
* Enforced code coverage threshold using `coverage <https://coverage.readthedocs.io>`_
* Dependencies pinned to the major version, allowing for backwards-compatible updates when upstream
  projects respect `Semantic Versioning <https://semver.org/>`_
* Costless continuous integration for Open-Source projects using `Travis-CI <https://travis-ci.org/>`_
* Costless code coverage reports for Open-Source projects using `Coveralls <https://coveralls.io/>`_
* Project dependencies are checked for security vulnerabilities using `Safety <https://pyup.io/safety/>`_
* Licensed under `CC0 Public Domain Dedication <http://creativecommons.org/publicdomain/zero/1.0/>`_,
  you can copy/paste anything and not worry about a thing, not even giving original authors attribution.

Usage
*****

*Remember only to follow those instructions after editing the source code to bootstrap your new
project.*


Licensing
*********

Written in 2018 by Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>

To the extent possible under law, the author(s) have dedicated all copyright
and related and neighboring rights to this software to the public domain
worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along
with this software. If not, see http://creativecommons.org/publicdomain/zero/1.0/.



### Run the application

```shell
pipenv install
pipenv shell
flask run
```

### Run test suite

```shell
pipenv shell
tox
```
