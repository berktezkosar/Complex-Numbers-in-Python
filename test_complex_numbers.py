import math
import unittest
import subprocess
import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def test_addition(self):
        """
        Test addition of two complex numbers.

        This test method creates and checks two complex numbers, 
        adds them using the "+" sign,
        and checks that the real and imaginary parts 
        of the complex number that created are correct.
        
        (assertAlmostEqueal used instead of assertEqual,
        since the values are float)
        """
        # test addition of two complex numbers
        
        t1 = ComplexNumber(5, -7)
        t2 = ComplexNumber(3, 5)
        t3 = t1 + t2
        self.assertAlmostEqual(t3.real, 8)
        self.assertAlmostEqual(t3.imag, -2)
    
    def test_subtraction(self):
        """
        Test subtraction of two complex numbers.

        This test creates and checks two different complex numbers,
        subtracts them using '-' sign,
        and checks the final complex numbers' real and imaginary parts
        are created correctly.

        (assertAlmostEqueal used instead of assertEqual,
        since the values are float)
        """
        t1 = ComplexNumber(5, -7)
        t2 = ComplexNumber(3, 5)
        t3 = t1 - t2
        self.assertAlmostEqual(t3.real, 2)
        self.assertAlmostEqual(t3.imag, -12)

    def test_multiplication(self):
        """
        Test multiplication of two complex numbers.

        This test method creates two complex numbers, 
        multiplies them together using the "*"
        sign, and checks that the real and imaginary parts 
        of the resulting complex number are correct.
        """

        t1 = ComplexNumber(5, -7)
        t2 = ComplexNumber(3, 5)
        t3 = t1 * t2
        self.assertAlmostEqual(t3.real, -20)
        self.assertAlmostEqual(t3.imag, 4)

    def test_divition(self):
        """
        Test division of two complex numbers.

        This test method creates two complex numbers, 
        divides one by the other using the "/" sign, 
        and checks that the real and imaginary parts 
        of the resulting complex number are correct.
        """

        t1 = ComplexNumber(5, -7)
        t2 = ComplexNumber(3, 5)
        t3 = t1 / t2
        self.assertAlmostEqual(t3.real, -0.58)
        self.assertAlmostEqual(t3.imag, -1.35)
        
    def test_division_by_zero(self):
        """
        Test division by zero.

        This test method created to test a complex number and divides it by a complex number with
        real and imaginary parts both equal to zero. 
        It checks and raise error using a ZeroDivisionError
        """
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(0, 0)
        with self.assertRaises(ZeroDivisionError):
            z1 / z2

    def test_magnitude(self):
        """
        Test magnitude of complex number.

        This test creates a complex number and checks the magnitude value
        of the given complex number according to its real and 
        imaginary parts. 
        """
        t = ComplexNumber(3, 4)
        self.assertAlmostEqual(t.magnitude(), 5)

    def test_phase(self):
        """
        Test phase of a complex number.

        This test creates a complex number and checks the phase (angle) value
        of the given complex number according to its real and 
        imaginary parts.  
        """
        t = ComplexNumber(1, 1)
        self.assertAlmostEqual(t.phase(), math.pi/4)

    def main(self):
        # run the test suite
        runner = unittest.TextTestRunner()
        result = runner.run(unittest.makeSuite(TestComplexNumber))

        # save the test results to a file
        with open('test_results.txt', 'w') as f:
            subprocess.call(['python', '-m', 'unittest', '-v', 'test_complex_number'], stdout=f)

if __name__ == '__main__':
    test = TestComplexNumber()
    test.main()