import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Telemetry data repository
infrastructure_data = {
    'Model_Name': ['LLM_Llama', 'Vision_ResNet', 'LLM_Llama', 'BERT_Text', 'Vision_ResNet', 'Tabular_XGB', 'LLM_Llama', 'BERT_Text'],
    'Inference_Time_ms': [120.5, 45.2, np.nan, 85.0, 42.1, 15.8, 115.3, 90.2],
    'Energy_Cost_Watts': [250.0, 90.0, 260.0, np.nan, 85.0, 30.0, 245.0, 110.0],
    'Server_Status': ['Optimal', 'Optimal', 'Overloaded', 'Optimal', np.nan, 'Optimal', 'Optimal', 'Optimal']
}

class InfrastructureAnalyzer:
    def __init__(self, data):
        """
        Initializes the analyzer by converting the raw data dictionary into a Pandas DataFrame.
        """
        self.df = pd.DataFrame(data)

    def clean_telemetry(self):
        """
        Handles missing telemetry values using standard vector reassignment.
        Imputes inference time with the mean, energy cost with the median,
        and drops rows with missing status identifiers.
        """
        self.df = self.df.fillna({'Inference_Time_ms': self.df['Inference_Time_ms'].mean()})
        self.df = self.df.fillna({'Energy_Cost_Watts': self.df['Energy_Cost_Watts'].median()})
        self.df = self.df.dropna(subset=['Server_Status'])
    
    def generate_dashboard(self):
        """
        Generates a 1x2 Matplotlib subplot performance dashboard.
        - Left: Bar chart comparing mean inference times per model.
        - Right: Histogram displaying the distribution of energy consumption.
        """
        # Compute group aggregations for the bar chart
        inference_time_model = self.df.groupby('Model_Name')['Inference_Time_ms'].mean()
        
        # Initialize the figure workspace with explicit dimension tuning
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
        
        # Subplot 1: Bar Chart Configuration
        ax1.bar(inference_time_model.index, inference_time_model.values, color='salmon')
        ax1.set_xlabel('Model Name')
        ax1.set_ylabel('Inference Time (ms)')
        ax1.set_title('Inference Time Comparison')

        # Subplot 2: Histogram Configuration
        ax2.hist(self.df['Energy_Cost_Watts'], bins=4, color='purple')
        ax2.set_xlabel('Energy Cost (Watts)')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Energy Consumption Distribution')

        # Optimize axis positioning and render the output window
        plt.tight_layout()
        plt.show()

# --- Entry Point ---
if __name__ == "__main__":
    # Instantiate the monitoring pipeline with the infrastructure dataset
    dashboard_analyzer = InfrastructureAnalyzer(infrastructure_data)
    
    # Execute preprocessing and visualization routines
    dashboard_analyzer.clean_telemetry()
    dashboard_analyzer.generate_dashboard()