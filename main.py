from pampy import match, _

class Nothing:
    """A basic Callable NoneType
    Use this object to write generic code pipelines
    Makes your life easier when using the railway paradigm
    >>> Nothing()
    >>> Nothing

    >>> print(Nothing)
    >>> Nothing

    >>> Nothing + 1
    >>> Nothing
    """
    def __call__(self, *args, **kwargs):
        return self
    
    def __repr__(self) -> str:
        return "Nothing"
    
    def __str__(self) -> str:
        return "Nothing"
    
    def __add__(self, other):
        return self
    
    def __sub__(self, other):
        return self

    def __mul__(self, other):
        return self
    
    def __matmul__(self, other):
        return self
    
    def __truediv__(self, other):
        return self

    def __floordiv__(self, other):
        return self

    def __eq__(self, other):
        if isinstance(other, Nothing):
            return True
        return False

    def __getattr__(self, attr):
        return self

    def __setattr__(self, attr, value):
        pass

    def __getitem__(self, k):
        return match(k,
            int, self,
            _, [Nothing()]
        )

    def __iter__(self):
        return iter([Nothing()])

    def __len__(self):
        return 1