# შექმენით სია ამ სიაში ჩაწერეთ სხვადასხვა რიცხვები და
#  გამოიტანეთ ამ სიაში ყველა რიცხვების ჯამი
#  ასევე ამ სიიდან უნდა დაპრინტონთ ყველა რიცხვი ცალკ ცალკე ლუწია თუ კენტი

#1 sum

my_nums = [2,4,5,7,3,16,30]

sum = 0 

for num in my_nums:
    sum += num
print(sum)

#2 even or odd numbers

my_nums = [2,4,5,7,3,16,30]
for num in my_nums:
    if num % 2 == 1:
        print(str(num)+ " არის კენტი")
    else:
        print(str(num) + " არის ლუწი")

