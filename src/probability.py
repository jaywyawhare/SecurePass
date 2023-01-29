from src.entropy import encode
from src.similarity import checkSimilarity


def TotalProbability(encode, checkSimilarity):
    if (encode > checkSimilarity):
        return (encode - checkSimilarity) * 100
    else:
        return (checkSimilarity - encode) * 100


if __name__ == '__main__':
    TotalProbability()
