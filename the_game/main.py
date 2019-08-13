# from quiz_game import Quiz_Game

def load_questions(filename):
    rounds = []
    quest_list = []
    game = "game.txt"
    file = open(game, 'r')
    num_rounds = int(next(file))
    rounds = [[next(file) for i in range(4)]]
    for i in range(num_rounds-1):
        next(file)
        question = [next(file) for i in range(4)]
        rounds.append(question)
    return rounds

def game_loop():
    FILENAME = 'game.txt'
    questions = load_questions(FILENAME)
    game = Quiz_Game(questions)
    while Game.complete == False:
        Game.ask_question()
    Game.display_final_score()

if __name__ == '__main__':
    rounds = load_questions('game.txt')
    for r in rounds:
        print('------------------------')
        for question in r:
            print(question)
