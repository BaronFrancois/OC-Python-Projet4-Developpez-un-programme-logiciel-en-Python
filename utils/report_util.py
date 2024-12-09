from views.report_view import ReportView

class Report:
    
    @staticmethod
    def prepare(headers,my_list,file_name):   
            for header in headers:
                headers[header] = Report.find_longest(my_list,attribute = header)
            print(headers)
            report = Report.add_report_headings(headers)
            for x in my_list:
                row = "" 
                for header, spacing in headers.items():
                    if isinstance(x,dict):
                        value = x[header]
                    else:
                        value = getattr(x,header)
                    row += f" | {value:<{spacing}}"
                row += " |"
                report.append(row)
            ReportView.show_report(report)
            save_report = ReportView.ask_for_report()
            if save_report:
                Report.save_report_to_txt(report,file_name = file_name)
    
    @staticmethod        
    def find_longest(my_list,attribute =None):
            def get_attribute_len(x):
                value = None
                if isinstance(x,dict):
                    value = x[attribute]
                else: 
                    value = getattr(x,attribute)
                lenght = len(str(value))
                return lenght
            longest_x = max(my_list,key=get_attribute_len)
            value = None
            if isinstance(longest_x,dict):
                value = longest_x[attribute]
            else:
                value = getattr(longest_x,attribute)
            longest_str = max(len(str(value)),len(attribute))
            return longest_str
    
    @staticmethod    
    def add_report_headings(headers):
            report = []
            row = "" 
            for header, spacing in headers.items():
                header = header.replace("_"," ").title()
                row += f" | {header:<{spacing}}"
            row += " |"
            report.append(row)
            row = ""
            for header, spacing in headers.items():
                row += f" | {"_"*spacing}"
            row += " |"
            report.append(row)
            return report 
    
    @staticmethod    
    def save_report_to_txt(report,file_name):
            with open(f"resources/reports/{file_name}.txt","w") as file:
                for line in report:
                    file.write(line+"\n")
                print("report has been generated")