install: # Установка зависимостей проекта через poetry
	poetry install


brain-games: # Запуск скрипта brain-games
	poetry run brain-games


build: # Сборка проекта
	poetry build


publish: # Отладка публикации проекта как пакета 
	poetry publish --dry-run


package-install: # Установка пакета на компьютер
	python3 -m pip install --user dist/*.whl

make-lint:
	poetry run flake8 brain_games