"""
                        School Administration System
                        -----------------------------
"""

# CSV Package
import csv


# Function to open file and append info
def write_into_file(data_list):
    with open("student-data-file.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # First row headers when opening the file
        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Registration-Id', 'Contact Number', 'Email-Id'])

        # Append info
        writer.writerow(data_list)


# Main Block
if __name__ == '__main__':

    # Set up loop for multiple student input
    input_again = True
    student_number = 1

    while (input_again):
        student_info = input("Enter data of #{} student in the form of 'Name Age Registration-Id Contact Number Email-Id' (separated by spaces)\n".format(student_number)).split()

        print("Data Entered :-\nName: {}\nAge: {}\nRegistration-Id: {}\nContact Number: {}\nEmail-Id: {}".format(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4]))

        # Check if proper input was given
        input_check = input("Enter (Y/y) for correct input and (N/n) for wrong input ")
        if input_check in {'Y', 'y'}:
            write_into_file(student_info)

            # Check for another input of student data
            input_check = input("Enter (Y/y) for another student data input and (N/n) to exit ")
            if input_check in {'Y', 'y'}:
                student_number = student_number + 1
            elif input_check in {'N', 'n'}:
                input_again = False

        elif input_check in {'N', 'n'}:
            print("Please re-enter the values!")
