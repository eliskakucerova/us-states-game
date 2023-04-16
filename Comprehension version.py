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
    text.write(answer_state)


df_list = df.state.to_list()

guessed_state = []
count_guessed_state = 0
while count_guessed_state < 50:
    answer_state = screen.textinput(title=f"{count_guessed_state}/50 States Correct",
                                    prompt="What is another state?").title()

    if answer_state == "Exit":
        data = pandas.DataFrame(df_list)
        data.to_csv("Which name of states you should learn.")
        break

    # add if else condition in list comprehension
    # PROBLEM because of the while loop te list guessed state is overwritten
    # so instead of appending new state it always create a new list and add only one answer_state
    # SOLUTION?

    guessed_state = [state for state in df_list if answer_state == state]
    df_list.remove(answer_state)

    # get the coordination
    coor_x = int(df[df.state == answer_state]["x"])
    coor_y = int(df[df.state == answer_state]["y"])

    write_state(coor_x, coor_y)


# screen.exitonclick()
