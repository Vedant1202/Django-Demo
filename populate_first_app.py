import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

#Setup the Configuration
import django
django.setup()

#============================================================
                    # FAKER DATA POPULATION SCRIPT
#============================================================


import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fake_data_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


#======================================================================

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()

    return t

#======================================================================

def populate_data(N=len(topics)):

    for entry in range(N):
        #Get the topic for the entry
        top = add_topic()

        #Create the fake data for that entry
        fake_url = fake_data_gen.url()
        fake_date = fake_data_gen.date()
        fake_name = fake_data_gen.company()

        #Create a new Webpage entry
        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #Create a fake AccessRecord for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

#=====================================================================

if __name__ == '__main__':
    print("Faker is populating the Db!")
    populate_data(50)
    print("Successfully populated the Db!")
