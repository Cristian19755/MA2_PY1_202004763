# MA2_PY1_202004763
PROYECTO 1 del curso Matematica aplicada 2 2S 2023

## Requisitos
1. Los audios se encuentran en formato wav, por tanto se puede acceder a ellos sin necesidad de herramientas externas al OS.
2. Para ejecutar los archivos de python es necesario tener una version mayor a la 3.6 de dicho programa. https://www.python.org/
3. Instalacion de la librerias necesarias (se debe de ejecutar en una consola de powershell):
     pip install numpy
     pip install mathplotlib
     pip install tkinter
     pip install wave
4. Se recomienda el uso de VSCode como IDE para su ejecucion https://code.visualstudio.com/

## Uso de EJ_Audio.py
1. Al iniciar la aplicacion se mostraran dos imagenes, la primera perteneciente al espectro defrecuencia del sonido (que para el oido humano pareciera constante) mientras que en la otra imagen se mostrara el resultado de aplicar la Transformada rapida de fourier. Ademas se mostrara un slidebar con un numero inicial de 440, este slidebar representa en Hz la frecuencia que tendra el sonido. Mientras que en la parte inferior se mostraran dos botones, el primero Guarda en un archivo con formato wav el audio correspondiente a la frecuencia seleccionada en el slidebar y el otro cerrara la aplicacion (Forma recomendada para cerrarla).
