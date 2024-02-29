import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIA_STATES")
image = "/Users/debasishpal/India_States/political-map.gif"

data = pandas.read_csv("data.csv")
state_list = data['State'].to_list()


def reset():
    screen.addshape(image)
    turtle.shape(image)


ans = 0
while ans != 28:
    reset()

    answer_state = screen.textinput(title=f'{ans}/28 GUESS THE STATE', prompt="WHAT'S ANOTHER STATE NAME ? ")
    if answer_state in state_list:
        turtle.shape('circle')
        ans += 1

        row = data.loc[data['State'] == answer_state]

        # Extract the values of x and y from the row
        x_value = row.iloc[0]['X']
        y_value = row.iloc[0]['Y']
        turtle.penup()
        turtle.goto(x_value, y_value)
        turtle.write(answer_state, font=("Arial", 12, "bold"))
        turtle.goto(0, 0)

screen.exitonclick()
