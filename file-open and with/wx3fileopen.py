import json
import csv

data = [["ikan","hulu","hala"],
            ["xiaohui",22,"x"],
            ["xixixixi",33],"isisi",
            ["hoahaiha",233,"ssaww"]]
try:
	with open("rin2.csv","x",newline="") as file:
		writer = csv.writer(file)
		for row in data:
			writer.writerow(row)
		print(f"file csv sudah dibuat")
except FileExistsError:
		print("that file already exists!")