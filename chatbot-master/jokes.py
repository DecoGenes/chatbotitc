import random

jokes_animation_list = ['giggling', 'laughing']

list_of_jokes = (
    '''Doctor: "I'm sorry but you suffer from a terminal illness and have only 10 to live."

    Patient: "What do you mean, 10? 10 what? Months? Weeks?!"
    
    Doctor: "Nine."''',
    '''My old aunts would come and tease me at weddings, “Well Sarah? Do you think you’ll be next?”
    We’ve settled this quickly once I’ve started doing the same to them at funerals.''',

    '''An old grandma brings a bus driver a bag of peanuts every day.

    First the bus driver enjoyed the peanuts but after a week of eating them he asked: "Please granny, don't bring me peanuts anymore. Have them yourself.".
    
    The granny answers: "You know, I don't have teeth anymore. I just prefer to suck the chocolate around them."''',

    '''I got another letter from this lawyer today. It said “Final Notice”. Good that he will not bother me anymore.''',

    '''I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.''',

    '''One company owner asks another: “Tell me, Bill, how come your employees are always on time in the mornings?”

    Bill replies: “Easy. 30 employees and 20 parking spaces.”''',
)


def random_jokes(user_msg):
    if 'joke' or 'jokes' in user_msg:
        return {"animation": random.choices(jokes_animation_list), "msg": random.choices(list_of_jokes)}
