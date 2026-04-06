import pandas
import turtle

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score=0
data=pandas.read_csv("50_states.csv")


all_states=data.state
corrected_state = []
while len(corrected_state) < 50:
    answer_output = screen.textinput(title=f"{score}/50 Guess The State",
                                     prompt="Whats Another States Name ").capitalize()

    if answer_output == "exit":
        missing_state = []
        for state in all_states:
            if state not in corrected_state:
                missing_state.append(state)
        print(missing_state)
        break

    state_name=data['state']
    for name in state_name:
        if name == answer_output:
            state_data=data[data.state == answer_output]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            print("True")
            score += 1
            t.goto(int(state_data.x.item()),int(state_data.y.item()))
            t.write(name,align="center",font=("Courier",10,"normal"))


screen.exitonclick()


