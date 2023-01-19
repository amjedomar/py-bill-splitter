import random


def main():
    print('Enter the number of friends joining (including you):')
    friends_num = int(input())
    
    if friends_num <= 0:
        return print('No one is joining for the party')

    print('Enter the name of every friend (including you), each on a new line:')
    
    friends = {}
    for i in range(0, friends_num):
        friends[input()] = 0

    print('Enter the total bill value:')
    billAmount = int(input())
    billPerFriend = round(billAmount / len(friends), 2)

    for friend in friends:
        friends[friend] = billPerFriend

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    chosed_lucky_feature = input() == 'Yes'

    if chosed_lucky_feature:
        friends_names = list(friends.keys())
        rand_idx = random.randint(0, len(friends) - 1)
        lucky_friend = friends_names[rand_idx]
        print(f"{lucky_friend} is the lucky one!")
        
        billPerFriend = round(billAmount / (len(friends) - 1), 2)
        for friend in friends:
            friends[friend] = billPerFriend if friend != lucky_friend else 0
    else:
        print('No one is going to be lucky')

    print(friends)


main()
