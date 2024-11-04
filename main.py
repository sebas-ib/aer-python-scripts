import csv
import pandas as pd

# Input and output file names
# Hardcoded for now, can be changed later
input_file = 'rc_0.log'
output_file = 'rc_0.csv'

def parse_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Separate the header and data
    header = []
    data_rows = []
    reading_header = True

    for line in lines:
        # Clean up line and skip empty lines
        clean_line = line.strip()
        if not clean_line:
            continue

        if reading_header:
            # Read the header until data is encountered
            if clean_line.startswith('"'):
                # Extract fields from header
                header_fields = clean_line.split(',')
                for field in header_fields:
                    # Split by | and take the first element (parameter name)
                    param_info = field.split('|')
                    if len(param_info) > 0:
                        header.append(param_info[0].strip('"') + ' (' + param_info[1].strip('"') + ')')

            else:
                # Switch to reading data after the first data line is detected
                reading_header = False

        if not reading_header:
            # Read data lines
            data_rows.append(clean_line.split(','))

    return header, data_rows

def write_to_csv(header, data_rows, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(header)

        # Write data rows
        for row in data_rows:
            writer.writerow(row)

if __name__ == '__main__':
    header, data_rows = parse_data(input_file)
    write_to_csv(header, data_rows, output_file)
    print(f"Data has been parsed and written to {output_file}.")
