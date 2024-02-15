class seive:

    def __init__(self, n=10**7):
        self.n = n
        self.prime_nums = []
        self.least_prime_factor = [0 for i in range(n + 1)]

        for i in range(2, n + 1):
            if self.least_prime_factor[i] == 0:
                self.least_prime_factor[i] = i
                self.prime_nums.append(i)

            j = 0
            while (
                j < len(self.prime_nums)
                and i * self.prime_nums[j] <= n
                and self.prime_nums[j] <= self.least_prime_factor[i]
            ):
                self.least_prime_factor[i * self.prime_nums[j]] = self.prime_nums[j]
                j += 1

    def prime_factorization(self, num):
        factorization = []
        while num != 1:
            factorization.append(self.least_prime_factor[num])
            num //= self.least_prime_factor[num]
        return factorization

