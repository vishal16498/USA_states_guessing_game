import turtle
import pandas
screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
states_info = pandas.read_csv("50_states.csv")
states_list = states_info.state.to_list()
# print(states_list)
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
guessed_states = []
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"Guess the US state: Your score is {score}/50", prompt="What's the state name?")
    user_input = answer_state.title()
    if user_input in states_list:
        score += 1
        guessed_states.append(user_input)
        state_name = states_info[states_info.state == user_input]
        text_turtle.goto(int(state_name.x), int(state_name.y))
        text_turtle.write(arg=f"{user_input.title()}", align="Center", font=("Arial", 8, "normal"))
    if score == 50 or user_input == "Exit":
        break
missed_states = [each for each in states_list if each not in guessed_states]
print(missed_states)
missing_states = pandas.DataFrame(missed_states)
missing_states.to_csv("states_to_practice.csv")
# screen.exitonclick()
turtle.mainloop()
