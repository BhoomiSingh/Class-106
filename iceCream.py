import csv
import plotly.express as px
import numpy as np

def getDataSource(data_Path):
    iceCream_sales=[]
    coldDrink_sales=[]
    with open("IceCream.csv") as f:
        df = csv.DictReader(f)
        for row in df:
            iceCream_sales.append(float(row['Temperature']))
            coldDrink_sales.append(float(row['Ice-cream Sales( â‚¹ )']))
    return{"x: iceCreame_sales", "y: coldDrink_sales"}

def findCorrelation(data_source):
    correlation= np.corrcoef(data_source["x"],data_source["y"])
    print("Corelation between Ice-Cream and Cold Drink", correlation[0,1])

def setup():
    data_Path="IceCream.csv"
    data_source=getDataSource(data_Path)
    findCorrelation(data_source)
setup()
