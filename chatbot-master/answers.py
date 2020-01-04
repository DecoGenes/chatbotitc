import random
import name
import mood
import jokes


curse_dictonary = ['fuck', 'shit', 'asshole']
greetings_animation_list = ['excited', 'ok']
greetings_list = ['hello', 'hi', 'hey', 'sup', 'how are you']
greetings_answer_list = ['Hello there, how are you?', 'Hi', 'What is up?']
moods = ['mood', 'feeling']
jokes_list_words = ['joke', 'jokes']
city_list = ['Recife', 'Tel Aviv', 'New York', 'Berlin', 'Joao Pessoa', 'New Jersey', 'Givataiym']


def answer_from_input(user_input):
    user_msg = user_input.lower().split()
    print(user_msg)
    if any(i in curse_dictonary for i in user_msg):
        return {"animation": "no", "msg": "Don't talk like this. It is not nice!"}
    elif 'name' in user_msg and len(user_msg) > 1:
        return {"animation": "excited", "msg": f'Hi {name.get_name(user_msg)}, nice to meet you!'}
    elif any(i in moods for i in user_msg):
        use_mood = mood.random_mood(user_msg)
        return {"animation": use_mood[0][1], "msg": use_mood[0][0]}
    elif any(i in jokes_list_words for i in user_msg):
        return jokes.random_jokes(user_msg)
    if any(i in greetings_list for i in user_msg):
        print(user_msg)
        return {"animation": random.choices(greetings_animation_list), "msg": random.choices(greetings_answer_list)}
    elif 'animal' in user_msg:
        return {"animation": "dog", "msg": 'Dogs, Dogs, Dogs!!!!'}
    elif 'travel' in user_msg:
        return {"animation": "takeoff", "msg": f'I would love to visit {random.choices(city_list)[0]}'}
    else:
        return {"animation": "heartbroke", "msg": '''Didn't understand what you said.'''}


print(answer_from_input('tell me a joke'))
