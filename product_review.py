# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

    # Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good","excellent","bad","poor","average"]
#-------- BREAKDOWN
    # 1. searches through a series of product reviews for keywords
    #     - make list with keywords
    #     - Loop through reviews
    # 2.Print out each review with the keywords in uppercase
    #     - .replace(keyword, keyword.upper())    

def word_search (list):
     for review in list:
        for word in keywords:
            if word in review:
                new_word = word.upper()
                print(f"\n- {review.replace(word,new_word)}")

word_search(reviews)
print("="*50)

# Task 2: Sentiment Tally

    # Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(list):
    pos_count = 0
    neg_count = 0
    for review in list:
        for word in positive_words:
            if word in review:
                pos_count += 1
        for word in negative_words:
             if word in review:
                neg_count += 1

    return print(f'''
    - Positive word count : {pos_count}
    - Negative word count : {neg_count}
    ''')

tally(reviews)
print("="*50)

# Task 3: Review Summary

    # Implement a function that takes the first 30 characters of a review and appends "…" to create a summary. 
    # (Bonus) Ensure that the summary does not cut off in the middle of a word.

def summary(list):
    summary_bank = []
    for review in list:
        summary_bank.append(f'{review[0:30]}...')
        
    print(summary_bank)
    

summary(reviews)
        

    

