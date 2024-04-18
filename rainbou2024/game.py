import string


class Judge:
    def __init__(self, n) -> None:
        assert 0 < n <= 26
        self.n = n
        self.s = string.ascii_uppercase[:n]
    