# Format specifiers are special codes that tell Python how to format
# (or style) numbers when printing them — especially when using f-strings
price = 3.14159

# to two decimal places:
print(f"{price} to 2 decimal places (:.2f) {price:.2f}")
print(f"{price} to 4 decimal places (:.4f) {price:.4f}")
print(f"{price} consuming 10 spaces (right aligned) (:10) {price:10}")
print(f"{price} consuming 10 spaces (right aligned) (:010.2f) ZERO PADDED and 2 decimal points {price:010.2f}")
# alignments:
print(f"Left: ####{price:<10.2f}####")
print(f"Right: ####{price:>10.2f}####")
print(f"Center: ####{price:^10.2f}####")

newnum = 100987000
# showing positive and negative signs
print(f"{newnum:+}")
newnum *= -1  # make the num negative
print(f"{newnum:+}")

# comma as thousand separator
print(f"{newnum:,}")

# putting many together:
print(f"{price:>+10,.2f}")
