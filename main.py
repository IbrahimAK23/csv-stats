from csvstats.reader import the_reader
from csvstats.calc import stats

if __name__ == "__main__":

 rows =the_reader("readings.csv")
 co2_values=[row["co2_in"] for row in rows]
 print(co2_values)

 calc2=stats(co2_values)

 print(calc2.mean())
 print(calc2.max())
 print(calc2.min())
 print(calc2.count())

 print(f"co2_in : count {calc2.count()} , mean {calc2.mean()} max {calc2.max()} ,min {calc2.min()}")