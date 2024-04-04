# Data_sci_project
Overview:

This project analyzes the impact of review scores on listing prices using Python. It includes data manipulation, visualization, and linear regression modeling to investigate the relationship between review scores and prices.

Dependencies:
Ensure you have the following Python libraries installed:

pandas
numpy
matplotlib
seaborn
scikit-learn
You can install them using pip: pip install pandas numpy matplotlib seaborn scikit-learn

Data Source:
The data is accessed online. go to this website https://www.kaggle.com/datasets/mrnabiz/detailed-airbnb-listing-data-london-sep-2022/data. Then download the data set and change the file variable to match the path of the download on your device

Running the Code:
Open the Jupyter Notebook file (project.ipynb) in Jupyter Notebook or JupyterLab.
Execute the code cells one by one. Ensure you have an internet connection to access the data online.
For generating graphs, note that a popup window will appear for each graph. Take a screenshot of each graph and close the popup window to allow the code to continue executing.

Expected Output:
Summary statistics such as mean, median, standard deviation, variance, min, max, and quartiles.
Visualizations including box plots, scatter plots, and histograms.
Linear regression model results including coefficients, mean squared error, and R-squared value.

Troubleshooting:
If you encounter any issues make sure all required libraries are installed by running:
python3 -m pip check
Manually configure the interactive backend for matplotlib if needed. Ensure pyqt5 and pyside2 are installed.
Use command pip list to check if the libraries are installed correctly.
