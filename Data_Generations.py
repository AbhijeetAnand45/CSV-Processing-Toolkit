import csv
import random
import string

def generate_unique_rows(num_rows):
    # Generate unique rows
    unique_rows = []
    for sno in range(1, num_rows + 1):
        alarmid = ''.join(random.choices('0123456789', k=6))
        alarmname = random.choice(['Any Solar MPPT Module Common Fault','Battery Fuse Fail', 'DC Low', 'Device Not Reachable', 'DG Common Fault', 'DG Fail to start', 'DG in Manual', 'DG Low Fuel Level Trip', 'Load MCB trip',
                                   'Load on Battery', 'Site On Battery Gt 1Hr', 'SPD Fail', 'Site SOC Low'])
        alarmstate = random.choice(['CLEAR', 'RAISED'])
        preceivedseverity = random.choice(['CRITICAL', 'MAJOR', 'MINOR'])
        area = random.choice(['Ghansoli', 'Rabale', 'Vashi', 'Thane', 'Nerul', 'Dadar', 'Mulund', 'Ghatkopar', 'Colaba', 'Juhu', 'Bandra', 'Versova', 'Malad', 'Borivali', 'Goregaon'])
        latitude = round(random.uniform(18.0, 19.5), 6)  # Assuming latitude between 18.0 and 19.5
        longitude = round(random.uniform(72.0, 73.5), 6)  # Assuming longitude between 72.0 and 73.5
        sapid = 'I-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        ciname = 'IN' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=26))
        unique_rows.append([sno, alarmid, alarmname, alarmstate, preceivedseverity, area, latitude, longitude, sapid, ciname])
    return unique_rows

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["SNo", "AlarmID", "AlarmName", "AlarmState", "PreceivedSeverity", "Area", "Latitude", "Longitude", "SAPID", "CINAME"]) # Header
        writer.writerows(data)

if __name__ == "__main__":
    num_rows = 100000
    output_filename = "alarm_data.csv"
    unique_rows = generate_unique_rows(num_rows)
    write_to_csv(unique_rows, output_filename)
    print(f"{num_rows} unique rows generated and saved to '{output_filename}'.")
