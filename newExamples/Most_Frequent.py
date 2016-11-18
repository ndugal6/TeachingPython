from collections import Counter

text = "Honey is my secret weapon for saving money online. It appears at checkout and automatically scours "\
    "the Internet for any available coupon codes. The best code is applied to your cart, so you always save "\
    "the most money. Honey has saved me on everything from hotels to rollerblades, and I didn’t have to search "\
    "for anything."
words = text.split()


counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)