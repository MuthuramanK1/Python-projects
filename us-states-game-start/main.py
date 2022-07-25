import turtle
import pandas

FONT_ = ("Courier", 6, "normal")
screen = turtle.Screen()
screen.setup(725, 491)
image = "us-states-game-start/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
# getting the csv to a avariable with PANDAS
data = pandas.read_csv("us-states-game-start/50_states.csv")
states = data["state"].to_list()
# getting length of the states for scoring purpose
states_len = len(states)

# turtle to write the states name in screen
state_writing = turtle.Turtle()
state_writing.hideturtle()
state_writing.penup()


answer = screen.textinput(title="Guess another state",
                          prompt="What's the another state's name?").title()
score = 0
# None is returned when clicked cancel
while answer != None and score < 49:
    # enter exit to get out from game
    if answer == "Exit":
        break
    # check the states list for entered state
    if answer in states:
        # getting the value of x and  y from dataframe and convert it into integer
        state_x = int(data[data.state == answer].x)
        state_y = int(data[data.state == answer].y)
        state_position = (state_x, state_y)
        score += 1
        # removing correct answer from states list for creating missed states csv
        # and for not scoring repeated answers
        states.remove(answer)
        state_writing.goto(state_position)
        state_writing.write(answer)

    answer = screen.textinput(title=f"{score}/{states_len} state",
                              prompt="What's the another state's name?").title()

# creating dataframe and convert it into csv file.Thanks panda🐼
missed_states = {
    "states_to_learn": states
}
missed_states_df = pandas.DataFrame(missed_states)
missed_states_df.to_csv("us-states-game-start/missed_states.csv")
turtle.mainloop()
