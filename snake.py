from snake_game import SnakeGame
import time

game = SnakeGame()
time.sleep(1)  # give window time to appear

def decide_move(head, apple):
    sx, sy = head
    ax, ay = apple
    # Prefer horizontal moves first if distance is larger
    if abs(ax - sx) > abs(ay - sy):
        return "RIGHT" if ax > sx else "LEFT"
    else:
        return "DOWN" if ay > sy else "UP"

# Main AI loop
while not game.game_close:
    head, apple = game.get_state()
    move = decide_move(head, apple)
    game.move_snake(move)
    game.step()
