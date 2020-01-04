import random

mood_answer_list = [
    ("Because I'm happy", 'dancing'),
    ('I am in love', 'inlove'),
    ('Not understanding anything', 'confused'),
    ('Feel like dancing', 'dancing'),
    ('I feel like crying', 'crying'),
    ('Feeling rich!!', 'money'),
    ('Feel like doing nothing', 'bored'),
]

def random_mood(user_msg):
    if 'mood' or 'feelings' in user_msg:
        return random.choices(mood_answer_list)


