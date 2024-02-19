from core import Tablero


def print_tablero():
    """tabla = [
        [8, None, None, None, None, None, None, None, None],
        [None, None, 3, 6, None, None, None, None, None],
        [None, 7, None, None, 9, None, 2, None, None],
        [None, 5, None, None, None, 7, None, None, None],
        [None, None, None, None, 4, 5, 7, None, None],
        [None, None, None, 1, None, None, None, 3, None],
        [None, None, 1, None, None, None, None, 6, 8],
        [None, None, 8, 5, None, None, None, 1, None],
        [None, 9, None, None, None, None, 4, None, None]
    ]"""
    tabla = [
        [None, None, None, None, None, 2, None, None, None],
        [7, 3, None, None, 5, None, 1, None, None],
        [None, 1, None, None, None, None, 5, 3, None],
        [5, None, None, None, 4, None, None, None, None],
        [3, 4, 2, None, None, None, None, None, None],
        [None, None, None, 8, 6, None, None, 5, None],
        [9, None, None, None, None, 1, None, None, None],
        [None, None, None, 4, 3, None, None, None, 6],
        [None, None, None, None, None, None, 8, None, None]
    ]
    tablero = Tablero(tabla)
    tablero.complete_sudoku()
    print(tablero.get_values())  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_tablero()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
