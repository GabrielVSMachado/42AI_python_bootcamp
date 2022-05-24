class CsvReader(object):
    def __read_csv(self, filename: str, sep: str) -> list:
        """
        Read all line from csv file
        """
        try:
            data: list = []
            for line in open(filename, 'r'):
                data.append(
                        [line.strip(' \t\r\v\n"')
                            for line in line.split(sep=sep)]
                )
            if [line for line in data if len(line) != len(data[0])]:
                return None
            return data
        except FileNotFoundError:
            return None

    def __init__(
            self, filename: str = None, sep: str = ',',
            header: bool = False, skip_top: int = 0,
            skip_bottom: int = 0) -> None:
        self.data: list = self.__read_csv(filename, sep)
        self.header: list = self.data[0] if header and self.data else None
        self.skip_top: int = skip_top
        self.skip_bottom: int = skip_bottom

    def __enter__(self: object) -> object:
        if self.data is None:
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return False

    def getdata(self: object) -> list:
        """
        Retrieves the data/records from skip_top to skip_bottom.
        Return:
            nested list  representing the data.
        """
        return self.data[self.skip_top:self.skip_bottom:]

    def getheader(self) -> list:
        """
        Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
        None: (when self.header is False)
        """
        return self.header


if __name__ == '__main__':
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
