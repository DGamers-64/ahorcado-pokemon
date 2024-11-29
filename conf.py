import curses
import json

def menu(stdscr):
    curses.curs_set(0)
    opciones = list(range(1, 10))  # Opciones numéricas del 1 al 9
    seleccionados = set()
    indice = 0

    while True:
        stdscr.clear()
        for i, opcion in enumerate(opciones):
            marcado = "[x]" if i in seleccionados else "[ ]"
            prefijo = "> " if i == indice else "  "
            stdscr.addstr(i, 0, f"{prefijo}{marcado} {opcion}", curses.A_REVERSE if i == indice else 0)
        stdscr.addstr(len(opciones) + 2, 0, "Flechas para moverte, ESPACIO para seleccionar, ENTER para finalizar.")
        
        tecla = stdscr.getch()
        if tecla == curses.KEY_UP:
            indice = (indice - 1) % len(opciones)
        elif tecla == curses.KEY_DOWN:
            indice = (indice + 1) % len(opciones)
        elif tecla == ord(' '):
            if indice in seleccionados:
                seleccionados.remove(indice)
            else:
                seleccionados.add(indice)
        elif tecla == ord('\n'):
            return [opciones[i] for i in seleccionados]

if __name__ == "__main__":
    seleccionados = curses.wrapper(menu)
    resultado = {"seleccionados": seleccionados}
    
    with open("config.json", "w") as archivo:
        json.dump(resultado, archivo, indent=4)
    
    print(f"\nSelección guardada en 'config.json': {resultado}")
