from chains.All_chains import explanation_chain

difficulty_options = {
    "1": "Beginner",
    "2": "Intermediate",
    "3": "Advanced"
}

language_options = {
    "1": "English",
    "2": "Roman Urdu",
    "3": "Simple English"
}
doc_type = {
    "1": "Explain Topic",
    "2": "Generate Notes",
    "3": "Generate MCQs",
    "4": "Exit"
}

print("\nSelect Language:")
print("1. Explaination")
print("2. Quiz")
print("3. notes")
print('4. exit')
topic = input('Please enter your topic : ')
output_type = input('Select what you want : ')

print("\nSelect Difficulty:")
print("1. Beginner")
print("2. Intermediate")
print("3. Advanced")

difficulty_choice = input("Select difficulty: ")


print("\nSelect Language:")
print("1. English")
print("2. Roman Urdu")
print("3. Simple English")

language_choice = input("Select language: ")



difficulty = difficulty_options.get(difficulty_choice)
language = language_options.get(language_choice)
type = doc_type.get(output_type)

if difficulty is None or language is None or type is None:
    print("\nInvalid selection!")
else:
    print("\nSelected Options:")
    print('Topic : ',topic)
    print("Difficulty:", difficulty)
    print("Language:", language)
    print("output type : ",type)
output =   explanation_chain.invoke({
        "topic": topic,
        "difficulty":difficulty,
        "language": language,
    })
print(output)