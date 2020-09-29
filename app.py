import test_API
import tally_logic


def main():
    dictionary_test = {"PLAYER1": {"SCORE":0, "POINTS":0, "ID":"Firestabber"}, "PLAYER2": {"SCORE":4, "POINTS":0, "ID": "CaWU"}, "RESETS": 3, "REGION": "US WEST"}
    duel = tally_logic.Duel(dictionary_test)
    duel.player_points()
    duel_info = duel.info

    info = test_API.basic_info

    spread = test_API.get_spreadsheet()
    sheet = spread.spreadsheets()
    data = test_API.get_data(info, sheet)
    curr_names = [r[0] for r in data]

    test_edit_values = []
    test_append_values = []

    for player in ("PLAYER1", "PLAYER2"):
        if ((playerID := (duel_info[player]["ID"])) in curr_names):
            # print(f'Sheet1!A{curr_names.index(playerID)+1}:D')
            # print([[playerID, str(duel_info[player]["SCORE"] + int(data[curr_names.index(playerID)][1])), duel_info["REGION"]]])

            test_edit_values.append( {
                "range": f'Sheet1!A{curr_names.index(playerID)+1}:D',
                "values": [[playerID, str(duel_info[player]["SCORE"] + int(data[curr_names.index(playerID)][1])), duel_info["REGION"]]]
            })
        else:
            test_append_values.append( 
                [duel_info[player]["ID"], duel_info[player]["SCORE"], duel_info["REGION"]]
            )
    
    sheet.values().append(spreadsheetId=info['ID'], range='Sheet1', valueInputOption="USER_ENTERED", body={'values':test_append_values}).execute()
    sheet.values().batchUpdate(spreadsheetId=info['ID'], body={'data':test_edit_values, 'valueInputOption':"USER_ENTERED"}).execute()
        


    

if __name__ == "__main__":
    main()