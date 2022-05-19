from turtle import Turtle, Screen
import pandas
from score import Score


screen = Screen()
screen.setup(width=750, height=495)
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
score = Score()

screen.bgpic("blank_states_img.gif")



data = pandas.read_csv("50_states.csv")
data_states = data.state

states_list = data.state.to_list()
states_list

data_dict = data.to_dict()
data_dict

guessed_states = []

game_is_on = True
while game_is_on :
    answer_state = screen.textinput(title=f"{score.current_score}/{score.max_score} Guess the State",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    if score.current_score < 50:
        for item in states_list:
            if answer_state == item :
                guessed_states.append(item)
                item_index = states_list.index(item)
                state_name = data_dict["state"][item_index]
                state_xcor = data_dict["x"][item_index]
                state_ycor = data_dict["y"][item_index]
                new_turtle = Turtle()
                new_turtle.hideturtle()
                new_turtle.penup()
                new_turtle.goto(state_xcor, state_ycor)
                new_turtle.write(f"{state_name}")
                score.increase_score()

    else:
        game_is_on = False
        print("You got all the states correct. You Won")

missing_states = [state for state in states_list if state not in guessed_states]


new_data = pandas.DataFrame(missing_states)

new_data.to_csv("States to learn")
