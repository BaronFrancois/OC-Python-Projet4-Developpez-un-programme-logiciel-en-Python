class ReportView:
    @staticmethod
    def show_report(report):
        for line in report:
            print(line)

    
    @staticmethod
    def ask_for_report():
        ask_report = input("Do you want to save the report ? y/n :")
        if ask_report.lower() == "y":
            return True
        else:
            return False
        
    