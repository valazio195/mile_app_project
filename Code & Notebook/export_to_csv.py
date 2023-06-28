import csv
from itertools import zip_longest

class Save_To_CSV:

    def __init__(self, file):
        self.file = file
    

    def save(self, first_element, second_element, third_element, fourth_element, fifth_element, enam, tujuh, lapan, sembilan, sepuluh, sebelas, duabelas, tigabelas, empatbelas, limabelas, enambelas, tujuhbelas, lapanbelas):
        k = [first_element, second_element, third_element, fourth_element, fifth_element, enam, tujuh, lapan, sembilan, sepuluh, sebelas, duabelas, tigabelas, empatbelas, limabelas, enambelas, tujuhbelas, lapanbelas]
        export = zip_longest(*k, fillvalue='')

        with open('{}'.format(self.file), 'w') as file_csv:
            wb = csv.writer(file_csv)
            wb.writerow(('latitude', 'longitude', 'task_created_time','task_completed_time', 'amount', 'cod_received_status', 'task_assigned_to', 'task_status', 'flow', 'task_id', 'branch_destination', 'task_status_label', 'receiver_city', 'task_detail_status_label', 'task_detail_status', 'weight', 'branch_origin', 'task_status_id'))
            wb.writerows(export)
        file_csv.close()

