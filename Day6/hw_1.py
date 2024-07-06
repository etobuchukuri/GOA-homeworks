#მომხმარებლის ნიშნებისგან გამოიანგარიშება საშვალო არითმეტიკული
#და თუ ცხრაზე მეტი იქნება 

#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგრცა 300 ლარიანი ბანძი ტოსტერი
#  რისთვისაც შეალიე შენი ცხოვრების წლები

#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას

#თუ იქნება 5 დან 9 მდე დაუპრინტე YOU ARE MID

#თუ 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you

subj1 = int(input("enter your subj1 score: "))
subj2 = int(input("enter your subj2 score: "))
subj3 = int(input("enter your subj3 score: "))

score_avrg = (subj1 + subj2 + subj3) / 3

if score_avrg > 9:
    print("გილოცავ მატრიცელო შენ გადმოგრცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები")
elif score_avrg < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif score_avrg >= 5 and score_avrg < 9:
    print("YOU ARE MID")
else:
    print("there is something wrong with you")




