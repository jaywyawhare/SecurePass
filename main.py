from src.entropy import encode
from src.generate import password_generator
from src.probability import TotalProbability
from src.similarity import checkSimilarity


if __name__ == '__main__':
    print("Welcome to password utility:\nSelect one from below.\n1. Check password strength.\n2. Generate strong password.\nPress 'q' to exit.")
    choice = input("Enter a number: ")
    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        tp = TotalProbability(
            encode(password), checkSimilarity(username, password))
        print("Password strength: ", round(tp, 3))
    elif choice == '2':
        print("Your strong password: ", password_generator())
