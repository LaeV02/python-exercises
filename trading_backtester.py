import numpy as np

class Trading_Portfolio:
    def __init__(self):
        # Initialize starting capital and empty portfolio assets
        self.total_money = 10000.0
        self.financial_shares = 0

    def buy(self, price):
        # Check if available cash is sufficient for the transaction
        if self.total_money < price:
            return "Not enough money"
        else:
            self.total_money -= price
            self.financial_shares += 1

    def sell(self, price):
        # Check if the portfolio holds any shares to liquidate
        if self.financial_shares < 1:
            return "Not enough shares"
        else:
            self.total_money += price
            self.financial_shares -= 1

def generate_historical_prices():
    start_price = 50.0
    # Generate 100 random daily percentage returns using a normal distribution
    daily_returns = np.random.normal(loc=0.001, scale=0.02, size=100)
    historical_prices = start_price * np.cumprod(1 + daily_returns)
    return historical_prices

# --- Execution ---
historical_prices = generate_historical_prices()
portfolio = Trading_Portfolio()

# Run the trading loop starting from day 5 to allow for moving average calculation
for day in range(5, 100):
    current_price = historical_prices[day]
    # Compute the 5-day moving average using NumPy slicing
    past_5_days_average = np.mean(historical_prices[day-5:day])

    # Algorithmic execution strategy based on price vs moving average
    if current_price < past_5_days_average:
        portfolio.buy(current_price)
    elif current_price > past_5_days_average:
        portfolio.sell(current_price)

# --- Final Analysis using NumPy ---
last_market_price = historical_prices[-1]
final_value = round(portfolio.total_money + (portfolio.financial_shares * last_market_price), 2)
total_return_rate = round(((final_value - 10000.0) / 10000.0) * 100, 2)

max_price = np.max(historical_prices).round(2)
min_price = np.min(historical_prices).round(2)
max_price_day = np.argmax(historical_prices) + 1
min_price_day = np.argmin(historical_prices) + 1

print("=========================================")
print("      ALGORITHMIC TRADING REPORT         ")
print("=========================================")
print(f"Final Portfolio Value: {final_value} €")
print(f"Total Return Rate:     {total_return_rate} %")
print(f"Remaining Cash:        {round(portfolio.total_money, 2)} €")
print(f"Shares Owned:          {portfolio.financial_shares}")
print("-----------------------------------------")
print(f"Max Stock Price:       {max_price} € (Day {max_price_day})")
print(f"Min Stock Price:       {min_price} € (Day {min_price_day})")
print("=========================================")