# exercise5_api_option_b.py
# Exercise 5: Public API Connection - CoinGecko

import requests
import pandas as pd
import matplotlib.pyplot as plt

print("="*60)
print("EXERCISE 5: PUBLIC API CONNECTION - CoinGecko")
print("="*60)

# Step 1: Connect to CoinGecko API
print("\nStep 1: Connecting to CoinGecko API...")
api_url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters for top 10 cryptocurrencies by market cap
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1
}

try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    print(f"✓ API request successful (Status Code: {response.status_code})")
except Exception as e:
    print(f"✗ API request failed: {e}")
    exit()

# Step 2: Parse response
print("\nStep 2: Parsing cryptocurrency data...")
crypto_data = response.json()
print(f"✓ Retrieved data for {len(crypto_data)} cryptocurrencies")

# Step 3: Extract relevant information
print("\nStep 3: Processing data...")
df = pd.DataFrame(crypto_data)
df_selected = df[['name', 'symbol', 'current_price', 'market_cap', 
                  'price_change_percentage_24h']].copy()

print("\nTop 10 Cryptocurrencies:")
print(df_selected.to_string(index=False))

# Step 4: Create visualization - Price comparison
print("\nStep 4: Creating price comparison chart...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Chart 1: Current prices
bars1 = ax1.barh(df_selected['symbol'], df_selected['current_price'],
                 color='#D69E2E', edgecolor='#1A202C', linewidth=1.5)

ax1.set_title('Current Cryptocurrency Prices (USD)',
              fontsize=14, fontweight='bold', color='#1A202C')
ax1.set_xlabel('Price (USD)', fontsize=11)
ax1.set_ylabel('Cryptocurrency', fontsize=11)
ax1.grid(axis='x', alpha=0.3, linestyle='--')

# Chart 2: 24h price change percentage
colors = ["#A8FF12" if x > 0 else "#0BCA1B" for x in df_selected['price_change_percentage_24h']]
bars2 = ax2.barh(df_selected['symbol'], df_selected['price_change_percentage_24h'],
                 color=colors, edgecolor='#1A202C', linewidth=1.5)

ax2.set_title('24-Hour Price Change (%)',
              fontsize=14, fontweight='bold', color='#1A202C')
ax2.set_xlabel('Change (%)', fontsize=11)
ax2.set_ylabel('Cryptocurrency', fontsize=11)
ax2.axvline(x=0, color='black', linewidth=1, linestyle='-')
ax2.grid(axis='x', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('exercise5_visualization.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved as: exercise5_visualization.png")
plt.show()

# Step 5: Market analysis 
print("\nStep 5: Market Analysis") #each column with its operations
print(f"Highest Price: {df_selected.loc[df_selected['current_price'].idxmax(), 'name']} "
      f"(${df_selected['current_price'].max():,.2f})")
print(f"Biggest 24h Gain: {df_selected.loc[df_selected['price_change_percentage_24h'].idxmax(), 'name']} "
      f"({df_selected['price_change_percentage_24h'].max():.2f}%)")
print(f"Biggest 24h Loss: {df_selected.loc[df_selected['price_change_percentage_24h'].idxmin(), 'name']} "
      f"({df_selected['price_change_percentage_24h'].min():.2f}%)")
print(f"Total Market Cap: ${df_selected['market_cap'].sum():,.0f}")

print("\n" + "="*60)
print("Exercise 5 Complete!")
print("="*60)