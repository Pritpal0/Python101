#Pritpal Singh
#CS101 MWF 12PM-12:50PM
#Created 9/4/2017
#Due 9/9/2017

#variables for ingredient, so it can be changed later on
it_sm_bread=float(0.5) #amount of bread for small italian
it_lg_bread=int(1) #amount of bread for large italian
it_sm_salami=float(0.3) #amount of salami for small italian
it_lg_salami=float(0.5) #amount of salami for large italian
it_sm_vegetables=float(0.2) #amount of vegetables for small italian
it_lg_vegetables=float(0.5) #amount of vegetables for large italian
it_sm_cheese=int(4) #amount of cheese for small italian
it_lg_cheese=int(8) #amount of cheese for large italian
veg_sm_bread=float(0.5) #amount of bread for small vegetarian
veg_lg_bread=int(1) #amount of bread for large vegetarian
veg_sm_vegetables=float(0.5) #amount of vegetables for small vegetarian
veg_lg_vegetables=float(1.2) #amount of vegetables for large vegetarian
veg_sm_cheese=int(5) #amount of cheese for small vegetarian
veg_lg_cheese=int(11) #amount of cheese for large vegetarian
tb_sm_bread=float(0.5) #amount of bread for small TBird
tb_lg_bread=int(1) #amount of bread for large TBird
tb_sm_turkey=float(0.4) #amount of turkey for small TBird
tb_lg_turkey=float(0.9) #amount of turkey for large TBird
tb_sm_cheese=int(3) #amount of cheese for small TBird
tb_lg_cheese=int(8) #amount of cheese for large TBird

small_italian=input("How many small Italians were sold? :") #Will ask for how many small italian sandwiches were sold
large_italian=input("How many large Italians were sold? :") #Will ask for how many large italian sandwiches were sold
print()
small_veg=input("How many small Vegetarians were sold? :") #Will ask for how many small vegetarian sandwiches were sold
large_veg=input("How many large Vegetarians were sold? :") #Will ask for how many large vegetarian sandwiches were sold
print()
small_tbird=input("How many small TBirds were sold?: ") #Will ask for how many small T Bird sandwiches were sold
large_tbird=input("How many large TBirds were sold?: ") #Will ask for how many large T Bird sandwiches were sold
print()

small_italian=int(small_italian) #takes the number of small italian and converts the input to a int
large_italian=int(large_italian) #takes the number of large italian and converts the input to a int
small_veg=int(small_veg) #takes the number of small vegetarian and converts the input to a int
large_veg=int(large_veg) #takes the number of large vegetarian and converts the input to a int
small_tbird=int(small_tbird) #takes the number of small t bird and converts the input to a int
large_tbrid=int(large_tbird) #takes the number of large t bird and converts the input to a int

breadtotal=(small_italian*it_sm_bread)+(small_veg*veg_sm_bread)+(small_tbird*tb_sm_bread)+(large_italian*it_lg_bread)+(large_veg*veg_lg_bread)+(large_tbird*tb_lg_bread) #equation will multiply the total number of each sandwhich is sold and then add all different types togather for a final count
salamitotal=(small_italian*it_sm_salami)+(large_italian*it_lg_salami) #equation will multiply the total number of each sandwhich is sold and then add all different types togather for a final count
vegestotal=(small_italian*it_sm_vegetables)+(small_veg*veg_sm_vegetables)+(large_italian*it_lg_vegetables)+(large_veg*veg_lg_vegetables) #equation will multiply the total number of each sandwhich is sold and then add all different types togather for a final count
cheesetotal=(small_italian*it_sm_cheese)+(small_veg*veg_sm_cheese)+(small_tbird*tb_sm_cheese)+(large_italian*it_lg_cheese)+(large_veg*veg_lg_cheese)+(large_tbird*tb_lg_cheese) #equation will multiply the total number of each sandwhich is sold and then add all different types togather for a final count
turkeytotal=(small_tbird*tb_sm_turkey)+(large_tbird*tb_lg_turkey) #equation will multiply the total number of each sandwhich is sold and then add all different types togather for a final count

print("You have used") #prints a line "you have used"
print(breadtotal, "Loaves of bread") #prints the total calculated bread
print(salamitotal, "lbs of Salami") #prints the total calculated salami
print(vegestotal, "lbs of Veges") #prints the total calculated vegetables
print(cheesetotal, "Slices of Cheese") #prints the total calculated cheese
print(turkeytotal, "lbs of Turkey") #prints the total calculated turkey
