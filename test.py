import csv

def read_hostnames_from_csv(file_path):
    hostnames = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            hostnames.append(row['Hostname'])
    return hostnames

# Example usage
file_path = '/home/dgomez/Documents/Repositories/python/inventory.csv'  # Replace with your CSV file path
hostnames = read_hostnames_from_csv(file_path)
print("List of servers to connect to:")
for hostname in hostnames:
    print(hostname)





