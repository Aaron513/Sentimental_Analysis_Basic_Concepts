punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(text):
    for char in punctuation_chars:
        if char in text:
            text = text.replace(char, "")
    return text

# Lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_sentiment_score(tweet, positive_words, negative_words):
    positive_score = 0
    negative_score = 0

    tweet_words = strip_punctuation(tweet.lower()).split()

    for word in tweet_words:
        if word in positive_words:
            positive_score += 1
        elif word in negative_words:
            negative_score += 1

    net_score = positive_score - negative_score
    return positive_score, negative_score, net_score

input_file = "project_twitter_data.csv"
output_file = "resulting_data.csv"

with open(input_file, "r") as csvfile, open(output_file, "w") as resultfile:
    lines = csvfile.readlines()

    resultfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for line in lines[1:]:
        tweet_data = line.strip().split(",")
        tweet_text = tweet_data[0]
        retweets = int(tweet_data[1])
        replies = int(tweet_data[2])
        
        positive_score, negative_score, net_score = get_sentiment_score(tweet_text, positive_words, negative_words)        
        
        tweet_data.extend([str(positive_score), str(negative_score), str(net_score)])
        resultfile.write(",".join(tweet_data[1:]) + "\n")