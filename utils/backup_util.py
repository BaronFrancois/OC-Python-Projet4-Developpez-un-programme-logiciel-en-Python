import os
import json


class Backup:
    @staticmethod   
    def pause(option_number,details,tournament):
        details["option_number"] = option_number
        if tournament:
            details["tournament"] = tournament.name
        Backup.save(details)
        
    @staticmethod     
    def save(data):
        # Assurer que le répertoire existe
        os.makedirs("resources", exist_ok=True)
        with open("resources/resume_file.json", "w") as file:
            json.dump(data, file, indent=4) 