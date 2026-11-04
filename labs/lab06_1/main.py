# Starting file for LAB 6-1
# Include your course number, student first and last name, and date in the comment header

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores= [] # initialize an empty list
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores 
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                # add score to list
                scores.append(score) 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total = 0 # set a counter for total scores
    for score in scores:
        total += score

    # calculate average score
    average = round(total / len(scores))

    # get the min and max value
    low_score = min(scores)
    high_score = max(scores)

    # get the median
    median_index = len(scores) // 2

    if len(scores) % 2 == 1: # if it is odd 
        median_score = scores[median_index]
    else: # if it is even we have to add values togther and divide
        middle1 = scores[median_index]
        middle2 = scores[median_index - 1]
        median_score = (middle1 + middle2) / 2


    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low score:         ", low_score)
    print("Hgih score:         ", high_score)
    print("Median score:         ", median_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

