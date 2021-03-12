name = ""

question = ""
answer = ""

import random
random_Number = random.randint(1,9)

if question == "" or question == " ":
  print("please input a question")
else:
  if name == "" or name == " ":
    print("you ask:  " + "\"" + question + "\"")
  else:
    print(name,"asks:  " + "\"" + question + "\"")

  if random_Number == 1:
    answer = "Yes definetly"
  elif random_Number == 2:
    answer="It is decidedly so"
  elif random_Number == 3:
    answer="Without a doubt"
  elif random_Number == 4:
    answer="Reply hazy, try again"
  elif random_Number == 5:
    answer="Ask again later"
  elif random_Number == 6:
    answer="Better not tell you now"
  elif random_Number == 7:
    answer="My sources say no"
  elif random_Number == 8:
    answer="Outlook not so good"
  else:
    answer="Very doubtful"
  print("my sources say that:",answer)
