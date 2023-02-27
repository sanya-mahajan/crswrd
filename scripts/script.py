import pandas as pd
from app.models import Ques
import csv

def run():
    with open('scripts/crswrd.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Ques.objects.all().delete()
        Ques.objects.all().delete()

        for row in reader:
            print(row)


            entry = Ques(id=row[0],
                        ans=row[1],
                        direction=row[2])
            entry.save()