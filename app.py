import random

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Act as if what you do makes a difference. It does. – William James",
    "With the new day comes new strength and new thoughts. – Eleanor Roosevelt"
]

# Pick a random quote
random_quote = random.choice(quotes)

# Display it
print("💬 Random Quote of the Day:")
print(random_quote)
