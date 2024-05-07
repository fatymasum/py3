
class cat:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def miyaulda(self):
        return "Miyav!"



cat1 = cat("Whiskers", 3)
cat2 = cat("Tom", 5)


print(f"{cat1.ad} cat name {cat1.yas} yaşında.")
print(f"{cat2.ad} cat name {cat2.yas} yaşında.")

print(cat1.miyaulda())
print(cat2.miyaulda())
