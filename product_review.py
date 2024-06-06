# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good","excellent","bad","poor","average"]
#-------- BREAKDOWN
    # 1. searches through a series of product reviews for keywords
    #     - make list with keywords
    #     - Loop through reviews
    # 2.Print out each review with the keywords in uppercase
    #     - .replace(keyword, keyword.upper())

for review in python_reviews:
    for word in keywords:
       if word in review:
            new_word = word.upper()
            print(f"\n- {review.replace(word,new_word)}")
            

           



