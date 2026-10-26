import csv

def the_reader(path):
    rows=[]
    with open (path) as f:
     for row in csv.DictReader(f):
          row["co2_in"]=float(row["co2_in"])
          row["co2_out"]=float(row["co2_out"])
          rows.append(row)
        
    return(rows)


if __name__ == "__main__":

 print(the_reader("readings.csv"))
 print(len(the_reader("readings.csv")))