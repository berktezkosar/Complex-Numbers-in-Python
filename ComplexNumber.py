class ComplexNumber:
    """
    A class for representing complex number with real and imaginary components.
    """

    def __init__(self, real, imag):
        """

        """
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """
        """
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real,imag)

    def __subs__(self, other):
        """
        """
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real,imag)

    def __mult__(self,other):
        return

    def __div__(self,other):
        return
    
    def magnitude(self,other):
        return

    def angle(self, other):
        return 

    def n_root(self,other):
        """
        n-degree root of a complex number
        """
        return
    
    def complex_sqrt(self,other):
        """
        square root of complex number
        """
        return