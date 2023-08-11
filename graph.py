import matplotlib.pyplot as plt
import csv

net_scores = []
retweets = []

# Read data from the resulting_data.csv file
with open("resulting_data.csv", "r") as csvfile:
    lines = csvfile.readlines()
    for row in lines[1:]:
        tweet_data = row.strip().split(",")
        x = tweet_data[-1]
        y = tweet_data[0]
        net_scores.append(int(x))
        retweets.append(int(y))

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(net_scores, retweets, alpha=0.5)
plt.xlabel("Net Score")
plt.ylabel("Number of Retweets")
plt.title("Scatter Plot of Net Score vs. Number of Retweets")
plt.grid(True)

# Show the plot
plt.show()