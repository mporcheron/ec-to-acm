# -*- coding: utf-8 -*-

import csv
import sys

from collections import OrderedDict

filename_authors = sys.argv[1]
filename_output = sys.argv[2]

data = []
data.append(['proceedingID', 'event_tracking_number/theirnumber', 'paper_type', 'art_submission_date', 'art_approval_date', 'theTitle', 'prefix', 'first_name', 'middle_name', 'last_name', 'suffix', 'author_sequence_no', 'contact_author', 'ACM_profile_id', 'ACM_client_no', 'orcid', 'email', 'department_school_lab', 'institution/AFFILIATION', 'city', 'state_province', 'country', 'secondary_department_school_lab', 'secondary_institution', 'secondary_city', 'secondary_state_province', 'secondary_country', 'section_title', 'section_seq_no', 'published_article_number', 'start_page', 'end_page', 'article_seq_no'])

with open(filename_authors, 'r') as file_authors:
    csvfile = csv.reader(file_authors)
    header = True

    paper_author_sequence_no = {}
    published_article_number = 0
    article_seq_no = -1
    
    previous_event_tracking_number = None

    # Go through each author
    for row in csvfile:
        if header:
            header = False

        proceeding_id = 'REQUIRED'
        event_tracking_number = row[0]
        paper_type = 'REQUIRED'
        art_submission_date = ''
        art_approval_date = ''
        title = row[1]
        prefix = ''

        split_first_names = row[2].split(' ')
        first_name = row[2]
        middle_name = ''
        if len(split_first_names) < 1:
            print('Something went wrong parsing this name:')
            print(row[2])
            exit()
        elif len(split_first_names) == 2:
            first_name = split_first_names[0]
            middle_name = split_first_names[1]
        elif len(split_first_names) > 2:
            first_name = split_first_names[0]
            middle_name = split_first_names[1:]

        last_name = row[3]
        suffix = ''
        
        if event_tracking_number in paper_author_sequence_no:
            author_sequence_no = paper_author_sequence_no[event_tracking_number]
            paper_author_sequence_no[event_tracking_number] = author_sequence_no + 1
        else:
            author_sequence_no = 1
            paper_author_sequence_no[event_tracking_number] = 2
        
        contact_author = 'yes' if row[7] == '✔' else 'no'
        ACM_profile_id = ''
        ACM_client_no = ''
        orcid = ''
        email = row[4]
        
        if ', ' in row[5]:
            institution_split = row[5].split(', ')
            department_school_lab = institution_split[0]
            institution = ', '.join(institution_split[1:])
        else:
            department_school_lab = ''
            institution = row[5]
            
        city = ''
        state_province = ''
        country = row[6]
        secondary_department_school_lab = ''
        secondary_institution = ''
        secondary_city = ''
        secondary_state_province = ''
        secondary_country = ''
        section_title = ''
        section_seq_no = ''
        start_page = ''
        end_page = ''
        
        if event_tracking_number != previous_event_tracking_number:
            published_article_number += 1
            article_seq_no += 1
            previous_event_tracking_number = event_tracking_number
        else:
            previous_event_tracking_number = event_tracking_number
        
        data.append([
            proceeding_id,
            event_tracking_number,
            paper_type,
            art_submission_date,
            art_approval_date,
            title,
            prefix,
            first_name,
            middle_name,
            last_name,
            suffix,
            author_sequence_no,
            contact_author,
            ACM_profile_id,
            ACM_client_no,
            orcid,
            email,
            department_school_lab,
            institution,
            city,
            state_province,
            country,
            secondary_department_school_lab,
            secondary_institution,
            secondary_city,
            secondary_state_province,
            secondary_country,
            section_title,
            section_seq_no,
            published_article_number,
            start_page,
            end_page,
            article_seq_no])
            
with open(filename_output, 'w') as file_output:
    writer = csv.writer(file_output)
    writer.writerows(data)
    