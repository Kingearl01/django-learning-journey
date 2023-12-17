import csv
import os
import time
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse

from .models import CustomUser

def export_to_csv(request):
    # user = CustomUser.objects.all()
    # with open('userpassword.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    #     writer.writerow(["ID"])
    #     for row in user:
    #         writer.writerow([row.student_id])
    # file_path = "L400_IDs.csv"
    # directory = os.path.abspath(file_path).replace('\\', '/')     
    # with open(directory, 'r', newline="") as f:
    #     reader = csv.reader(f)
    #     with open('L400_default_pwsd.csv', 'w', newline="") as output_file:
    #             writer = csv.writer(output_file)
    #             # writer.writerow(["ID", "password"])
    #             for row in reader:
    #                 password = str(row)
    #                 clean_pswd = password.replace("['",'').replace("']",'').strip()
    #                 writer.writerow([clean_pswd, make_password(clean_pswd)])
    #                 print(clean_pswd)

                    
    # f.close()
    # output_file.close()

    # file_path = "L400_default_pwsd.csv"
    # directory = os.path.abspath(file_path).replace('\\', '/')     
    # with open(directory, 'r', newline="") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #          print(check_password(row[0], row[1]))
    # f.close()
    hasher = 'pbkdf2_sha256$600000$OclvuneRwDkTOXWycl7Sxb$XdCMCtzv5ZXbhQS/NT2XQXfBGQYfrDOGzyPWZAwpZ0c='

    return HttpResponse(check_password('200048402', hasher))

    