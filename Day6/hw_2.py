#მომხმარებელს შეეკითხეთ ხელფასი 
# თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
# თუ 1000--10000-ია, დაუპრინტეთ you mid
# თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

user_salary = int(input("enter your salary: "))

if user_salary > 10000:
    print("გოა-ში სწავლობდი?")
elif user_salary <= 10000 and user_salary >= 1000:
    print("you mid")
else:
    print("შემოსულიყავი გოაში, მატრიცელო")