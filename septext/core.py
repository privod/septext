class Septext:

    def __init__(self, sep, file_name=None, text=None):
        self._sep = sep

        if file_name is not None:
            with open(file_name, mode='r') as file:
                text = file.read()

        if text is None:
            return

        line_list = text.splitlines()

        if len(line_list) > 0:
            self._header = line_list[0].split(sep)                             # Первая строка - заголовок
            if len(line_list) > 1:
                self._data = [line.split(sep) for line in line_list[1:]]        # Остальные строки - данные

    def get_line_list(self):
        return [self._sep.join(line) for line in self._data]

    def get_array(self):
        return self._data

    def count(self):
        return len(self._data)

    def get_dict(self, index):
        return {key: val for key, val in zip(self._header, self._data[index])}


    def get_dict_list(self):
        return [self.get_dict(index) for index in range(self.count())]
