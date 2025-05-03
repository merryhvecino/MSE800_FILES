import pandas as pd
import matplotlib.pyplot as plt

class TempComparison:
    def __init__(self):
        self.auckland = None
        self.christchurch = None
        self.combined = None

    def load_data(self):
        self.auckland = pd.read_csv('ACTIVITY1_WEATHER\auckland_temperature.csv')
        self.auckland['City'] = 'Auckland'

        self.christchurch = pd.read_csv('ACTIVITY1_WEATHER\christchurch_temperature.csv')
        self.christchurch['City'] = 'Christchurch'

        self.combined = pd.concat([self.auckland, self.christchurch])

    def show_plot(self):
        for city in self.combined['City'].unique():
            city_data = self.combined[self.combined['City'] == city]
            plt.plot(city_data['Month'], city_data['Mean Temperature (°C)'], label=city)

        plt.title('Monthly Temperature: Auckland vs Christchurch')
        plt.xlabel('Month')
        plt.ylabel('Mean Temp (°C)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Run the program
comparison = TempComparison()
comparison.load_data()
comparison.show_plot()
