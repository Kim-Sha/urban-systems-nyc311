from collections import OrderedDict
from matplotlib_venn import venn2, venn3
from tqdm.notebook import tqdm
tqdm.pandas()
import numpy as np
import geopandas as gpd

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

import re
import os
import time

import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

from sodapy import Socrata

import pdb
from IPython import display
from base64 import b64decode