
from django_cron import CronJobBase, Schedule
from django.core.management import call_command


class saveDump(CronJobBase):
    RUN_EVERY_MINS = 4
    RUN_AT_TIMES = ['4:34']
    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=RUN_EVERY_MINS)
    code = 'itscoolweb.saveDump'
    def do(self):
        file_json = open('outjson.json', 'w')
        call_command('dumpdata', format='json', indent=3, stdout=file_json)
        file_json.close()

        file_xml = open('outxml.xml', 'w')
        call_command('dumpdata', format='xml', indent=3, stdout=file_xml)
        file_xml.close()

        call_command(
            'pg_dump --dbname=config("postgres") —file=”output.sql” —username= config("postgres") –-password= config("123456789"), —host= config("localhost") —port=''')
