import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# by this code we get all coor. for use on the map
# def get_mouse_click_coor(x, y):
# print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# this keep our screen open
# turtle.mainloop()

df = pandas.read_csv("50_states.csv")


def write_state(x, y):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.setposition(x, y)
    text.write(picked_state)


df_list = df.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What is another state?").title()

    picked_state = ""
    if answer_state == "Exit":
        missing_state = [state for state in df_list if state not in guessed_state]
        data = pandas.DataFrame(missing_state)
        data.to_csv("Which name of states you should learn.")
        break

    for state in df.state:
        if answer_state.lower() == state.lower():
            picked_state = state
            guessed_state.append(picked_state)

    # TODO add condition which you allow to keep guessing in case there will be mistake in spelling
    # now it is error

    
    # get the coordination
    coor_x = int(df[df.state == picked_state]["x"])
    coor_y = int(df[df.state == picked_state]["y"])

    write_state(coor_x, coor_y)



# screen.exitonclick()
