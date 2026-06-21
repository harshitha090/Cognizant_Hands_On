class Report:
    def generate(self):
        print("Generating Report")

class ReportSaver:
    def save(self):
        print("Saving Report")

report = Report()
saver = ReportSaver()

report.generate()
saver.save()