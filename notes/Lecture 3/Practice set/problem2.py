# Problem 2 : Write a program to fill in a letter template given below with name and date 

letter = ''' Dear <|Name|>,
             You are selected!
              <|date|> 
              Congrats '''

# letter.replace("<|Name|>","Yash")
# letter.replace("<|date|>" , "27/02/2026")

print(letter.replace("<|Name|>","Yash").replace("<|date|>" , "27/02/2026")) #chaining of the string functions  

  