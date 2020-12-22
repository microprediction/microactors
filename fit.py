from microprediction import MicroWriter
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import random 
import time
import warnings
warnings.filterwarnings('ignore')
from copulas.multivariate import GaussianMultivariate
import pandas as pd


# Grab the Github secret 
import os 
WRITE_KEY = os.environ.get('WRITE_KEY')          # <-- You need to add a Github secret
ANIMAL = MicroWriter.animal_from_key(WRITE_KEY)  # <-- Your nom de plume      
REPO = 'https://github.com/microprediction/microactors/blob/master/fit.py' # <--- Change your username
print('This is '+ANIMAL+' firing up')

STOP_LOSS = 25 # <--- Governs when we give up on a stream/horizon

# Get historical data, fit a copula, and submit 

def fit_and_sample(lagged_zvalues:[[float]],num:int, copula=None):
    """ Example of creating a "sample" of future values
    
           lagged_zvalues:     [ [z1,z2,z3] ]  distributed N(0,1) margins, roughly
           copula :            Something from https://pypi.org/project/copulas/
           returns:            [ [z1, z2, z3] ]  representative sample

        Swap out this function for whatever you like. 
    """
    # Remark 1: It's lazy to just sample synthetic data
    # Remark 2: Any multivariate density estimation could go here. 
    # Remark 3: If you prefer uniform margin, use mw.get_lagged_copulas(name=name, count= 5000) 
    #
    # See https://www.microprediction.com/blog/lottery for discussion of this "game" 
    
    df = pd.DataFrame(data=lagged_zvalues)
    if copula is None:
        copula = GaussianMultivariate() # <--- 
    copula.fit(df)
    synthetic = copula.sample(num)
    return synthetic.values.tolist()


if __name__ == "__main__":
    mw = MicroWriter(write_key=WRITE_KEY)
    mw.set_repository(REPO) # Just polite, creates a CODE badge on the leaderboard
    
    NAMES = [ n for n in mw.get_stream_names() if 'z2~' in n or 'z3~' in n ]
    for _ in range(1):       
        name = random.choice(NAMES)
        lagged_zvalues = mw.get_lagged_zvalues(name=name, count= 5000)
        if len(lagged_zvalues)>20:
            zvalues = fit_and_sample(lagged_zvalues=lagged_zvalues, num=mw.num_predictions)
            pprint((name, delay))
            try:
                for delay in mw.DELAYS:
                    res = mw.submit_zvalues(name=name, zvalues=zvalues, delay=delay )
                pprint(res)
            except Exception as e:
                print(e)
    # Quit some stream/horizon combinations where we fare poorly
    mw.cancel_worst_active(stop_loss=STOP_LOSS, num=3)
