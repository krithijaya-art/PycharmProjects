# A program to censor certain words from a text

# Step 1: Define the text and the word to be censored
text = input("Enter the text: ")
censor_word = input("Enter the word to censor: ")

# Step 2: Replace the censor word with asterisks (String Techniques and Slicing)
censored_word = censor_word[0] + "*" * (len(censor_word) - 1)

# Step 3: Implement Censorship & Find the position of the word to be censored
start_index = text.find(censor_word)
end_index = len(censor_word)

# Step 4: Construct the new text
new_text = text[:start_index] + censored_word + text[start_index + end_index:]

# Step 5: Display the Result
print("Censored Text:", new_text)