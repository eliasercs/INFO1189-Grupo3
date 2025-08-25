from datetime import datetime

class ReportLoader:
    def load(self):
        return {"ventas": 1200, "fecha": str(datetime.now())}

class ReportFormatter:
    def format(self, data):
        return f"REPORTE: ventas={data['ventas']} fecha={data['fecha']}"

class ReportPersister:
    def save(self, text, filename="reporte.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

class ReportPresenter:
    def present(self, text):
        print(text)

class ReportService:
    def __init__(self, loader, formatter, persister, presenter):
        self.loader = loader
        self.formatter = formatter
        self.persister = persister
        self.presenter = presenter

    def run(self):
        data = self.loader.load()
        text = self.formatter.format(data)
        self.persister.save(text)
        self.presenter.present(text)

if __name__ == "__main__":
    service = ReportService(
        loader=ReportLoader(),
        formatter=ReportFormatter(),
        persister=ReportPersister(),
        presenter=ReportPresenter()
    )
    service.run()
