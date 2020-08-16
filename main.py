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

    >>> Nothing[-42:42]
    >>> Nothing
    """
    def __call__(self, *args, **kwargs):
        """calling Nothing
        The long awaited callable None
        >>> Nothing()
        >>> Nothing
        Returns:
            Nothing: the long awaited callable None
        """
        return self
    
    def __repr__(self) -> str:
        """string represention
        >>> repr(Nothing)
        >>> "Nothing"
        Returns:
            str: Nothing
        """
        return "Nothing"
    
    def __str__(self) -> str:
        """string represention
        >>> str(Nothing)
        >>> "Nothing"
        Returns:
            str: Nothing
        """
        return "Nothing"
    
    def __neg__(self):
        """support negation
        >>> - Nothing
        >>> Nothing
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __pos__(self):
        """support position +
        >>> + Nothing
        >>> Nothing
        Returns:
            self Nothing: Nothing
        """
        return self

    def __abs__(self):
        """support absolute value operation 
        >>> abs(Nothing)
        >>> Nothing
        Returns:
            self Nothing: Nothing
        """
        return self

    def __invert__(self):
        """support invesion ~
        >>> ~Nothing
        >>> Nothing
        Returns:
            self Nothing: Nothing
        """
        return self

    def __int__(self):
        """support int conversion operation
        Returns:
            self Nothing: Nothing
        """
        raise TypeError("int() argument must be Something, not Nothing")

    def __round__(self, *args, **kwargs):
        """support rounding operation
        >>> round(Nothing)
        Nothing

        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __trunc__(self):
        """support rounding operation
        >>> from math import trunc
        >>> trunc(Nothing)
        Nothing

        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __floor__(self):
        """support floor operation
        Floor Gang Awou
        >>> from math import floor
        >>> floor(Nothing)
        Nothing

        Returns:
            self Nothing: Nothing
        """
        print("Floor gang awou")
        return self
        
    def __ceil__(self):
        """support ceil operation
        >>> from math import ceil
        >>> ceil(Nothing)
        Nothing
        
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __add__(self, other):
        """add left to right operation
        >>> Nothing + 1
        Nothing
        
        Args:
            other (Any): Can be anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __radd__(self, other):
        """add right to left operation
        >>> 1 + Nothing
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __sub__(self, other):
        """substract lef to right
        >>> Nothing - 1
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __rsub__(self, other):
        """substract lef to right
        >>> 1 - Nothing
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __mul__(self, other):
        """multiply lef to right
        >>> Nothing * 1
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __rmul__(self, other):
        """multiply right to left
        >>> 2 * Nothing
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __matmul__(self, other):
        """matrix multiply left to right
        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __rmatmul__(self, other):
        """matrix multiply right to left
        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __truediv__(self, other):
        """divide left to right
        >>> Nothing / 2
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __rtruediv__(self, other):
        """divide right to left
        >>> 2 / Nothing
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __floordiv__(self, other):
        """floor divide left to right
        >>> Nothing // 2
        Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self
    
    def __rfloordiv__(self, other):
        """floor divide right to left
        >>> 2 // Nothing

        Args:
            other (Any): Can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __getattr__(self, attr: str):
        """get attribute of Nothing
        >>> getattr(Nothing, "heok")
        Nothing

        Args:
            attr (str): Can be any string
        Returns:
            self Nothing: Nothing
        """
        return self

    def __setattr__(self, attr, value):
        """Do Nothing
        >>> setattr(Nothing, "hello", "world")
        Args:
            attr (str): Can be any string
            value (Any): Can be Anything
        """
        pass

    def __getitem__(self, k):
        """Support indexing and slicing
        >>> Nothing[3]
        Nothing

        >>> Nothing[2:3]
        [Nothing]

        Args:
            k (Union[int, List[int]]): Can be any int or any slice
        Returns:
            Union[Nothing, List[Nothing]]: Can be either Nothing or [Nothing]
        """
        return match(k,
            int, self,
            _, [self]
        )

    def __iter__(self):
        """Support iteration
        Returns:
            Iterable: Iterable[Nothing]
        """
        return iter([self])

    def __len__(self) -> int:
        """Support len function on Nothing
        Returns:
            int: 1
        """
        return 1

    def __and__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __rand__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __or__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __lt__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __le__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __gt__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __ge__(self, other):
        """Boolean operation
        Args:
            other (Any): can be Anything
        Returns:
            self Nothing: Nothing
        """
        return self

    def __eq__(self, other) -> bool:
        """Support Equality check
        Args:
            other (Union[Nothing, Any]): can be either Nothing or Anything
        Returns:
            bool: can be either True or False
        """
        if isinstance(other, Nothing):
            return True
        return False
    
    def __hash__(self) -> int:
        """Support hash function
        Returns:
            int: returns in hash of Nothing object
        """
        return hash(Nothing)
