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
WRITE_KEY = os.environ.get('WRITE_KEY')      # <-- You need to add a Github secret

ANIMAL = MicroWriter.animal_from_key(WRITE_KEY)       
REPO = 'https://github.com/microprediction/microactors/blob/master/fit.py' # <--- Change your username
print('This is '+ANIMAL+' firing up')

STOP_LOSS = 25 # <--- Governs when we give up on a stream/horizon

# Get historical data, fit a copula, and submit 

def fit_and_sample(lagged_zvalues:[[float]],num:int, copula=None):
    """ Example of fitting a copula function, and sampling
           lagged_zvalues: [ [z1,z2,z3] ]  distributed N(0,1) margins, roughly
           copula : Something from https://pypi.org/project/copulas/
           returns: [ [z1, z2, z3] ]  representative sample

    """
    # This is the part you'll want to change. 
    # Remark 1: It's lazy to just sample synthetic data
    # Some more evenly spaced sampling would be preferable. 
    # Remark 2: Any multivariate density estimation could go here. 
    # Remark 3: If you want to literally fit to a Copula (i.e. roughly uniform margins)
    # then you might want to use mw.get_lagged_copulas(name=name, count= 5000) instead
    #
    # See https://www.microprediction.com/blog/lottery for discussion of why evenly 
    # spaced samples are likely to serve you better. 

    df = pd.DataFrame(data=lagged_zvalues)
    if copula is None:
        copula = GaussianMultivariate() # <--- 
    copula.fit(df)
    synthetic = copula.sample(num)
    return synthetic.values.tolist()


if __name__ == "__main__":
    mw = MicroWriter(write_key=WRITE_KEY)
    mw.set_repository(REPO) # Just polite

    NAMES = [ n for n in mw.get_stream_names() if 'z2~' in n or 'z3~' in n ]
    for _ in range(5):
        name = random.choice(NAMES)
        for delay in [ mw.DELAYS[0], mw.DELAYS[-1]]:
            lagged_zvalues = mw.get_lagged_zvalues(name=name, count= 5000)
            if len(lagged_zvalues)>20:
                zvalues = fit_and_sample(lagged_zvalues=lagged_zvalues, num=mw.num_predictions)
                pprint((name, delay))
                try:
                    res = mw.submit_zvalues(name=name, zvalues=zvalues, delay=delay )
                    pprint(res)
                except Exception as e:
                    print(e)
    # Quit some
    mw.cancel_worst_active(stop_loss=STOP_LOSS, num=3)
