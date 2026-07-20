from random import random
import math

class discreteGenerators:
    def udiscrete1n(n: int) -> int:
        '''
        Via the inverse transform method, generates a discrete random
        variable uniformly distributed between 1 and n.
        Parameters:
            n (int): The upper bound of the distribution.
        Returns:
            int: A random integer between 1 and n (inclusive).
        '''
        u = random()
        return int(n * u) + 1

    def udiscretemk(m: int, k: int) -> int:
        '''
        Via the inverse transform method, generates a discrete random
        variable uniformly distributed between m and k.
        Parameters:
            m (int): The lower bound of the distribution.
            k (int): The upper bound of the distribution.   
        Returns:
            int: A random integer between m and k (inclusive).
        '''
        u = random()
        return int(u * (k - m + 1)) + m
    
    def geometric(p: float) -> int:
        '''
        Via the inverse transform method, generates a random variable
        following a geometric distribution with parameter 'p'.
        Parameters:
            p (float): The success probability of the geometric distribution.
        Returns:
            int: A random integer representing the number of trials until
            the first success in a geometric distribution.
        '''
        u = random()
        return int((math.log(1 - u) / math.log(1 - p))) + 1
    
    def bernoulli(p: float) -> int:
        '''
        Via the inverse transform method, generates a random variable
        following a Bernoulli distribution with parameter 'p'.
        Parameters:
            p (float): The success probability of the Bernoulli distribution.
        Returns:
            int: A random integer representing the outcome of a Bernoulli
            trial (0 for failure, 1 for success).
        '''
        u = random()
        return 1 if u < p else 0
    
    def Nbernoullis(n:int ,p: float) -> list:
        '''
        Via the inverse transform method, generates a list of 'n' random
        variables following a Bernoulli distribution with parameter 'p'.
        Parameters:
            n (int): The number of Bernoulli random variables to generate.
            p (float): The success probability of the Bernoulli distribution.
        Returns:
            list: A list of 'n' random integers representing the outcomes of
            Bernoulli trials (0 for failure, 1 for success).
        '''
        bernoullis = [0] * n
        j = discreteGenerators.geometric(p) -1
        while j < n:
            bernoullis[j] = 1
            j += discreteGenerators.geometric(p)
        return bernoullis

    def poisson(lam: float) -> int:
        '''
        Via the inverse transform method, generates a random variable
        following a Poisson distribution with parameter 'lam'.
        Parameters:
            lam (float): The rate parameter of the Poisson distribution.
        Returns:
            int: A random integer representing the number of events in a
        '''
        p = math.exp(-lam)
        f = p
        for j in range(1, int(lam) + 1):
            p *= lam / j
            f += p
        u = random()
        if u >= f:
            j = int(lam) + 1
            while u >= f:
                p *= lam / j
                f += p
                j += 1
            return j - 1
        else:
            j = int(lam)
            while u < f:
                f -= p
                if(j == 0):
                    break
                p *= lam / j
                j -= 1
            return j + 1

    def binomial(n: int, p: float) -> int:
        '''
        Via the inverse transform method, generates a random variable
        following a Binomial distribution with parameters 'n' and 'p'.
        Parameters:
            n (int): The number of trials in the Binomial distribution.
            p (float): The success probability of each trial in the
            Binomial distribution.
        Returns:
            int: A random integer representing the number of successes in
            'n' trials of a Binomial distribution.
        '''
        f = (1 - p) ** n
        u = random()
        if u < f:
            return 0
        for j in range(1, n + 1):
            f += math.comb(n, j) * (p ** j) * ((1 - p) ** (n - j))
            if u < f:
                return j
        return n
    



class permutation:
    def permutation1(a: list) -> list:
        '''
        Generates a random permutation of the input list 'a' using the
        Fisher-Yates shuffle algorithm.
        Parameters:
            a (list): The list to be permuted.
        Returns:
            list: A new list containing a random permutation of the
            input list 'a'.        
        '''
        N = len(a)
        for j in range(N-1):
            indice = int((N - j) * random()) + j
            a[j], a[indice] = a[indice], a[j]
        return a
    
    def permutation2(a: list) -> list:
        '''
        Generates a random permutation of the input list 'a' using an
        alternative version of the Fisher-Yates shuffle algorithm.
        Parameters:
            a (list): The list to be permuted.
        Returns:
            list: A new list containing a random permutation of the
            input list 'a'.
        '''
        N = len(a)
        for j in range(N-1, 0, -1):
            indice = int((j + 1) * random())
            a[j], a[indice] = a[indice], a[j]
        return a

    def subcRandom(r: int, a: list) -> list:
        '''
        Generates a random subset of size 'r' from the input list 'a'
        using a modified version of the Fisher-Yates shuffle algorithm.
        Parameters:
            r (int): The size of the subset to be generated.
            a (list): The list from which the subset will be generated.
        Returns:
            list: A new list containing a random subset of size 'r' from
            the input list 'a'.
        '''
        n = len(a)
        for j in range(n - 1, n - 1 - r, -1):
            indice = int((j + 1) * random())
            a[j], a[indice] = a[indice], a[j]
        return a[n-r:]
