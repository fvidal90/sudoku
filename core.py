class Casilla:
    def __init__(self, value=None):
        self.value = value if value else -1
        self.possible_values = {value} if value else {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def get_defined_value(self):
        return self.value != -1

    def can_define_value(self):
        return len(self.possible_values) == 1

    def update_value(self, value):
        self.value = value
        self.possible_values = {value}

    def define_value(self):
        self.value = next(iter(self.possible_values))

    def update_possible_values(self, just_defined_values):
        self.possible_values = self.possible_values - just_defined_values


class OneToNineSet:
    def __init__(self, elements):
        self.defined_values = set()
        self.elements = elements

    def update_defined_values(self):
        for element in self.elements:
            if element.value != -1:
                self.defined_values.add(element.value)
                self.elements.remove(element)

    def define_element_value(self):
        for i in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            if i not in self.defined_values:
                aux = set()
                for element in self.elements:
                    if i in element.possible_values:
                        aux.add(element)
                if len(aux) == 1:
                    element = next(iter(aux))
                    element.update_value(i)

    def update_element_possible_values(self):
        for element in self.elements:
            if not element.get_defined_value():
                element.update_possible_values(self.defined_values)


class Tablero:
    def __init__(self, tabla):
        self.casilleros = []
        for i in range(9):
            self.casilleros.append([])
            for j in range(9):
                value = tabla[i][j]
                self.casilleros[i].append(Casilla(value))

        self.row_sets = []
        for i in range(9):
            aux = []
            for j in range(9):
                aux.append(self.casilleros[i][j])
            self.row_sets.append(OneToNineSet(aux))

        self.column_sets = []
        for i in range(9):
            aux = []
            for j in range(9):
                aux.append(self.casilleros[j][i])
            self.column_sets.append(OneToNineSet(aux))

        self.square_sets = []
        for i in range(9):
            aux = []
            i_d, i_r = i // 3, i % 3
            for j in range(9):
                j_d, j_r = j // 3, j % 3
                aux.append(self.casilleros[3 * i_d + j_d][3 * i_r + j_r])
            self.square_sets.append(OneToNineSet(aux))

    def get_values(self):
        return [[self.casilleros[i][j].value for j in range(9)] for i in range(9)]

    def get_possible_values(self):
        return [[self.casilleros[i][j].possible_values for j in range(9)] for i in range(9)]

    def complete_sudoku(self):
        for h in range(30):
            for i in range(9):
                for j in range(9):
                    if self.casilleros[i][j].can_define_value():
                        self.casilleros[i][j].define_value()

            for sets in [self.row_sets, self.column_sets, self.square_sets]:
                for one_to_nine_set in sets:
                    one_to_nine_set.update_defined_values()
                    one_to_nine_set.define_element_value()
                    one_to_nine_set.update_element_possible_values()
