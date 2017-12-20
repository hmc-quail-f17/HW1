import quandl
import os
import math
import datetime
from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
import bokeh as bk
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
quandl.ApiConfig.api_key = "48ko5SjBusis3HgfdzoF"
pd.options.mode.chained_assignment = None  # default='warn'