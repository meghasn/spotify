import pickle as pkl
import pandas as pd
import os
for filename in os.listdir("./pkl files"):
    with open("./pkl files/" + filename, "rb") as f:
        object = pkl.load(f)
    
    df = pd.DataFrame(object)
    df.to_csv("./csv files/"+filename+'.csv')