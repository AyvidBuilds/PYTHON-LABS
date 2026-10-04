"""Simple InterestTake:

Principal
Rate
Time

from the user and calculate: Simple Interest = (P × R × T) / 100 """

P =int(input("enter the principal -",))
R = int(input("enter the rate -",))
T =int(input("enter the time -",))

simple_interest = (P * R * T) / 100
print("simple interest",simple_interest)