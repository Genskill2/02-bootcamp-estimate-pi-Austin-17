import math
import unittest
import random
def wallis(no1):	#no1 is number of iterations
	pdt = 1
	for i in range (1,no1+1):
		t = 4*i*i
		pdt = pdt * (t/(t-1))
	pdt = pdt * 2
	return pdt




def monte_carlo(no2):	#no2 is total number of darts & also number of iteration
	n = 0
	for j in range (1,no2+1):
		x = random.random()
		y = random.random()
		r = math.sqrt( x**2 + y**2 )
		if r < 1:
			n = n + 1
	pi_val = 4 * (n/no2)
	return pi_val

no1 = int(input("Enter number of iterations: "))
print(wallis(no1))
no2 = int(input("Enter number of iterations: "))
print(monte_carlo(no2))

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
