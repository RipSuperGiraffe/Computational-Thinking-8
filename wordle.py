import random

# Pick a word at random
word_list = ["about","above","abuse","actor","acute","admit","adopt","adult","after","again","agent","agree","ahead","alarm","album","alert","allow","alone","along","alter","among","anger","angle","angry","apart","apple","apply","arena","argue","arise","array","aside","asset","audio","audit","avoid","award","aware","bacon","badge","beach","beard","begin","being","below","bench","birth","black","blame","blind","block","blood","board","brain","brand","bread","break","brick","brief","bring","broad","brown","build","bunch","buyer","cable","carry","catch","cause","chain","chair","chart","check","chest","chief","child","claim","class","clean","clear","clerk","click","clock","close","coach","coast","could","count","court","cover","craft","crash","cream","crime","cross","crowd","crown","curve","cycle","daily","dance","dated","dealt","death","debut","delay","depth","dirty","doubt","dozen","draft","drama","dream","dress","drink","drive","dying","eager","early","earth","eight","elite","empty","enemy","enjoy","enter","entry","equal","error","event","every","exact","exist","extra","faith","false","fault","fiber","field","fifth","fifty","fight","final","first","fixed","flash","fleet","focus","force","forum","found","frame","fresh","front","fruit","fully","funny","giant","given","glass","globe","going","grace","grade","grand","grant","grass","great","green","gross","group","guard","guess","guest","guide","habit","happy","harsh","heart","heavy","hence","hobby","honor","horse","hotel","house","human","ideal","image","index","inner","input","issue","joint","judge","known","label","large","laser","later","laugh","layer","learn","lease","least","leave","legal","level","light","limit","local","logic","loose","lower","lucky","lunch","magic","major","match","maybe","media","metal","minor","model","money","month","moral","motor","mount","mouse","mouth","movie","music","needs","never","newly","night","noise","north","novel","nurse","occur","ocean","offer","often","order","other","ought","paint","panel","party","peace","phase","phone","piece","pilot","pitch","place","plain","plane","plant","plate","point","press","price","pride","prime","print","prior","prize","proof","proud","prove","queen","quick","quiet","radio","raise","range","rapid","ratio","reach","ready","refer","right","rival","river","rough","round","route","royal","rural","scale","scene","scope","score","sense","serve","seven","shall","shape","share","sharp","sheet","shelf","shift","shine","shirt","shock","shoot","short","shown","sight","since","sixth","sixty","skill","smart","smile","smoke","solid","solve","sorry","sound","south","space","spare","speak","speed","spend","spent","split","sport","staff","stage","stand","start","state","steam","steel","stick","still","stock","stone","store","storm","story","strip","study","stuff","style","sugar","suite","super","sweet","table","taken","taste","taxes","teach","teeth","thank","their","theme","there","these","thick","thing","think","third","those","three","throw","tight","times","tired","title","today","topic","total","touch","tough","tower","track","trade","train","treat","trend","trial","trust","truth","twice","under","union","unity","upper","upset","urban","usage","usual","value","video","virus","visit","voice","waste","watch","water","wheel","where","which","while","white","whole","whose","woman","world","worry","worse","worst","worth","would","write","wrong","yield","young","abide","abled","acorn","adore","afire","aging","aisle","alarm","alike","aloha","amber","amuse","angel","annoy","antic","anvil","apply","apron","arbor","armor","aroma","ascot","axiom","azure","banjo","barge","basil","batch","beefy","begun","belly","berry","bison","blast","bleed","blend","bliss","blown","bluer","blunt","bonus","boost","booth","brake","brave","briar","bride","brink","broom","buddy","bully","burst","camel","canoe","caper","cargo","carve","cello","chant","chaos","charm","chill","chirp","civic","clamp","clash","climb","cling","clown","cobra","colon","comet","coral","couch","coven","crank","creek","crest","cubic","cumin","curly","dairy","daisy","delta","demon","diary","dizzy","donor","dread","dried","droop","eagle","easel","ember","elope","epoch","erupt","ethic","fable","feast","ferry","fever","filly","fjord","flame","flank","flare","float","flora","flute","foggy","forgo","forty","fuzzy","gamma","gauze","genoa","glyph","gnome","gorge","grove","haste","haunt","hedge","hilly","hippo","humid","icily","irony","ivory","jaunt","jelly","karma","kayak","kneel","knock","koala","latch","lemon","lilac","liver","lodge","lorry","lunar","mango","marsh","medal","mercy","mimic","mirth","moody","mossy","nymph","oasis","olive","omega","opera","otter","ovary","pansy","pearl","pecan","perch","petal","piano","pious","plaza","plume","poppy","pound","quack","quilt","radar","rebel","relic","rhyme","risky","robin","rumor","salsa","satin","scarf","scoff","serum","shady","skull","slant","sleet","slope","slump","sneak","snore","solar","sonic","spine","spore","stain","stalk","sting","swoop","thyme","toast","token","trout","tulip","vigor","vivid","vowel","whale","widen","wiser","woven","zesty"]

hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #seond letter
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        #third
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #forth
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #fith
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
print(f'The word was "{hidden_word[0]}{hidden_word[1]}{hidden_word[2]}{hidden_word[3]}{hidden_word[4]}"')

