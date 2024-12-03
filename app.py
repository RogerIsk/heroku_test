from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Check for draw
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Draw"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global board, current_player
    data = request.json
    row, col = data['row'], data['col']

    if board[row][col] == "":
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            return jsonify({"winner": winner})
        current_player = "O" if current_player == "X" else "X"
        return jsonify({"winner": None})
    return jsonify({"error": "Invalid move"}), 400

if __name__ == '__main__':
    app.run(debug=True)
