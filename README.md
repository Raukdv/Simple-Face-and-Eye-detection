# Simple-Face-and-Eye-detection
Just a simple scripts to face and eye detection using OpenCV

Solo necesitas instalar el "requeriments.txt"
y ejecutar desde la consola/termianl/bash como quieras llamarlo.
El "main.py"




Si tienes problemas con el numpy usa en la terminal: 
python -c "import numpy;print(numpy.__version__);print(numpy.__file__)";

Con esto podras ver en que version estas

ImportError: numpy.core.multiarray failed to import
este error puede ser causado al usar Python 3.9 y Numpy 1.19.4 (Ultima version segun la fecha de subido este script)

Si tu version es de 1.19.4, desintalala e isntala pip install numpy==1.19.3
Esto deberia mitigar el siguiente error.
https://stackoverflow.com/questions/20518632/importerror-numpy-core-multiarray-failed-to-import


numpy fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information
https://stackoverflow.com/questions/64654805/how-do-you-fix-runtimeerror-package-fails-to-pass-a-sanity-check-for-numpy-an

Para ambos errores de Numpy, me basto con instalar una version anterior.


Error al cerrar la ventana:
opencv `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
La solucion esta dentro del "main.py".

Esto se debe a un Bug del backend para ciertos OS, en mi caso windows, no deberia aparecer en otros OS que no sean windows
segun la documentacion oficial. Como sea el caso, la solucion es simple para windows.
https://stackoverflow.com/questions/60007427/cv2-warn0-global-cap-msmf-cpp-674-sourcereadercbsourcereadercb-termina



