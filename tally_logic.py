
class Duel: 
    ''' 
    Duel is an object that holds a duel. Duels are formatted as such:
    {"PLAYER1": {"SCORE":(0-4), "POINTS":0, "ID":steamID}, "PLAYER2": {"SCORE":(0-4), "POINTS":0, "ID": steamID}, "RESETS": (0-4), "REGION":(US, EU, etc)}
    '''
    def __init__(self, duel_info : dict):# DICT WITH PLAYER STEAM ID AND SCORE
        self.info = duel_info

    def player_points(self):
        players = ["PLAYER1", "PLAYER2"]
        greater_score_player = [p for p in players if self.info[p]["SCORE"] == 4][0]
        lesser_score_player = [p for p in players if self.info[p]["SCORE"] < 4][0]
        if self.info["RESETS"] == 4:
            self.info[greater_score_player]["POINTS"] = 5
            self.info[lesser_score_player]["POINTS"] = 4
        else:
            self.info[greater_score_player]["POINTS"] = 4
            self.info[lesser_score_player]["POINTS"] = self.info[lesser_score_player]["SCORE"]

    def __str__(self):
        return str(self.info)


def tally(duel : Duel, curr_tally : dict):
    '''
    curr_tally represents the google sheets. it would be formatted as such:
        A    |   B
    PlayerID | Points
    PlayerID | Points
    PlayerID | Points

    As currently, curr_tally would look like a dict of the form {playerID: points, playerID: points, playerID: points}
    '''
    try:
        curr_tally[duel.info["PLAYER1"]["ID"]] += duel.info["PLAYER"]["POINTS"]
    except KeyError:
        curr_tally[duel.info["PLAYER1"]["ID"]] = duel.info["PLAYER"]["POINTS"]
    except Exception as e:
        print(e)
    return curr_tally







if __name__=="__main__":
    dictionary_test = {"PLAYER1": {"SCORE":4, "POINTS":0}, "PLAYER2": {"SCORE":(2), "POINTS":0}, "RESETS": 3, "REGION": "EU"}
    duel_test = Duel(dictionary_test)
    duel_test.player_points()
    print(duel_test)