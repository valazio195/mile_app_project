import json
from time import sleep
from export_to_csv import Save_To_CSV


with open('data-sample.json') as f:
    data = json.load(f)


temp = 0

#Nama-nama kolom
lat = []
longi = []

start_time = []
stop_time = []

amount = []
status_cod = []

assign_id = []
status_task = []
flow = []
task_id = []

branch_dest = []
task_status_label = []
receiver_city = []
task_detail_status_label = []
task_detail_status = []
weight = []
branch_origin = []
task_status = []


#Iteration process

for angka in range(0, 8334):

    try:
        latitude = data[angka]['taskLocationDone']['lat']
        lat.append(latitude)

        longitude = data[angka]['taskLocationDone']['lon']
        longi.append(longitude)
    
    except KeyError:
        lat.append(None)
        longi.append(None)


    start = data[angka]['taskCreatedTime']
    start_time.append(start)


    try:
        stop = data[angka]['taskCompletedTime']
        stop_time.append(stop)
    
    except KeyError:
        stop_time.append(None)

    try:
        cash = data[angka]['cod']['amount']
        amount.append(cash)
    
    except KeyError:
        amount.append(None)

    
    try:
        stat = data[angka]['cod']['received']
        status_cod.append(stat)
    
    except KeyError:
        status_cod.append(None)
        
    try:
        iden = data[angka]['taskAssignedTo']
        assign_id.append(iden)
    
    except KeyError:
        assign_id.append(None)

    status = data[angka]['taskStatus']
    status_task.append(status)

    arus = data[angka]['flow']
    flow.append(arus)

    id_task = data[angka]['taskId']
    task_id.append(id_task)




    dest = data[angka]['UserVar']['branch_dest']
    branch_dest.append(dest)

    try:
        label = data[angka]['UserVar']['taskStatusLabel']
        task_status_label.append(label)

    except KeyError:
        task_status_label.append(None)
    
    kota = data[angka]['UserVar']['receiver_city']
    receiver_city.append(kota)

    try:
        detail = data[angka]['UserVar']['taskDetailStatusLabel']
        task_detail_status_label.append(detail)
    
    except KeyError:
        task_detail_status_label.append(None)

    try:
        stat_2 = data[angka]['UserVar']['taskDetailStatus']
        task_detail_status.append(stat_2)
    
    except KeyError:
        task_detail_status.append(None)

    berat = data[angka]['UserVar']['weight']
    weight.append(berat)

    asal = data[angka]['UserVar']['branch_origin']
    branch_origin.append(asal)

    try:
        stat_3 = data[angka]['UserVar']['taskStatus']
        task_status.append(stat_3)
    
    except KeyError:
        task_status.append(None)

    temp += 1
    print('Data sudah jadi {}'.format(temp))


#Saving to CSV format
saving = Save_To_CSV('delivery_sample_data_updated.csv')

saving.save(lat, longi, start_time, stop_time, amount, status_cod, assign_id, status_task, flow, task_id, branch_dest, task_status_label, receiver_city, task_detail_status_label, task_detail_status, weight, branch_origin, task_status)

