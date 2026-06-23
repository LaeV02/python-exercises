import pandas as pd
import numpy as np

solar_data = {
    'Station_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Country': ['Italy', 'Spain', 'Italy', 'Germany', 'Spain', 'Germany', 'Italy', 'France'],
    'Energy_Generated_kWh': [450.5, np.nan, 380.0, 510.2, 290.5, np.nan, 410.0, 320.8],
    'Maintenance_Cost_EUR': [120.0, 150.0, 95.0, 180.0, np.nan, 130.0, 110.0, 90.0],
    'Status': ['Active', 'Active', 'Under Review', 'Active', 'Active', 'Under Review', np.nan, 'Active'],
    'Panel_Type': ['Monocrystalline', 'Polycrystalline', 'Monocrystalline', 'Thin-Film', 'Polycrystalline', 'Thin-Film', 'Monocrystalline', 'Polycrystalline']
}

class EnergyGridAnalyzer:
    def __init__(self, df_SolarData):
        # Store the incoming DataFrame as an object attribute
        self.df_SolarData = df_SolarData

    def solve_nan(self):
        # Handle missing values 
        self.df_SolarData = self.df_SolarData.fillna({'Energy_Generated_kWh' : self.df_SolarData['Energy_Generated_kWh'].mean()})
        self.df_SolarData = self.df_SolarData.fillna({'Maintenance_Cost_EUR' : self.df_SolarData['Maintenance_Cost_EUR'].median()})
        # Drop rows where the critical 'Status' column is missing
        self.df_SolarData = self.df_SolarData.dropna(subset=['Status'])
        return self.df_SolarData

    def new_colums(self):
        # Feature engineering: compute ROI ratio and high-performance boolean mask
        self.df_SolarData.insert(4, 'ROI_Ratio', self.df_SolarData['Energy_Generated_kWh'] / self.df_SolarData['Maintenance_Cost_EUR'])
        is_top_performer = self.df_SolarData['Energy_Generated_kWh'] > 400
        self.df_SolarData.insert(5, 'Top_Performer', is_top_performer)
        return self.df_SolarData

    def dfPrint(self):
        # 1. Advanced slicing using .loc for row filtering and specific column selection
        best_StationIDs = self.df_SolarData.loc[self.df_SolarData['Top_Performer'] == True, ['Station_ID','ROI_Ratio']]
        print("\n------------------------------------------------\nThe best stations are: ")
        print(best_StationIDs)
        
        # 2. Business aggregations using groupby
        EnergyGenerated_in_Country = self.df_SolarData.groupby('Country')['Energy_Generated_kWh'].sum()
        print("\n------------------------------------------------\nThe energy generated in each country is: ")
        print(EnergyGenerated_in_Country)
        
        MaxCost_panels = self.df_SolarData.groupby('Panel_Type')['Maintenance_Cost_EUR'].max()
        print("\n------------------------------------------------\nThe max maintenance cost is: ")
        print(MaxCost_panels)

# --- Execution ---
if __name__ == "__main__":
    # Convert dictionary to DataFrame and initialize the analyzer object
    raw_df = pd.DataFrame(solar_data)
    analyzer = EnergyGridAnalyzer(raw_df)
    
    # Run the processing pipeline
    analyzer.solve_nan()
    analyzer.new_colums()
    analyzer.dfPrint()