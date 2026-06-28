import random
import time
import os

# ================= LOADING BAR =================
def loading_bar():
    print("Starting Game Pack...\n")
    for i in range(0, 101, 10):
        bar = "█" * (i // 10) + " " * (10 - i // 10)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.2)
    print("\nReady!\n")

# ================= TIC TAC TOE =================
def tic_tac_toe():
    print("\n=== Tic Tac Toe ===")
    print("1. Vs Bot")
    print("2. Vs Friend")

    mode = input("Choose mode: ")

    if mode == "1":
        play_vs_bot()
    elif mode == "2":
        play_vs_friend()

def print_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_win(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def get_moves(board):
    return [i for i in range(9) if board[i] == " "]

def play_vs_friend():
    board = [" "] * 9
    for turn in range(9):
        print_board(board)
        player = "X" if turn % 2 == 0 else "O"

        move = int(input(f"Player {player}, move (0-8): "))
        if board[move] != " ":
            print("Invalid!")
            continue

        board[move] = player

        if check_win(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            return
    print("Draw!")

# ----- BOT -----
def play_vs_bot():
    board = [" "] * 9
    human, bot = "X", "O"

    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Impossible")
    diff = input("Choose: ")

    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:
            move = int(input("Your move (0-8): "))
            if board[move] != " ":
                print("Invalid!")
                continue
            board[move] = human

            if check_win(board, human):
                print_board(board)
                print("🎉 You win!")
                return
        else:
            if diff == "1":
                move = random.choice(get_moves(board))
            elif diff == "2":
                if random.random() < 0.5:
                    move = best_move(board, bot, human)
                else:
                    move = random.choice(get_moves(board))
            else:
                move = minimax_best(board, bot, human)

            board[move] = bot
            print(f"Bot: {move}")

            if check_win(board, bot):
                print_board(board)
                print("🤖 Bot wins!")
                return

    print("Draw!")

def best_move(board, bot, human):
    for move in get_moves(board):
        board[move] = bot
        if check_win(board, bot):
            board[move] = " "
            return move
        board[move] = " "

    for move in get_moves(board):
        board[move] = human
        if check_win(board, human):
            board[move] = " "
            return move
        board[move] = " "

    if 4 in get_moves(board):
        return 4

    return random.choice(get_moves(board))

# ----- MINIMAX -----
def minimax(board, is_max, bot, human):
    if check_win(board, bot): return 1
    if check_win(board, human): return -1
    if " " not in board: return 0

    if is_max:
        best = -999
        for m in get_moves(board):
            board[m] = bot
            best = max(best, minimax(board, False, bot, human))
            board[m] = " "
        return best
    else:
        best = 999
        for m in get_moves(board):
            board[m] = human
            best = min(best, minimax(board, True, bot, human))
            board[m] = " "
        return best

def minimax_best(board, bot, human):
    best_score = -999
    move_choice = None
    for m in get_moves(board):
        board[m] = bot
        score = minimax(board, False, bot, human)
        board[m] = " "
        if score > best_score:
            best_score = score
            move_choice = m
    return move_choice

# ================= NUMBER GUESS =================
def number_guess():
    num = random.randint(1, 100)
    while True:
        g = int(input("Guess (1-100): "))
        if g < num: print("Too low")
        elif g > num: print("Too high")
        else:
            print("Correct!")
            break

# ================= HANGMAN =================
def hangman():
    words = ["python","keyboard","developer","algorithm","network",
             "software","hardware","database","function","variable"]

    used = []

    while True:
        available = [w for w in words if w not in used]
        if not available:
            print("You completed all words!")
            break

        word = random.choice(available)
        used.append(word)

        guessed = ["_"] * len(word)
        attempts = 6
        letters = []

        while attempts > 0 and "_" in guessed:
            print("\nWord:", " ".join(guessed))
            print("Guessed:", letters)
            print("Attempts:", attempts)

            guess = input("Letter: ").lower()

            if guess in letters:
                continue

            letters.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed[i] = guess
            else:
                attempts -= 1

        if "_" not in guessed:
            print("You win!", word)
        else:
            print("You lose!", word)

        if input("Play again? (y/n): ") != "y":
            break

# ================= RPS =================
def rps():
    choices = ["rock","paper","scissors"]
    user = input("rock/paper/scissors: ").lower()

    random.shuffle(choices)
    comp = random.choice(choices)

    time.sleep(random.uniform(0.3,1.0))
    print("Computer:", comp)

    if user == comp:
        print("Draw")
    elif (user=="rock" and comp=="scissors") or \
         (user=="paper" and comp=="rock") or \
         (user=="scissors" and comp=="paper"):
        print("You win!")
    else:
        print("You lose!")

# ================= SIMPLE REAL-TIME SNAKE =================
import os
import time
import random

def snake():
    width, height = 10, 10
    snake = [[5, 5]]  # initial position
    direction = [0, 1]  # start moving right
    food = [random.randint(0, height-1), random.randint(0, width-1)]
    snake_length = 1
    alive = True

    print("Use w/a/s/d keys to move. Press Enter after key.")

    while alive:
        os.system('clear')  # use 'cls' on Windows

        # Draw the grid
        for y in range(height):
            for x in range(width):
                if [y, x] == snake[0]:
                    print("S", end=" ")  # head
                elif [y, x] in snake[1:]:
                    print("s", end=" ")  # body
                elif [y, x] == food:
                    print("F", end=" ")  # food
                else:
                    print(".", end=" ")
            print()

        # Get input for direction
        key = input("Move (w/a/s/d): ").lower()
        if key == "w": direction = [-1, 0]
        elif key == "s": direction = [1, 0]
        elif key == "a": direction = [0, -1]
        elif key == "d": direction = [0, 1]

        # Move snake
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        # Check collision
        if head in snake or not (0 <= head[0] < height and 0 <= head[1] < width):
            print("💀 Game Over!")
            alive = False
            break

        snake.insert(0, head)

        # Eat food → grow by 1 letter
        if head == food:
            snake_length += 1
            food = [random.randint(0, height-1), random.randint(0, width-1)]
        else:
            # trim tail to maintain current length
            snake = snake[:snake_length]

        time.sleep(0.2)  # speed of snake
# ================= MAIN =================
def main():
    loading_bar()

    while True:
        print("\n=== 🎮 GAME PACK ===")
        print("1. Snake")
        print("2. Tic Tac Toe")
        print("3. Number Guess")
        print("4. Hangman")
        print("5. Rock Paper Scissors")
        print("6. Save & Exit")

        choice = input("Choose: ")

        if choice == "1":
            snake()
        elif choice == "2":
            tic_tac_toe()
        elif choice == "3":
            number_guess()
        elif choice == "4":
            hangman()
        elif choice == "5":
            rps()
        elif choice == "6":
            print("\nSaving progress...")
            time.sleep(1.5)
            print("Saved! ✅")
            break
        else:
            print("Invalid choice")

# RUN
main()
