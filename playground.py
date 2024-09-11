
import app.services.portfolio as portfolio


print("Running...")
data = portfolio.download_data(["AAPL", "GOOGL", "MSFT", "AMZN", "META"])
print("data:" , data)

print("Done")
