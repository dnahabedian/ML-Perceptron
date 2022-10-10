# perceptron.py

#   This is the main function of the program. It handles setting up the initial values of
#       poutput (output of the perceptron), the passCount, and examplesCount (which is used
#       for traversing the examples list). The function then calculates the sum of the current
#       input based on the value of the weight and example and compares that sum to the threshold.
#       If needed, the function will adjust the weights based on the adjustmentFactor value if the
#       predicted output does not match what the actual value is.
def perceptron(threshold, adjustmentFactor, weights, examples, passes):

    poutput = False
    passCount = 1
    examplesCount = 0

    print("Starting weights: ", weights)
    print("Threshold: ", threshold, " Adjustment: ", adjustmentFactor)

    while (passCount <= passes):
        count = 0
        print("\nPass ", passCount, "\n")

        while (examplesCount < len(examples)):
            sum = 0

            print("inputs: ", examples[examplesCount][1])

            for x in range(len(weights)):
                currExample = examples[examplesCount][1]
                sum += currExample[x] * weights[x]

            if sum > threshold:
                poutput = True
            else:
                poutput = False

            print("prediction: ", poutput,
                  " answer: ", examples[examplesCount][0])

            if poutput != examples[examplesCount][0]:
                currExample = examples[examplesCount]

                if poutput is False:
                    for x in range(len(weights)):
                        if currExample[1][x] == 1:
                            weights[x] += adjustmentFactor
                else:
                    for x in range(len(weights)):
                        if currExample[1][x] == 1:
                            weights[x] -= adjustmentFactor

            print("adjusted weights: ", weights)
            examplesCount += 1

        passCount += 1
        count += 1
        examplesCount = 0

    print()
