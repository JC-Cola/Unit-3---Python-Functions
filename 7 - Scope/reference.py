#Scope - The visibility of variables, where it can be seen and used
#Global - outside all functions (visible everywhere)
#Local - inside a function (only visible there)

# The Bug
def add_bonus():
    score = score+  100 # = Python thinks it's local

score = 500
add_bonus()