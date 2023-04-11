# Data Scrap Jakarta House Price

This project is focused on scraping data related to the house prices in Jakarta using the website [rumah.trovit.co.id](https://rumah.trovit.co.id/). The data scraped includes different features such as the number of bedrooms, bathrooms, area size, and location.

## Data Description

The dataset comprises 70 observations and 4 variables. The variables in the dataset are as follows:

| Variable Name | Description |
| --- | --- |
| item-title | The title of the house listing |
| item-description | The description of the house |
| item-price | The price of the house in Indonesian Rupiah |
| location | The location of the house |
| item-property item-rooms | The number of bedrooms |
| item-property item-baths | The number of bathrooms |
| item-property item-size	 | The area size of the house in squared meters |

## Pairplot

The pairplot shows the relationship between the numerical variables in the dataset.

![Pairplot](assets\img\pairplot.png)

from the pairplot above the price to be likely had positive correlation againts item size. The exact number correlation can be seen in the correlation section below.

## Displot

The displot shows the distribution of the price variable in the dataset.

![Displot](assets\img\displot.png)

from the displot in the dataset there are more data outside jakarta that webpage give in the search of jakarta house are sell, in the dataset for jakarta house are sell had more data in jakarta timur with price 0 to 1.25 Billion indonesia rupiah. 0 price means that the publisher doesnt give the actual price in the webpage, in jakarta selatan the data more distributed with price 0 to 4 Billion indonesia rupiah and the rest jakarta dictrict has small amount of data so i think it is not clear to say if the data assist the actual value of the district.

## Correlation

The correlation matrix shows the correlation between the numerical variables in the dataset.

![Correlation](web scrap\assets\img\correlation.png)

correlation matrix calculated using pearson method, from the graph we can know that item price has positive correlation between item size, and the item size has positive correlation with total bathroom and the total bathroom has positive correlation item bedrooms. The correlation make sense to say that higher size has higher price, and the higher the size more likely it has more bathroom and bedroom so it make sense if item sice correlated positively to total bathroom and total bedroom. Item bathroom has positive correlation with item total bedrooms, does it means that more bedroom in the house influece the more bathroom within the house? it can be makesense since the more person within the house can more likely that bathroom being used so it needs more bathroom to avoid waiting to enter the bathrooms

Overall, this dataset still has small amount of data since this project only scrape using one domain, this project shows how to scrape data from website using python and play some visualization tools to describe the data within the webpage that you already scrape.