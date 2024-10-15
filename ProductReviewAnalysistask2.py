# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar","average"]

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def comment_counter(positive_words,negative_words,reviews):
    positive_word_count = 0
    negative_word_count = 0

    for review in reviews:
        for positive_word in positive_words:
            if positive_word in review.lower():
                positive_word_count +=1
        
        for negative_word in negative_words:
            if negative_word in review.lower():
                negative_word_count +=1
                
    print (f"The positive word count is",positive_word_count)
    print (f"The negative word count is", negative_word_count) 
    return positive_word_count,negative_word_count
print(comment_counter(positive_words,negative_words,reviews)) 