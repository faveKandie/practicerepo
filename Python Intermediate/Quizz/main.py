#this is the main file of the project
def process():
	from question_model import Question  #imports module in order of use and accessibilty.
	from data import question_data
	from quiz_brain import QuizBrain

	question_bank = [] #an empty list to store question and corresponding question anser
	for question in question_data: #loops through the elements of the dictionary question_data in the data module using their positional array
		question_text = question["text"]  #the test and answer is from the question_model module. It stores things there.
		question_answer = question["answer"] #the first one accesses the element and the second one the key of the dictionary
		new_question = Question(question_text, question_answer)#calls/access the new dictionary question_bank
		question_bank.append(new_question) #it adds consecutive new_questions(a dictionary of the correct answer)

	quiz = QuizBrain(question_bank) #an object quiz with the methods of a module quiz_brain called QuizBrain holding the question_bank as the argument.

	while quiz.still_has_question():
		quiz.next_question() #loop to run the program from the quiz_brain module created.

process()

fake = False
while not fake:
	ask = input("Is there any other player to play this round so you could compare? yes or no: ")
	print("\n")
	if ask == "yes":
		process()
	else:
		print("\nGame Over")
		fake = True