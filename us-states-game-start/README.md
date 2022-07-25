# This is United States guessing game created using turtle modules and Pandas in python.

> I've implemented the things, I learnt.

```
# creating dataframe and convert it into csv file.Thanks panda🐼
missed_states = {
    "states_to_learn": states
}
missed_states_df = pandas.DataFrame(missed_states)
missed_states_df.to_csv("us-states-game-start/missed_states.csv")

#Starts event loop
turtle.mainloop()

```

> this is the most important section of the project.
>creates the csv file from the missed states name, so we can learn from it.

