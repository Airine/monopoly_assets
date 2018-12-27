
def form_ending(player):
    if player.money >= 0 and player.ability >= 90:
        if player.money >= 5000 and player.personality.manage_point >= 10:
            return 0
        elif player.money >= 5000 and player.personality.real_point < 0:
            return 1
        elif player.personality.research_point >= 15:
            return 2
        elif player.personality.art_point >= 15:
            return 3
        elif player.personality.real_point >= 15:
            return 4
        else:
            return 5
    elif player.study_warning+player.administrative_warning>=3:
        return 6
    else:
        return 7
