import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation





# Load the environment variables from the .env file
#by calling the load_dotenv function
load_dotenv()

alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

#os.environ["ALPACA_API_KEY"] = 'AKFHULJCTRSEOW67JIOQ'
#os.environ["ALPACA_SECRET_KEY"] = 'BSfSsplxXweaqzQSABEpDaXChIVWZKt4pvLtu4ku'

environ_data = os.environ
for data in environ_data:
    print(data)
print(alpaca_api_key)

print(alpaca_secret_key)
