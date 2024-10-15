#Task 3: Review Summary



#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",

reviews = [
       "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

def summarize_reviews(reviews):
  # We want to return an array because the original argument was an array 
  reviews_to_return = [] 

# Iterate through reviews 
  for review in reviews:

    # If the review is less than 30 characters, add the original review to our reviews_to_return 
    if len(review) <= 30:
      reviews_to_return.append(review)

    # If the reviews are longer than 30 characters, we want to do something to it 
    else:
      # Find the cutoff (where is the last space in our first 30 characters?)
      # string.rfind(value we want to find)
      cutoff = review[:30].rfind(' ')

      # review[:cutoff] + ... 
      if cutoff != -1:
        reviews_to_return.append(review[:cutoff] + "...")
        #print (review[:cutoff] + "...")
      else:
        reviews_to_return.append(review[:30] + "...")
        #print (review[:30] + "...")

  return reviews_to_return
        


lists_of_reviews = summarize_reviews(reviews)
print (lists_of_reviews)
for review in lists_of_reviews:
    print (review)