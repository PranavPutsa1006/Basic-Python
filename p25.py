shopping = ["Bread","Butter","Jam"]
print(shopping)
for i in shopping:    # here you shouldn't use shopping(3)
    print(i)
shopping.append("Mayonnaise")
print(shopping)
for i in range(4):
    print(shopping[i])
print(shopping[0])
shopping[1]="Sauce"
print(shopping)