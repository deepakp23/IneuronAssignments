### Area of Triangle

class SidesofTriangle():

    def __init__(self):
        self.a = float(input("First: "))
        self.b = float(input("Second: "))
        self.c = float(input("Third: "))

    def __str__(self):
        return f"The side are {self.a}, {self.b} and {self.c}"


class AreaofTriangle(SidesofTriangle):
    def __init__(self):
        super().__init__()

    def areaofTriangle(self):
        semiPeri = (self.a + self.b + self.c) * 0.5
        area = (semiPeri * (semiPeri - self.a) * (semiPeri - self.b) * (semiPeri - self.c)) ** 0.5
        return round(area, 4)

    def __str__(self):
        return f"Area: {self.areaofTriangle()}"


area = AreaofTriangle()
print(area)


########################################################################
###### FILTER WORDS #######################

def filter_long_words(words, size):
    filter_words = [x for x in words if len(x) > size]
    return filter_words

######################################################


def get_length(lst):
    len_lst = [len(x) for x in lst]
    return len_lst


####################################################

def vowel(word):
    vow = ['a', 'e', 'i', 'o', 'u']
    if word.lower() in vow:
        return True
    else:
        return False





