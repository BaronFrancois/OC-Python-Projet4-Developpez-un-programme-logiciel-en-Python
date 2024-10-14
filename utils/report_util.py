class ReportUtil:
    # 
    @staticmethod
    # Back up save when exiting the program
    def save_resume_file(data):
        # Assurer que le répertoire existe
        os.makedirs("resources", exist_ok=True)
        with open("resources/resume_file.json", "w") as file:
            json.dump(data, file, indent=4)