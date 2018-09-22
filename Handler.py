import pandas as pd
from Swings import *
from ElliotAnalyzer import *
import os
import time


FOREX_DATA_PATH = "C:\\Users\\wyatt\\Documents\\ForexData"
GRAPHS_PATH = "C:\\Users\\wyatt\\Documents\\ForexGraphs"
ANALYSIS_SUMMARY_PATH = ".\\"

with open("Pair_Analysis.txt", 'r') as infile:
    pairs_to_analyze = infile.read().splitlines()

outfile = open(ANALYSIS_SUMMARY_PATH + "summary_analysis.txt", 'w')

for pair in pairs_to_analyze:
    pairname, pairtime = pair.split("_")
    forex_name_template = FOREX_DATA_PATH + "\\" + pairname + "\\"
    sg = Swing_Generator(forex_name_template + pair + ".csv", forex_name_template + pair + "_swings.csv")
    if(os.path.isfile(forex_name_template + pair + "_swings.csv")):
        sg.update_swings()
    else:
        sg.generate_swings()

    ea = Elliot_Analyzer(pair, forex_name_template + pair + "_swings.csv", sg.OHLC_data)
    analysis_summary = ea.analyze()
    if analysis_summary != []:
        ea.export_graph(GRAPHS_PATH + "\\" + pair + "_waves.html")
        outfile.write(pair + "\t" + str(analysis_summary) + "\n")

outfile.close()

print("Total Time: ", time.process_time())
