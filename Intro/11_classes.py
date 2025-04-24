# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

'''
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
'''

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)
    
    def sum(self):
        sum = 0
        for num in self.data:
            sum += num
        return sum
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def mean(self):
        sum = 0
        for num in self.data:
            sum += num
        return f"{sum / len(self.data):.0f}"
    
    def median(self):
        list = sorted(self.data)
        n = len(list)
        mid = n // 2

        if n % 2 == 1:
            return list[mid]
        else:
            return (list[mid - 1] + list(mid)) / 2
    
    def mode(self):
        frequency = {}
        for number in self.data:
            if number in frequency.keys():
                frequency[number] += 1
            else:
                frequency[number] = 1
        max_count = max(frequency.values())

        modes = [num for num, count in frequency.items() if count == max_count]

        return f"{modes}, count: {max_count}" if len(modes) > 1 else f"{modes[0]}, count: {max_count}"

    def std(self):
        sum_of_elements = 0
        for i in self.data:
            sum_of_elements += i
        mean = sum_of_elements / len(self.data)

        sqr_difference = 0
        for n in self.data:
            sqr_difference += (n - mean) ** 2

        sample_variance = sqr_difference / (len(self.data) - 1)

        std = sample_variance ** 0.5

        return f"{std:.1f}"

    def var(self):
        sum_of_elements = 0
        for i in self.data:
            sum_of_elements += i
        mean = sum_of_elements / len(self.data)

        sqr_deviation = 0
        for n in self.data:
            sqr_deviation += (n - mean)**2

        sample_variance = sqr_deviation / (len(self.data) - 1)

        return sample_variance

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print('Count:', data.count())
print('Sum:', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 18.2

# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
        
    def add_income (self, concept, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        income = (concept, amount)
        self.incomes.add(income)
        print(f"New income added: {concept}")

    def total_income (self): 
        total_income = 0
        # for single_income in self.incomes:
        #     concept, amount = single_income
        #     total_income +=  amount
        
        # # return f"Total income: {total_income}"
        for _, amount in self.incomes:
            total_income += amount
        
        return total_income

        # generator version
        # return sum(amount for _, amount in self.incomes)

    
    def add_expense (self, concept, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        expense = (concept, amount)
        self.expenses.add(expense)
        print(f"New expense added: {concept}")

    def total_expense (self): 
        total_expense = 0
        for _, amount in self.expenses:
            total_expense += amount
        
        return total_expense

    def account_balance (self):
        return self.total_income() - self.total_expense()
    
    def account_info (self):
        return f"Full name: {self.firstname} {self.lastname}\nTotal income: {self.total_income()}\nTotal expenses: {self.total_expense()}\nAccount balance: {self.account_balance()}"
        

my_person = PersonAccount("John", "Doe")
my_person.add_income("Salary", 200)
my_person.add_income("Sales", 100)
my_person.add_expense("Food", 27)

print(my_person.account_info())