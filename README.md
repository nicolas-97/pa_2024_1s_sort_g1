# Ejercicios algoritmos de ordenamiento | Programación Avanzada - Grupo 1

Este proyecto contiene implementaciones de algoritmos de ordenamiento para el curso de Programación Avanzada.

## Instrucciones para Clonar el Repositorio

1. Abre tu terminal.

2. Clona el repositorio ejecutando el siguiente comando:

    ```bash
    git clone https://github.com/nicolas-97/pa_2024_1s_sort_g1.git
    ```

3. Cambia al directorio del proyecto:

    ```bash
    cd pa_2024_1s_sort_g1
    ```

## Instrucciones para Codificar en el Módulo utils

Las implementaciones de los algoritmos de ordenamiento se encuentran en el módulo `utils/sort.py`. Puedes modificar o agregar código en este archivo según sea necesario.

## Instrucciones para Ejecutar las Pruebas Localmente

Asegúrate de tener Python instalado en tu sistema.

1. Abre una terminal en el directorio del proyecto.

2. Ejecuta las pruebas de Shell Sort:

    ```bash
    python -m unittest discover -s test -p "test_shell_sort.py"
    ```

3. Ejecuta las pruebas de Quick Sort:

    ```bash
    python -m unittest discover -s test -p "test_quick_sort.py"
    ```

4. Ejecuta las pruebas de Merge Sort:

    ```bash
    python -m unittest discover -s test -p "test_merge_sort.py"
    ```

Estos comandos ejecutarán las pruebas unitarias para los algoritmos de ordenamiento. Asegúrate de que todas las pruebas pasen antes de enviar cambios al repositorio.

## Crear una Rama y Subir Cambios

1. Crea una nueva rama para tus cambios:

    ```bash
    git checkout -b nombre-de-tu-rama
    ```

2. Realiza y guarda tus cambios.

3. Agrega y haz commit de tus cambios:

    ```bash
    git add .
    git commit -m "Descripción de tus cambios"
    ```

4. Sube tu rama al repositorio remoto:

    ```bash
    git push origin nombre-de-tu-rama
    ```

## Crear un Pull Request en GitHub

1. Abre tu navegador y ve a la página de tu repositorio en GitHub.

2. Cambia a la rama que acabas de crear.

3. Haz clic en "Compare & pull request".

4. Completa la descripción del pull request y haz clic en "Create pull request".

¡Listo! Has creado una rama, subido cambios y creado un pull request. Asegúrate de describir claramente tus cambios para que los revisores puedan entenRightlos fácilmente.
