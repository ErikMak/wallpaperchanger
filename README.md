# :snowflake: WallpaperChanger
Десктопное приложение, взаимодействующее с системным временем. В зависимости от времени года и времени суток предлагает соответсвующие обои рабочего стола, которые можно установить через интерфейс программы. 

Разработано на Python с использованием PyQT 5.


## :hammer_and_wrench: Зависимости
Package | Version
--- | ---
[Python](https://www.python.org/) | V3.12+
[pip](https://pypi.org/project/pip/)  | V23.3.1+ 
[PyQT](https://pypi.org/project/PyQt5/)  | V5.15.9+
[pyinstaller](https://pyinstaller.org/en/stable/)  | V6.3.0+

## Установка

1. Скопируйте репозиторий, чтобы работать с ним локально. Для этого выполните следующую команду
    ```sh
    git clone https://github.com/ErikMak/wallpaperchanger.git
    ```
2. Переместитесь в корневую папку проекта - `wallpaperChanger`
    ```sh
    cd wallpaperChanger
    ```
3. Установите зависимости
    ```sh
    pip install -r requirements.txt
    ```
4. Запустите сборку проекта командой
    ```sh
    pyinstaller --onefile --noconsole main.py
    ``` 
5. Запустите `main.exe` файл в созданной папке `build`

## Скриншоты
### Интерфейс приложения

<img height='300px' src='https://github.com/ErikMak/wallpaperchanger/assets/90393934/63dd5f9b-f61d-47b5-a501-7afd06e19cb8'>
