install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check

fix-lint:
	uv run ruff check --fix

test:
	uv run pytest
