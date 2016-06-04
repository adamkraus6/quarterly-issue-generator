#!/usr/bin/python

# =============================================================================
# This provides functionality for reading the log .csv file into a list! Nice!
# =============================================================================

import csv
import Tkinter as tk
import tkFileDialog
import zipfile
import os
import collections
import datetime
import math


def readcsv():
	Log = collections.namedtuple("Log", ["date", "time", "psa"])
	logs = []

	root = tk.Tk()
	root.withdraw()

	file_path = tkFileDialog.askopenfilename()
	zip_ref = zipfile.ZipFile(file_path, 'r')
	zip_ref.extractall('logs/extracted/')
	zip_ref.close()

	path = 'logs/extracted/' + os.path.splitext(os.path.basename(file_path))[0]+'/'

	for filename in os.listdir(path):
		print(filename)
		if not filename.startswith('.'):
			with open(path+filename) as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					entry = Log(row['date'], row['time'], row['psa'])
					logs.append(entry)
	return logs