class RoundView:
    @staticmethod
    def ask_match_result(player1, player2):
        while True:
            # Prompt the user for the match result
            print("")
            print(player1.first_name,"///VS///" ,player2.first_name)
            print(f'press 1 {player1.first_name} won the match ')
            print(f'press 2 {player2.first_name} won the match ')
            print('press 3 for draw')
            ask_result = int(input("Choose match winner :"))
            if ask_result == 1 or ask_result == 2 :
                break
            elif ask_result != 3:
                print("please enter a valid option:")
            elif ask_result == 3:
                print("match is draw, the players are playing again.")
        
        return ask_result

    @staticmethod
    def show_round_details(round):
        print("---------------------------")
        print("Round Name       :",round.rnd_name)
        print("Round Start Date :",round.rnd_start_datetime)
        print("Round End Date   :",round.rnd_end_datetime)
        # print("")