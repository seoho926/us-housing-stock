
# American Housing Stock
Classifying Adequacy of Units Based on Neighborhood Characteristics

Contributors:
 - 
* Seoho Hahm (@seoho926)
* Nicole Bills (@NicoleJaneway)

Goal:
 - 
The goal of this analysis is to assist U.S. Department of Housing and Urban Development (HUD) to better understand the adequacy of housing units based on neighborhood characteristics.
 
Methods Used:
 -
* Supervised Machine Learning:
  * Logistic Regression
  * Random Forest Classification
  * Support Vector Classification

Data Source:
 -
  1. To set up the data for this project, download the AHS 2017 National survey data <a href='http://www2.census.gov/programs-surveys/ahs/2017/AHS%202017%20National%20PUF%20v3.0%20CSV.zip?#'>here</a>
  2. Move the 'household.csv' into the data folder within this repo
  3. From the home directory of this repo, import 'get_data.py' and run create_dataset function to limit survey data to features related to the neighborhood plus the target feature (ADEQUACY)
  4. Use export_dataset function from the home directory of this repo to export cleaned dataset to data folder
 
Summary and Links to Files:
 - 
 - <a href='https://github.com/seoho926/us-housing-stock/blob/master/US_housing_stock.pdf'>Slide Deck (pdf)</a>
 - <a href='http://www2.census.gov/programs-surveys/ahs/2017/AHS%202017%20National%20PUF%20v3.0%20CSV.zip?#'>Data Source</a>
 - <a href = 'https://github.com/seoho926/us-housing-stock/tree/master/notebooks'>Notebooks</a>
    - <a href = 'https://github.com/seoho926/us-housing-stock/blob/master/technical_notebook.ipynb'>Technical Notebook</a>
 - <a href='https://github.com/seoho926/us-housing-stock/tree/master/py_files'>Python files</a>
