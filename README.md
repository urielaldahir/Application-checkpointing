Calculadora cientifica , la cual lleva implementada consigo un checkpoint para poder guardar su status si el usuario cierra la interfaz de manera intencional o no intencional.

<img src="https://github.com/user-attachments/assets/24cf0198-8f5a-4850-9aaf-2ea8343cf65d" width="300" />


Funciones save_state y load_state:
save_state(entry, history): Guarda el texto actual de la entrada y el historial en un archivo llamado calculator_state.pkl utilizando pickle.
load_state(): Intenta cargar el estado del archivo calculator_state.pkl. Si no existe el archivo (es decir, cuando se ejecuta por primera vez), devuelve valores vacíos.

Carga del estado inicial:
Al crear la ventana principal, los valores de entrada y el historial se cargan utilizando la función load_state() y se asignan a las variables entry_var y history_var.

Guardar el estado al cerrar:
Se ha agregado un manejador de eventos con root.protocol("WM_DELETE_WINDOW", on_close) para garantizar que cuando se cierre la ventana, el estado se guarde en el archivo.
