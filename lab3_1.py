class Reader:
    def __init__(self, filenames):
        self.variables = {}
        self.current_vars = {}
        self.stack = []
        self.file_names = filenames
        self.i = -1
        self.process_files(file_names)

    def process_files(self, file_names):
        for file_name in file_names:
            with open(file_name, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()
                    if line.startswith('ShowVar;'):
                        self.show_vars()
                    elif '=' in line:
                        var_name, value = line.split('=')
                        var_name = var_name.strip()
                        value = int(value.strip().replace(';', ''))
                        self.enter_val(var_name, value)
                    elif line == '{':
                        self.start_scope()
                    elif line == '}':
                        self.end_scope()

    def show_vars(self):
        print("variables: ", self.variables)

    def enter_val(self, var_name, value):
        self.variables[var_name] = value
        self.stack[self.i][var_name] = value

    def start_scope(self):
        self.i += 1
        scope_variables = {var: self.variables.get(var, None) for var in self.variables}
        self.stack.append(scope_variables.copy())

    def end_scope(self):
        if self.stack:

            self.stack.pop()
            if len(self.stack) > 0:
                self.variables = self.stack[-1]
            else:
                self.variables = {}
            self.i -= 1

file_names = ['file1_1.txt']
reader = Reader(file_names)