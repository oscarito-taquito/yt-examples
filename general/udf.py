# simple interest
principal = 1000
rate = .04
years = 5


def simple_interest(p, r, y):
    m_amt = p * (1 + r*y)
    return m_amt


maturity_value = simple_interest(principal, rate, years)
print(f"I invested {principal}, and in {years} years later, I will receive ${maturity_value}")
