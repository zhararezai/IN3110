"""
Array class for assignment 2
"""

from itertools import chain


class Array:

    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        if type(shape) != tuple: raise TypeError("Shape-elements are of wrong types")
        elif type(values) != tuple: raise TypeError("Value-elements are of wrong types")

        shape_error = True
        value_error = True

        # Check if the values are of valid types 
        if all((type(n) is int) for n in shape) or all((type(n) is float) for n in shape) or all((type(n) is bool) for n in shape):
            shape_error = False
        if all((type(n) is int) for n in values) or all((type(n) is float) for n in values) or all((type(n) is bool) for n in values):
            value_error = False

        if shape_error:
            raise ValueError("types for shape are not all of the same type")
        if value_error:
            raise ValueError("types for value are not all of the same type")


        # Check that the amount of values corresponds to the shape

        #sjekker om det er 1d eller 2d
        if len(shape) == 1:
             if len(values) != shape[0]: #hvis lengden av values ikke er lik shape
                raise ValueError("The number of values does not fit with the shape")
        if len(shape) == 2:
            #hvis det er 2d array, initialiserer 2d array
            ny_liste = []
            teller = 0

            for i in range(shape[0]): #kolonner, y
                rad = []
                for j in range(shape[1]): #rader, x
                    rad.append(values[teller])
                    teller += 1
                ny_liste.append(rad)

            values = ny_liste


        # Set class-variables
        self._values = list(values)
        self._shape = tuple(shape)
        self._flat_array = self.flat_array()

        if len(self._shape) == 2 and len(self._flat_array) != shape[0]*shape[1]: #hvis lengden av values ikke er lik shape
            raise ValueError("The number of values does not fit with the shape")


        


    def flat_array(self):
        """Flattens the N-dimensional array of values into a 1-dimensional array.
        Returns:
            list: flat list of array values.
        """
        flat_array = self._values

        for _ in range(len(self._shape[1:])):
            flat_array = list(chain(*flat_array))

        return flat_array



    def __getitem__(self, index):
        """"Return the element of the given index.

            Args:
                index (int): the index of the element we want to access 
            
            Returns:
                self._values[index]: the element that can be found on the given index

         """
        if len(self._shape) == 1: #hvis det er 1d array
            if index > len(self._values): 
                raise IndexError("Index out of bounds")
            else: 
                return self._values[index]
        else: #hvis det er 2d array
            x = self._shape[0]
            y = self._shape[1]

            if index > x*y:
                raise IndexError("Index out of bounds")
            else:
                return self._values[index]


    
    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.
        """

        return "[" + ", ".join(map(str, self._values)) + "]"



    def __add__(self, other): #funksjon for å summere elementene i to arrayer
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented
    
        ny_liste = []
        ny_shape = self._shape

        if type(other) == bool or type(self) == bool:
            return NotImplemented

        if type(other) == Array: #hvis både self og other er Array-objekter
            
            flat_other = other.flat_array()

            if type(flat_other[0]) == bool or self._flat_array[0] == bool:
                return NotImplemented

            if len(self) > len(other): #hvis other er den minste, itererer i range(len(other))

                #legger til i den nye listen
                for i in range(0, len(self._flat_array)):
                    ny_liste.append(self._flat_array[i])

                for i in range(0, len(flat_other)):
                    ny_liste[i] = flat_other.__getitem__(i) + self._flat_array[i] 

            else: #hvis self er den minste eller begge er like store, itererer i range(len(self))
                ny_shape = other.get_shape()
                #legger til i listen
                for i in range(0, len(flat_other)):
                    ny_liste.append(flat_other[i])


                for i in range(0, len(self._flat_array)):
                    ny_liste[i] = flat_other.__getitem__(i) + self._flat_array[i]

        else: #hvis self eller other ikke er Array
            if type(self) != Array: #kun other er array
                return other.__radd__(self) #samme som array1.__radd__(10)
            elif type(other) != Array: #kun self er array
                return self.__radd__(other)
      

        return Array(ny_shape, *ny_liste)


        
    def __radd__(self, other): 
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        ny_liste = []

        if type(other) == Array: #både self og other er Array-objekter
                #legger til i listen
            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self._flat_array)):
                ny_liste[i] = other + self._flat_array[i]
        else: #self er 2d array, other er int

            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self)):
                ny_liste[i] = other + self._flat_array[i] 
      

        nytt_objekt = Array(self._shape, *ny_liste)
        
        return nytt_objekt


    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
            
        ny_liste = []
        ny_shape = self._shape

        if type(other) == bool or type(self) == bool:
            return NotImplemented


        if type(other) == Array: #hvis både self og other er Array-objekter
            
            flat_other = other.flat_array()
            
            if type(flat_other[0]) == bool or self._flat_array[0] == bool:
                return NotImplemented

            if len(self) > len(other): #hvis other er den minste, itererer i range(len(other))

                #legger til i den nye listen
                for i in range(0, len(self._flat_array)):
                    ny_liste.append(self._flat_array[i])

                for i in range(0, len(flat_other)):
                    ny_liste[i] = flat_other.__getitem__(i) - self._flat_array[i] 

            else: #hvis self er den minste eller begge er like store, itererer i range(len(self))
                ny_shape = other.get_shape()
                #legger til i listen
                for i in range(0, len(flat_other)):
                    ny_liste.append(flat_other[i])


                for i in range(0, len(self._flat_array)):
                    ny_liste[i] = flat_other.__getitem__(i) - self._flat_array[i]

        else: #hvis self eller other ikke er Array
            if type(self) != Array: #kun other er array
                return other.__rsub__(self) #samme som array1.__radd__(10)
            elif type(other) != Array: #kun self er array
                return self.__rsub__(other)
    
               
        return Array(ny_shape, *ny_liste)
        



    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.
        """
        ny_liste = []

        if type(other) == Array: #både self og other er Array-objekter
                #legger til i listen
            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self._flat_array)):
                ny_liste[i] = other - self._flat_array[i]
        else: #self er 2d array, other er int

            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self)):
                ny_liste[i] = other - self._flat_array[i] 
      

        nytt_objekt = Array(self._shape, *ny_liste)
        
        return nytt_objekt


    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        ny_liste = []
        ny_shape = self._shape

        if type(other) == bool or type(self) == bool:
            return NotImplemented

        if type(other) == Array: #hvis både self og other er Array-objekter
            
            flat_other = other.flat_array()

            if type(flat_other[0]) == bool or self._flat_array[0] == bool:
                return NotImplemented

            if len(self) > len(other): #hvis other er den minste, itererer i range(len(other))

                #legger til i den nye listen
                for i in range(0, len(self._flat_array)):
                    ny_liste.append(self._flat_array[i])

                for i in range(0, len(flat_other)):
                    ny_liste[i] = flat_other.__getitem__(i) * self._flat_array[i] 

            else: #hvis self er den minste eller begge er like store, itererer i range(len(self))
                ny_shape = other.get_shape()
                #legger til i listen
                for i in range(0, len(flat_other)):
                    ny_liste.append(flat_other[i])

                for i in range(0, len(self._flat_array)):
                    ny_liste[i] = flat_other.__getitem__(i) * self._flat_array[i]
        else: #hvis self eller other ikke er Array
            if type(self) != Array: #kun other er array
                return other.__rmul__(self) #samme som array1.__radd__(10)
            elif type(other) != Array: #kun self er array
                return self.__rmul__(other)

        return Array(ny_shape, *ny_liste)
        

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        #return self.__mul__(other)

        ny_liste = []

        if type(other) == Array: #både self og other er Array-objekter
                #legger til i listen
            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self._flat_array)):
                ny_liste[i] = other * self._flat_array[i]
        else: #self er 2d array, other er int

            for i in range(0, len(self._flat_array)):
                ny_liste.append(self._flat_array[i])


            for i in range(0, len(self)):
                ny_liste[i] = other * self._flat_array[i] 
      

        nytt_objekt = Array(self._shape, *ny_liste)
        
        return nytt_objekt




    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        is_eq = True

        is_shape_eq = True



        if is_shape_eq == False or type(other) != Array and type(other) != int or type(other) != Array and type(other) == bool: #ugyldig sjekk
                return False    
        
        #sjekker om shape er lik
        for i in range(len(self._shape)): 
            if self._shape[i] != other.get_shape()[i]:
                is_shape_eq = False
        
        if is_shape_eq == False or type(other) != Array and type(other) != int: #ugyldig sjekk
                return False


        flat_other = other.flat_array()

        for i in range(0, len(self._flat_array)):
            for i in range(0, len(flat_other)):
                if self._flat_array[i] != flat_other[i]:
                    is_eq = False



        return is_eq

            

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.
        """

        if type(other) == Array:
            for i in range(len(self._shape)): 
                if self._shape[i] != other.get_shape()[i]:
                    raise ValueError("shape of 'other' does not match")
        elif type(other) != Array and type(other) != int:
            raise TypeError("invalid type of 'other'")
        
        
        liste = []

        
        
        if type(other) == int:
            for i in range(0, len(self._flat_array)):
                if other == self._flat_array[i]:
                    liste.append(True)
                else:
                    liste.append(False)
        else:
            flat_other = other.flat_array()

            if(len(self._flat_array) > len(flat_other)): #other er den minste
                for i in range(0, len(flat_other)):
                    if self._flat_array[i] == flat_other[i]:
                        liste.append(True)
                    else:
                        liste.append(False)
            else: #self er den minste
                for i in range(0, len(self._flat_array)):
                    if self._flat_array[i] == flat_other[i]:
                        liste.append(True)
                    else:
                        liste.append(False)

                        

        return Array(self._shape, *liste)



    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        if type(self) == bool: return NotImplemented

        min_elem = self._flat_array[0]

        for i in range(len(self._flat_array)):
            if self._flat_array[i] < min_elem: min_elem = self._flat_array[i]

        return min_elem


    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        if type(self) == bool: return NotImplemented
        
        ant_elem = len(self._flat_array) #antall elementer i listen
        sum_elem = 0

        for i in range(0, len(self._flat_array)):
            sum_elem += self._flat_array[i] #summerer elementene

        mean_element = sum_elem / ant_elem #finner gjennomsnittet i listen

        return mean_element 


    def __len__(self):
        """
        Finds the length of the Array-object that calls on it.

        Args:
        
        Returns:
            size (int): the length of self._values
        
        """
        if len(self._shape) == 2:
            size = self._shape[0] * self._shape[1]
        else:
            size = self._shape[0]

        return size


    def get_shape(self):
        """
        Returns the shape

        Args:

        Returns:
            the shape of the Array-object
        """
        return self._shape

    def get_values(self):
        """
        Returns the values

        Args:

        Returns:
            the values of the Array-object
        """
        return self._values