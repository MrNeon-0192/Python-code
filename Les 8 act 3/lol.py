mean1=38
wrong_number=56
correct_number=36
total_number=40

sum=mean1*total_number

print("The sum of 40 numbers is: " + str(sum))

num2=sum-((wrong_number-correct_number))
print("sum-((wrong_number-correct_number)): " + str(num2))

mean2=num2/total_number
print("The new mean is: " + str(mean2))