class generators:
    def genMul(semilla: int, a: int, M: int)-> int:
        '''
        Generates the next number in the multiplicative
        congruential generator sequence.
        Parameters:
            semilla (int): The current seed value.
            a (int): The multiplier.
            M (int): The modulus.
        Returns:
            int: The next number in the sequence.
        '''
        next = (a * semilla) % M
        return next

    def genMix(semilla: int, a: int, c: int, M: int)-> int:
        '''
        Generates the next number in the mixed
        congruential generator sequence.
        Parameters:
            semilla (int): The current seed value.
            a (int): The multiplier.
            c (int): The increment.
            M (int): The modulus.
        Returns:
            int: The next number in the sequence.
        '''
        next = (a * semilla + c) % M
        return next

    def genComb_sum(semilla: int, a: int, c: int, M: int)-> int:
        '''
        Generates the next number in the combined
        congruential generator sequence.
        Parameters:
            semilla (int): The current seed value.
            a (int): The multiplier.
            c (int): The increment.
            M (int): The modulus.
        Returns:
            int: The next number in the sequence.
        '''
        next_mul = generators.genMul(semilla, a, M)
        next_mix = generators.genMix(semilla, a, c, M)
        combined = (next_mul + next_mix) % M
        return combined
    
    def vonNeumann(semilla: int)-> int:
        '''
        Generates the next number in the von Neumann middle-square
        generator sequence.
        Parameters:
            semilla (int): The current seed value.
        Returns:
            int: The next number in the sequence.
        '''
        next = (semilla**2 // 100) % 10000
        return next
    
    def randu(semilla: int)-> int:
        '''
        Generates the next number in the RANDU generator sequence.
        
        a=65539, c=0, M=2^31
        Parameters:
            semilla (int): The current seed value.
        Returns:
            int: The next number in the sequence.
        '''
        next = (semilla * 65539) % (2**31)
        return next
    
    def randu2(semilla: int)-> int:
        '''
        Generates the next number in the RANDU generator sequence.
        
        a=16807, c=0, M=2^31-1
        Parameters:
            semilla (int): The current seed value.
        Returns:
            int: The next number in the sequence.
        '''
        next = (semilla * 16807) % (2**31 - 1)
        return next