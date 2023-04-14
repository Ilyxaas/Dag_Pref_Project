# Dag_Pref_Project
Для запуска в PyCharm.
Установить в виртуальное окружение модули. 

python = "^3.9"
click = "^8.1.3"
dagster = "^1.1.18"
prefect = "^2.8.0"
pandas = "^1.5.3"
urllib3 = "^1.26.14"

и запустить 
poetry run task (По умолчанию)

либо
poetry run task --tool dagster --file_in original.csv --file_out norm.csv

Для этого в проекте файлы original.csv и norm.csv. продублированны.
Одни в корневой папке. Их копии в папке data


