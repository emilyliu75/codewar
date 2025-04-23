def calculate_years(principal, interest, tax, desired):
    one_year_i = principal * interest * (1-tax)
    year = 0
    while principal < desired:
        year += 1
        one_year_i = principal * interest * (1-tax)
        principal += one_year_i
    return year
