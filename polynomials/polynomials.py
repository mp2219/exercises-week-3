"""Create a polynomial class and related basic operations."""
from numbers import Number


class Polynomial:
    """Define a polynomial and its operations."""

    def __init__(self, coefs):
        """Define constructor."""
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            negativeothercoefs = tuple(-a for a in other.coefficients)
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + negativeothercoefs[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        negativeselfcoefs = tuple(-a for a in self.coefficients)
        return Polynomial((-self.coefficients[0] + other,)
                          + negativeselfcoefs[1:])

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            result = [0 for i in range(len(self.coefficients)
                      + len(other.coefficients) - 1)]
            for i in range(len(self.coefficients)):
                for j in range(len(other.coefficients)):
                    result[i+j] += self.coefficients[i] * other.coefficients[j]

            return Polynomial(tuple(result))

        elif isinstance(other, Number):
            return self * Polynomial(tuple(other))

    def __rmul__(self, other):
        return self * other
