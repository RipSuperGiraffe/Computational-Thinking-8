byrek_points = 0
solBowl_points = 0
starbucks_points = 0
batch_points = 0
subway_points = 0

answer1 = input("wheres the best to eat during lunch at A byrek, B SolBowl, C Starbucks, D Batch, E Subway" )
if answer1 == "A":
    byrek_points += 1
if answer1 == "B":
    solBowl_points += 1
if answer1 == "C":
    starbucks_points += 1
if answer1 == "D":
    batch_points += 1
if answer1 == "E":
    subway_points += 1

answer2 = input("Do you perfer on a random Wensday (your very hungry) A fries, B Chicken tenders, C Custom drinks, D Pizza, E a Sub" )
if answer2 == "A":
    byrek_points += 1
if answer2 == "B":
    solBowl_points += 1
if answer2 == "C":
    starbucks_points += 1
if answer2 == "D":
    batch_points += 1
if answer2 == "E":
    subway_points += 1
    
answer3 = input("If you not tryna spend to much money where do you go for lunch? A byrek, B SolBowl, C Starbucks, D Batch, E Subway" )
if answer3 == "A":
    byrek_points += 1
if answer3 == "B":
    solBowl_points += 1
if answer3 == "C":
    starbucks_points += 1
if answer3 == "D":
    batch_points += 1
if answer3 == "E":
    subway_points += 1

answer4 = input("If you have UNLIMITED money where are you going to eat lunch? A byrek, B SolBowl, C Starbucks, D Batch, E Subway" )
if answer4 == "A":
    byrek_points += 1
if answer4 == "B":
    solBowl_points += 1
if answer4 == "C":
    starbucks_points += 1
if answer4 == "D":
    batch_points += 1
if answer4 == "E":
    subway_points += 1

answer3 = input("If you had to work at one of these places where would you work?? A byrek, B SolBowl, C Starbucks, D Batch, E Subway" )
if answer3 == "A":
    byrek_points += 1
if answer3 == "B":
    solBowl_points += 1
if answer3 == "C":
    starbucks_points += 1
if answer3 == "D":
    batch_points += 1
if answer3 == "E":
    subway_points += 1

if byrek_points >= solBowl_points and byrek_points >= starbucks_points and byrek_points >= batch_points and byrek_points >= subway_points:
    print ("You like Byrek the most! (Its the best one)")
elif solBowl_points >= byrek_points and solBowl_points >= starbucks_points and solBowl_points >=batch_points and solBowl_points >=subway_points:
    print (" you like Solbowl the most! (second best one)")
elif starbucks_points >= byrek_points and starbucks_points >= solBowl_points and starbucks_points >= batch_points and starbucks_points >= subway_points:
    print("you like starbucks the most! (so exspensive)")
elif batch_points >= byrek_points and batch_points >= solBowl_points and batch_points >= starbucks_points and batch_points >= subway_points:
    print("you like batch the most(overrated)")
elif subway_points >= byrek_points and subway_points >= solBowl_points and subway_points >= starbucks_points and subway_points >= batch_points:
    print ("you like subway the most! (perfectly rated)")
