import os
import uuid
import pandas as pd
import numpy as np



def create_events(schedule):
    events=[]
    location = 'NSLS II, Brookhaven National Laboratory, Upton, NY, 11973 USA'

    for i in range(len(schedule)):
        d = schedule.iloc[i]
        start='{}T{}'.format(str(d['Start date'])[:10], d['Start time'])
        end = '{}T{}'.format(str(d['End date'])[:10], d['End time'])
        event = {
          'summary': 'NSLS-II ISS Beamtime GUP {}'.format(d['Proposal']),
          'location': location,
          'description': 'NSLS-II ISS Beamtime GUP {}'.format(d['Proposal']),
          'start': {
            'dateTime': start,
            'timeZone': 'America/New_York',
          },
          'end': {
            'dateTime': end,
            'timeZone': 'America/New_York',
          },
          'attendees': [
            {'email': d['E-mail']}
          ],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60 * 10},
              {'method': 'email', 'minutes': 24 * 60 * 20},
              {'method': 'email', 'minutes': 24 * 60 * 30}
            ],
          },
        }
        print(event)
        events.append(event)

    return(events)

def create_drafts(schedule):
    drafts = []
    for i in range(len(schedule)):
        d = schedule.iloc[i]
        email = d['E-mail']
        start='{} {}'.format(str(d['Start date'])[:10], d['Start time'])
        end = '{} {}'.format(str(d['End date'])[:10], d['End time'])

        message_body = 'Dear {},\n\nThe beamtime at NSLS-II ISS beamline against the GUP {} ' \
                       'in the 2018-2 Cycle has been scheduled for\n\n'\
                       '{} - {}\n\n'.format(d['PI'],d['Proposal'],start,end)

        subject = 'NSLS-II 8-ID ISS 2018-1 Beamtime scheduling notification for GUP {}'.format(d['Proposal'])

        email = '{}, istavitski@bnl.gov, kattenkofer@bnl.gov'.format(d['E-mail'])
        print(d['E-mail'])
        draft = create_message('staff8id@gmail.com', email, subject,message_body)
        drafts.append(draft)

    return drafts

def create_html_drafts(schedule):
    drafts = []
    fid = open('/Users/elistavitski/Running Projects/ISS operations/letter.html', 'r')
    letter = fid.read().replace('\n', '')
    print(letter)
    print(type(letter))

    for i in range(len(schedule)):
        d = schedule.iloc[i]
        email = d['E-mail']
        start='{} {}'.format(str(d['Start date'])[:10], d['Start time'])
        end = '{} {}'.format(str(d['End date'])[:10], d['End time'])
        message_body = letter.format(d['PI'],d['Proposal'],start,end)

        subject = 'NSLS-II 8-ID ISS 2018-2 Beamtime scheduling notification for GUP {}'.format(d['Proposal'])

        email = '{}, istavitski@bnl.gov, kattenkofer@bnl.gov'.format(d['E-mail'])
        print(d['E-mail'])
        draft = create_html_message('staff8id@gmail.com', email, subject,message_body)
        drafts.append(draft)

    return drafts



