""" Analyzes the growth"""

if __name__ == '__main__':
    print("Run Growth Analyzer")

    # Change these to affect the formula.
    K_CAPITAL = 1000
    K_YEARS = 10
    K_GROWTH_RATE = 0.10  # % Gain Per year.
    K_GROWTH_DECAY = 0.05  # How much % the growth decreases per year.
    K_COMPOUNDING_FREQUENCY = 30  # The rate will compound every X days.

    # Don't touch these..
    K_DAYS_IN_YEAR = 365

    # Run the program.
    current_growth = K_GROWTH_RATE
    current_capital = K_CAPITAL
    decay_rate = 1.0 - K_GROWTH_DECAY

    # How many days in total do we need to run for?
    remaining_days = int(K_YEARS * K_DAYS_IN_YEAR)
    times_compounded = 0

    # Run the loop.
    while remaining_days > 0:

        # Work out how many days to compound for.
        compound_days = min(remaining_days, K_COMPOUNDING_FREQUENCY)
        remaining_days -= compound_days
        times_compounded += 1

        # Work out the t-factor (time).
        t = compound_days / K_DAYS_IN_YEAR

        # Apply the growth to the capital.
        growth_factor = (1.0 + current_growth) ** t
        current_capital *= growth_factor

        # Apply the growth decay.
        decay_factor = decay_rate ** t
        current_growth *= decay_factor

    print("Simulation Complete")
    print("Compounded {} times".format(times_compounded))
    print("Capital Grew From {} to {}.".format(K_CAPITAL, current_capital))
    print("Absolute Capital Growth: {}".format(current_capital - K_CAPITAL))
    print("Total Percent Growth: {:.2f}%".format((current_capital/K_CAPITAL - 1) * 100))
    print("Ending Growth Rate: {}".format(current_growth))



