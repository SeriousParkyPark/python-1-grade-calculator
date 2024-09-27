lpp1 = int(input("Enter the number of labs completed: "))
if lpp1 > 6: 
    lpp1 = 6

lpp2 = (lpp1 / 6) * 20

qica1 = int(input("Enter the number of quizzes completed:"))
if qica1 > 6:
    qica1 = 6 

qica2 = (qica1 / 6) * 15

as1 = float(input("Enter grade for Assignment 1: "))
as2 = float(input("Enter grade for Assignmnet 2: "))
as3 = float(input("Enter grade for Assignment 3: "))
as4 = float(input("Enter grade for Assignment 4: ")) 
as5 = ((as1 + as2 + as3 + as4) / 4) * 0.16

mt1 = float(input("Enter grade for Midterm 1: ")) 
mt2 = float(input("Enter grade for Midterm 2: "))
mt3 = ((mt1 + mt2) / 2) * 0.25

fn1 = float(input("Enter grade for Final Exam: "))
fn2 = fn1 * 0.18

mtfp1 = float(input("Enter grade for Midterms and Final Preperation: "))
mtfp2 = mtfp1 * 0.06

grade = round(lpp2 + qica2 + as5 + mt3 + fn2 + mtfp2)
print("Your grade is: " + grade)
