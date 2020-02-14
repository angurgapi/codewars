class Primes:
	
	lst = [2]
	@classmethod
	def first(cls, n):
		if n>len(cls.lst):
			a = cls.lst[-1]+1
			while len(cls.lst)!= n:
				if(cls.is_prime(a)):
					cls.lst.append(a)
				a += 1
		return cls.lst[:n]

	@classmethod
	def is_prime(cls, n):
		for i in range(2,int(n**0.5)+1):
			if n%i==0:
				return False

		return True

primes = Primes()
				
#Sprint(primes.first(500))
