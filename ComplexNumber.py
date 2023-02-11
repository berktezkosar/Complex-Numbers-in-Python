import math
class ComplexNumber:
    """
    A class for representing complex number with real and imaginary components.
    """

    def __init__(self, real, imag):
        """
        Create a new complex number with given float values.

        Args:
            real (float): The real component of the complex number.
            imag (float): The imaginary component of the complex number.
        """
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """
        We define addition of complex numbers as follows:
                (a + bj) + (c + dj) = (a + c) + (b + d)j

        Args:
            other (ComplexNumber): The other complex number to add.
        Returns:
            ComplexNumber: The sum of the two complex numbers.
        """
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real,imag)

    def __sub__(self, other):
        """
        We define addition of complex numbers as follows:
                (a + bj) - (c + dj) = (a - c) - (b - d)j

        Args:
            other (ComplexNumber): The other complex number to subtract.
        Returns:
            ComplexNumber: The subtraction of the two complex numbers.
        """
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real,imag)

    def __mult__(self,other):
        """
        Complex multiplication is based on the identity j2 = - 1: 
        (a+bj)(c+dj)=ac+adj+bcj+bdj2 =(ac - bd)+(ad+bc)j.

        Args:
            other (ComplexNumber): The other complex number to multiply.
        Returns:
            ComplexNumber: The multiplication of the two complex numbers.
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real,imag)

    def __truediv__(self,other):
        """
        Args:
            other (ComplexNumber): The other complex number to divide.
        Returns:
            ComplexNumber: The true divition of the two complex numbers.
        """
        denom = other.real**2 + other.imag**2
        real = (self.real*other.real + self.imag*other.imag) / denom
        imag = (self.imag*other.real - self.real*other.imag) / denom
        return ComplexNumber(real,imag)
    
    def magnitude(self,other):
        """
        Calculate the magnitude value of the complex number.

        Returns:
            float: The magnitude of the complex number.
        """
        return (self.real**2 + self.imag**2)**0.5

    def phase(self, other):
        """
        The angle or phase or argument of the complex number a + bj is the angle, 
        measured in radians, from the point 1 + 0j to a + bj, 
        with counterclockwise denoting positive angle. 
        The angle of a complex number c = a + bj is denoted ̸ c:
                    ̸ c = arctan b/a.
                    
        Return:
            float: The phase of the complex number in radians.
        """
        return math.atan2(self.imag, self.real)

    def position(self):
        """
        Position on the plane 
        """
        pass

    def conjugate(self,other):
        """
        The complex conjugate of the complex number z = x + yi is given by x − yi. 
        It is denoted by either z or z*. This unary operation on complex numbers cannot 
        be expressed by applying only their basic operations addition, subtraction, 
        multiplication and division. 
        Geometrically, z is the "reflection" of z about the real axis. 
        Conjugating twice gives the original complex number
                z* = z
        """
        pass

    def n_root(self,other):
        """
        n-degree root of a complex number
        """
        pass
    
    def complex_sqrt(self):
        """
        square root of complex number
        """
        pass

    def complex_exp(self):
        """
        Complex exponention of complex number
        """
        pass
