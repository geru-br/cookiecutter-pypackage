{% set is_open_source = cookiecutter.license != 'GERU Intelectual Property' -%}
{% set is_geru_license = cookiecutter.license == 'GERU Intelectual Property' -%}

{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}
{% if is_open_source %}
* Free software: {{ cookiecutter.license }}
* Documentation: see `README` at https://github.com/geru-br/{{ cookiecutter.project_slug }}
{% endif %}

Installation
============

1. Go to directory and, install the lib

```
pip install {{ cookiecutter.project_slug }}
```

2. Just code with it. Inside you python app:

```
import {{ cookiecutter.project_slug }}
```

* TODO: Review the Installation section


How to contribute
=================

* Assumptions:
  * Python {{ " or ".join(cookiecutter.python_poetry_dependencies_versions.split(',')) }} installed.

1. Clone the lib (and go to directory)

```
git clone https://github.com/geru-br/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
```

2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install poetry

```
pip install poetry=={{ cookiecutter.poetry_version }}
```

4. Install project

```
make install
```

5. Run tests

```
make test-all
```

6. Bump version

To bump a minor version, just run:

```
make bump-version
```

If you need to generate a `major`, `patch` or another different version you can read [here](https://poetry.eustace.io/docs/cli/#version) for details.


Rationale
=========

* TODO: Insert here relevant information about project's structure, concepts and operation. Get a nice example from https://github.com/geru-br/arkham/blob/master/README.md.


Credits
=======

This package was created with Cookiecutter_ and the `geru-br/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`geru-br/cookiecutter-pypackage`: https://github.com/geru-br/cookiecutter-pypackage
