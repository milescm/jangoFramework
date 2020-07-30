from django.shortcuts import render
from .models import CsvData






# import numpy as np
# import seaborn as sns
# import pandas as pd 
# import matplotlib.pyplot as plt
# from .models import CsvData

def post_list(request):
    values = list(CsvData.objects.values())
    return render(request, 'readcsv/post_list.html', {'values':values})



