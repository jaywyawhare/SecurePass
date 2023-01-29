from src.entropy import encode
from src.generate import password_generator
from src.probability import TotalProbability
from src.similarity import checkSimilarity


if __name__ == '__main__':
    # print("Welcome to password utility:\nSelect one from below.\n1. Check password strength.\n2. Generate strong password.\nPress 'q' to exit.")
    # choice = input("Enter a number: ")
    # if choice == '1':
    #     username = input("Enter your username: ")
    #     password = input("Enter your password: ")
    #     tp = TotalProbability(
    #         encode(password), checkSimilarity(username, password))
    #     print("Password strength: ", round(tp, 3))
    # elif choice == '2':
    #     print("Your strong password: ", password_generator())
    username = ["7zHi8Y", "hdMQw0", "jKLOdP", "3pVJjd", "ZLm3vu", "UvdigG", "kSGzrE", "0mYH3G", "h0IFdz", "w348Nn", "vmshqc", "AZf3YO", "vnab0o", "amv8tf", "HxyuYJ", "uj4B0t", "xwPKnO", "YAHwZz", "1t46nl", "Ucjvk9", "3zfWZv", "bAv8jn", "PQyJet", "kCUR8V",
                "nsA2pM", "V4Y7kU", "1NMutO", "2xXClb", "54nFGw", "dK8CmT", "JFTBTw", "t7B7bx", "A89CEc", "JvwE2D", "W7W1WF", "6ZMez8", "I3VtRC", "IdPghq", "1zMEqo", "q8pEw0", "Wd1b6S", "5igojq", "VOpJH4", "L2FtpF", "6mzQdY", "2meZac", "wAJdAV", "r0E33G", "boGmSE", "9T73Qc", "gTyt8Pb6X", "jyOtrD3MU", "Xu9mc0309", "XLM6PCAAv", "7PFOUBjjC", "uvGHLQFkR", "gwb0kZrlY", "ac2wL5sC5", "Mn9zy8JNy", "62XX4XNW8", "MSs4HjSyq", "lS4FH4CAD", "Hksq7FbT4", "7ZeOZ6PjC", "GLcQKS2mO", "EQ7bbrtcg", "x1NFCYaam", "FSfgDCKKc", "38BgOM87s", "3aAyigq8G", "viTL0TJ7S", "WK4ze3kDT", "PovybIdUq", "wMWHg4r2q", "rf9gXzO6c", "11S2waEDP", "0RG29KFpj", "reQDo1wVr", "TPRqCPL8e", "MOJOqyqsz", "rq0QKo6hO", "pb49exsar", "neHXJ6MSh", "BitNQvO0s", "OF5LugI9u", "Yn9GgYZG8", "otvRfX5Ei", "mYSj2pwan", "Xsr2KtCnW", "WpR047Ywk", "d26id6dTr", "iEGlBw9RM", "PttGuP2jw", "7LvZtW8ck", "GOdgqsZq3", "juCJHcdRp", "riF7J3e42", "KRtHSl8YU", "ApSvtkUzK", "urRJP2l5Q", ]

    for uname in username:
        passwod = password_generator()
        tp = TotalProbability(
            encode(passwod), checkSimilarity(uname, passwod))
        print("Password strength: ", round(tp, 4),
              "\tUsername :", uname, "\tPassword : ", passwod)
