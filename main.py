import turtle
import pandas


tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

screen = turtle.Screen()
image = "PATH_TO/india.gif"

screen.addshape(image)
turtle.shape(image)


screen.title("India states Game.")



def mark(answer_state):
    new_state = data[data.state == answer_state]
    x_coor = new_state.x.values[0]
    y_coor = new_state.y.values[0]
    tim.goto(x=x_coor, y=y_coor)
    tim.write(answer_state)


data = pandas.read_csv("PATH_TO/Book1.csv")
all_state = data.state.tolist()

guessed_state = []
missed_state = []


while len(guessed_state) < 29:
    answer_state = screen.textinput(
        title=f"You guessed {len(guessed_state)}/29 States",
        prompt="What's another state's name?:",
    ).title()

    if answer_state == "Exit":
        for state in all_state:
            if state not in guessed_state:
                missed_state.append(state)

        new_data = pandas.DataFrame(missed_state)
        new_data.to_csv("states to learn.csv")
        break

    if answer_state in all_state:
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x.item()), int(state_data.y.item()))
        # print(state_data.x)
        tim.write(state_data.state.item())
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)


