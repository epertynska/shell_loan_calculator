import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["diff", "annuity"])
parser.add_argument("-p", "--principal")
parser.add_argument("-m", "--periods")
parser.add_argument("-i", "--interest")
parser.add_argument("-a", "--payment")
args = vars(parser.parse_args())
if args["principal"] != None:
    principal = int(args["principal"])
if args["periods"] != None:
    periods = int(args["periods"])
if args["interest"] != None:
    interest = float(args["interest"]) / 1200
if args["payment"] != None:
    payment =  int(args["payment"])
keys_control = [i for i in args.values() if i != None]
# checking incorrect
if (args["type"] != None and len(keys_control) < 4) or (args["type"] == None) or (args["type"] == "diff" and args["payment"] != None) or any(keys_control) < 0:
    print("Incorrect parameters")

# monthly payments different
if args["type"] == "diff" and args["principal"] != None and args["interest"] != None and args["periods"] != None and args["payment"] == None:
    i = 1
    total = []
    while i <= periods:
        payment = math.ceil((principal / periods) + interest * (principal - (principal * (i - 1) / periods)))
        print("Month {}: payment is {}".format(i, payment))
        total.append(payment)
        i += 1
    print()
    print("Overpayment = {}".format(math.ceil(sum(total) - principal)))

# annual monthly payments
if args["type"] == "annuity" and args["principal"] != None and args["interest"] != None and args["periods"] != None and args["payment"] == None:
    payment = math.ceil(principal * (((interest * math.pow((1 + interest), periods))) / ((math.pow((1 + interest), periods)) - 1)))
    print("Your annuity payment = {}!".format(int(payment)))
    print("Overpayment = {}".format(math.ceil(payment * periods - principal)))

# principal
if args["type"] == "annuity" and args["payment"] != None and args["principal"] == None and args["interest"] != None and args["periods"] != None:
    equation = payment / (((interest * math.pow((1 + interest), periods))) / ((math.pow((1 + interest), periods)) - 1))
    print("Your loan principal = {}!".format(int(equation)))
    print("Overpayment = {}".format(math.ceil(payment * periods - int(equation))))

# periods
if args["type"] == "annuity" and args["payment"] != None and args["principal"] != None and args["interest"] != None and args["periods"] == None:
    equation = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    if 1 < equation < 12:
        print(f"It will take {equation} months to repay this loan!")
    elif equation == 1:
        print(f"It will take {equation} month to repay this loan!")
    elif equation == 12:
        print(f"It will take {equation} year to repay this loan!")
    elif equation > 12:
        if equation % 12 == 0:
            years = equation // 12
            print(f"It will take {years} years to repay this loan!")
        else:
            years = equation // 12
            months = equation % 12
            if months == 1 and years > 1:
                print(f"It will take {years} years and {months} month to repay this loan!")
            elif months == 1 and years == 1:
                print(f"It will take {years} year and {months} month to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
    print("Overpayment = {}".format(math.ceil(payment * equation - principal)))
