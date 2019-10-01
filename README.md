UPDATE 01/10/2019:
  - Performed some little modifications to the main file of the package 


#This is a little SRS application really easy to use. Its goal is help you to study and remember a large amount of words. It's free and open source.

#You can set it via python console or through the __main__ file, maybe to set a list of instructions the application will have to do nextly. 

#The only parameter the class constructor requires is a text file where to save the data.
#It's highly recommended NOT to modify this file by manually, because you could then get unexpected errors.
#However, in case you want to modify it, please make sure to respect the correct format.

#Now, it's going to follow a list of all present methods in the class:
# 1 - insert(deck, topic) -- it allows you to insert a new deck. It returns void
# 2 - add(deck, front, back) -- it allows you to add a new card. It returns void
# 3 - remove(deck, front) -- it allows you to remove a card. It returns void
# 4 - delete(deck) -- it allows you to delete an entire deck. It returns void
# 5 - get(deck) -> List[str] -- it allows you to get a deck. It returns a list of strings.
# 6 - start(topic) -- it allows you to start the SRS session. It returns void
# 7 - __update -- it's need to correctly write the data on the file. **

#**IMPORTANT: THIS METHODS ARE STRONGLY PRIVATE AND SHOULD NEVER BE USED BY USERS
