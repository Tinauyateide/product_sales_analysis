# Optimizing Sales Methods to Maximize Revenue for Pens and Printers

## Project Overview
This project aims to support Pens and Printers in optimizing their sales methods to maximize revenue for a new product line. By analyzing the performance of different sales methods, we provide insights and recommendations on which methods to prioritize for higher revenue generation.

## Business Goals
- Determine the effectiveness of each sales method.
- Identify trends in revenue generation over time.
- Define a metric to monitor the impact of different sales methods on revenue.

## Dataset Description
The dataset used for this analysis includes columns representing revenue, `nb_sold` (number of items sold), sales methods, and other relevant fields that provide context for sales performance. Each row in the dataset represents a unique transaction or sales entry.

### Data Validation and Cleaning Steps
Data validation and cleaning steps were performed to ensure accuracy and consistency:
1. **Missing Data Check**: Verified that there are no missing values in the dataset.
2. **Data Consistency**: Checked and corrected data types, column formats, and ensured that revenue and `nb_sold` fields were in numerical formats suitable for analysis.
3. **Outlier Detection**: Identified and assessed potential outliers that could impact revenue analysis, making necessary adjustments to prevent skewed results.
4. **Revenue Column Verification**: Ensured the revenue column is accurate and aligns with the number of items sold and other transaction details.

## Exploratory Data Analysis (EDA)
To gain insights and answer key business questions, we performed the following EDA steps:
1. **Distribution Analysis**: Examined the distributions of revenue and `nb_sold` to understand overall sales trends and common sales quantities.
2. **Correlation Analysis**: Investigated the relationship between revenue and `nb_sold` to determine if a higher number sold consistently results in higher revenue.
3. **Sales Method Comparison**: Compared the average revenue generated by each sales method to identify which methods are most effective.
4. **Time-Series Analysis**: Explored revenue trends over time, identifying any seasonal or time-based patterns in sales.
5. **Customer Segmentation**: Analyzed clusters in customer purchasing behavior based on `nb_sold` and revenue, identifying common sales quantities and popular transaction sizes.

## Key Metrics
To effectively track and assess sales performance, the following metrics were defined:
- **Revenue per Sale**: Measures revenue per item sold, which helps in tracking the impact of pricing and sales volume.
- **Method Effectiveness**: Calculates the average revenue generated by each sales method, allowing us to rank methods by performance.
- **Revenue Growth Rate**: Measures the rate of revenue growth over time, highlighting any increasing or decreasing trends in sales performance.

## Key Findings
1. **Positive Correlation**: There is a general positive correlation between revenue and `nb_sold`, indicating that as more items are sold, revenue tends to increase, albeit with some variability.
2. **Sales Method Performance**: Certain methods, such as "email & call," tend to generate higher revenue compared to others, although they may require more resources.
3. **Trends Over Time**: Revenue trends fluctuate over time, suggesting that certain methods or periods may be more effective for targeting customers.
4. **Customer Clusters**: Data clusters around certain sales quantities, indicating popular purchase sizes and possible areas to target specific customer segments.

## Recommendations
Based on the analysis findings, we recommend focusing on sales methods that balance high revenue generation with efficient resource use. For instance:
- **Prioritize High-Yield Methods**: Methods that generate more revenue, like "email & call," can be prioritized for high-value customers who justify the additional effort.
- **Optimize Low-Cost Methods**: Simpler methods with lower resource demands can be used to reach smaller customers, maximizing reach without significant resource investment.

## How to Run the Code
To replicate this analysis:
1. Clone this repository and navigate to the project directory.
2. Install the necessary packages using:
   ```bash
   pip install -r requirements.txt


## Database Connection
This project uses a PostgreSQL database to store and update data in real-time. Follow these steps to connect:

1. Ensure PostgreSQL is installed and running.
2. Update the database connection settings in the Jupyter notebook:
   - `DATABASE_TYPE`: 'postgresql'
   - `DBAPI`: 'psycopg2'
   - `ENDPOINT`: Set to your database server address (e.g., 'localhost' if local).
   - `USER`: Database username.
   - `PASSWORD`: Database password.
   - `DATABASE`: Name of the database storing sales data.

3. Run the notebook to save cleaned data into the database.

## Power BI Connection
1. Open Power BI Desktop and select **Get Data > PostgreSQL**.
2. Enter your database connection details.
3. Import the `cleaned_sales_data` table.
4. Use **Refresh** to keep data updated in Power BI.

For automated updates, set up a scheduled refresh in Power BI Service.

