from player.CsPlayer import CsPlayer
from player.EePlayer import EePlayer
from player.FnPlayer import FnPlayer
from player.MaPlayer import MaPlayer
from player.Player import Player

class PlayerFactory:
    """玩家工厂，输入type制造不同的人物"""

    @staticmethod
    def create_player(player_id, room_id, name, seat, player_type):
        player = None
        if player_type == 0:
            player = Player(player_id, room_id, name, seat, 'CS')
        elif player_type == 1:
            player = Player(player_id, room_id, name, seat, 'EE')
        elif player_type == 2:
            player = EePlayer(player_id, room_id, name, seat, 'FN')
        elif player_type == 3:
            player = MaPlayer(player_id, room_id, name, seat, 'MA')

        return player


if __name__ == '__main__':
    cs_player = PlayerFactory.create_player(1, 1234, "唐博", None, 1)
    print(cs_player)
