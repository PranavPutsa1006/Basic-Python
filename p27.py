score = int(input("Enter student's score"))
if(score>=0 and score<=100):
    if score >= 90:
        print("Grade: A")
    else:
        if score >= 80:
            print("Grade: B")
        else:
            if score >= 70:
                print("Grade: C")
            else:
                if score >= 60:
                    print("Grade: D")
                else:
                    print("Grade: F")
else:
    print("Invalid score")