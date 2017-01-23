from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.contrib import admin
from home.models import Company
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        file_list = ['nyse.csv', 'nasdaq.csv', 'amex.csv']
        csv_filepathname='company information/all_companies.csv'
        dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
        for row in dataReader:
            ticker = row[0]
            name = row[1]
            exchange = row[2]
            try:
                l = Company.objects.get_or_create(ticker=ticker, name=name, exchange=exchange)
                print (ticker)
                l[0].save()
            except:
                pass
