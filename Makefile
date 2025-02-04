update-requirements:
	uv pip compile setup.py -o requirements/requirements.txt
	uv pip compile requirements/requirements-dev.in -o requirements/requirements-dev.txt

upgrade-requirements:
	uv pip compile --upgrade setup.py -o requirements/requirements.txt
	uv pip compile --upgrade requirements/requirements-dev.in -o requirements/requirements-dev.txt

sync-venv: update-requirements
	uv pip sync requirements/requirements.txt requirements/requirements-dev.txt
	uv pip install -e .

# create virtual env and install deps
init:
	uv venv

	uv pip install -r requirements/requirements-dev.txt
	uv pip install -r requirements/requirements.txt

	uv pip install -e .
	# python3 -m pre_commit install --install-hooks --overwrite

lint:  # lint all source code
	@uvx ruff check --config=pyproject.toml

format:  # format all source code
	@uvx ruff check --fix --config=pyproject.toml