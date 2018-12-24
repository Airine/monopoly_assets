from player.CsPlayer import CsPlayer
from player.EePlayer import EePlayer
from player.FnPlayer import FnPlayer
from player.MaPlayer import MaPlayer


class PlayerFactory:
    """玩家工厂，输入type制造不同的人物"""

    @staticmethod
    def create_player(player_id, room_id, name, seat, player_type):
        player = None
        if player_type == 0:
            player = FnPlayer(player_id, room_id, name, seat)
        elif player_type == 1:
            player = CsPlayer(player_id, room_id, name, seat)
        elif player_type == 2:
            player = EePlayer(player_id, room_id, name, seat)
        elif player_type == 3:
            player = MaPlayer(player_id, room_id, name, seat)

        return player


if __name__ == '__main__':
    cs_player = PlayerFactory.create_player(1, 1234, "唐博", None, 1)
    print(cs_player)
