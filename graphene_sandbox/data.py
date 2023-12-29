database_state = {
    "query_count": 0,
}

people = {
    "Me": {"name": "Me", "best_friend_name": "Bob"},
    "Bob": {"name": "Bob", "best_friend_name": "Me"},
    "Cal": {"name": "Cal", "best_friend_name": "Dee"},
    "Dee": {"name": "Dee", "best_friend_name": "Cal"},
}

friendships = {
    "Me": ["Bob", "Cal"],
    "Bob": ["Me", "Cal"],
    "Cal": ["Me", "Dee"],
    "Dee": ["Cal", "Me"],
}


def get_person(name):
    print(f"get_person({name})")
    database_state["query_count"] += 1
    return people[name]


def get_friends(name):
    print(f"get_friends({name})")
    database_state["query_count"] += 1
    return [people[friend_name] for friend_name in friendships[name]]


def get_query_count():
    return database_state["query_count"]
