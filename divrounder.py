def divround(Number, DivisibleBy):
    done = False
    Number = int(Number)
    InitNumber = Number
    AddSubstractBy = 0
    while not done:
        AddSubstractBy += 1 #Calculates how much its going to add and substract for this instance of the loop

        Number = InitNumber #resets num back to the intial value
        Number += AddSubstractBy # Adds value to the number
        Result = Number/DivisibleBy #Division
        if round(Result) == Result: #Checks if there is a remainder
            break

        Number = InitNumber #resets num back to the intial value
        Number -= AddSubstractBy # Substracts value to the number
        Result = Number/DivisibleBy #Division
        if round(Result) == Result: #Checks if there is a remainder
            break
            
    return Number