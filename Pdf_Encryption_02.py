
"""take one input file using tkinter and read that pdf file and convert that into a encrypted file
and store that file data in to a csv file """
# import PyPDF2
# import tkinter
# from tkinter import filedialog, messagebox
# import os
# import csv
# from datetime import datetime
#
#
# class PdfEncryption:
#
#     def getfile(self): #get a file  from directory it shows one dialog box in that we select one file usingtkinter"""
#         # file_name = open("one.pdf", 'rb')
#         root = tkinter.Tk()     #given root to a tkinter"""
#         root.withdraw()
#         file_name = filedialog.askopenfilename() # ask to open file in that directory
#         return file_name  # it returns A file which you are selected
#
#
#     def encryption(self):
#         input_file = self.getfile() # whatever you given the file it will converted to encrption form
#         # pdf_folder = r"C:\Users\91897\Desktop\Corporate_Trainings\BBI\PDF_File_Encryption"
#         pdf_in_file = open(input_file, 'rb')# open that file in the file directory and store it in a pdf_in_file
#         input_pdf = PyPDF2.PdfFileReader(pdf_in_file)# read that file and store it in a input_pdf
#         pages_no = input_pdf.numPages# and after storing it read all the pages in the pdf and give number
#         output = PyPDF2.PdfFileWriter()# using this pdffilewriter write that and store it in a output
#
#         for i in range(pages_no):#read the pages in one by one  and store it in a input_pdf
#             input_pdf = PyPDF2.PdfFileReader(pdf_in_file)
#             output.addPage(input_pdf.getPage(i))# it is used to add the page numbers in that pdf output file
#             output.encrypt('admin@123')# and encrypt that file in a admin@123 password
#
#             # with open("simple_password_protected.pdf", "wb") as outputStream:
#         with open("encrypted_one_pdf.pdf", "wb") as outputStream:# it is for open that encrypted
#                                          #file in the name of "encrypted one pdf
#             output.write(outputStream)
#         self.success_msg()# it is for saying that success_msg()
#         pdf_in_file.close()# and close that pdf file
#         return "encrypted_one_pdf.pdf"# return one encrypted file here
#
#     def success_msg(self):# after that if the file is encrypted it shows msg like succ....
#         return messagebox.showwarning("Successful", "File Encryption is successful")
#
#     def getsize(self, file_name):#get the size of a file in that
#         file_size = os.path.getsize(file_name)# it gives path to that file
#         file_size_kb = str(round((file_size/1024), 2))+"kb"
#         return file_size_kb# it returns file size
# #
#     def recordfile(self):#creation of the csv file using record file
#         filename = self.encryption()# name of that file
#         with open("record.csv", "w", newline=None) as file_obj:
#             csv_file_obj = csv.writer(file_obj)
#             csv_file_obj.writerow(["FileName", "TimeStamp", "FileSize"])
#             current_time = datetime.now().replace(microsecond=0) # it is for time stamp
#             time_format = "%Y_%B_%d_%H_%M_%S"
#             modified_time = datetime.strftime(current_time, time_format)
#             lst = []# store all that in this list (file_n,File_size,Time)
#             lst.append(filename)
#             lst.append(modified_time)
#             lst.append(self.getsize(filename))
#             csv_file_obj.writerows([lst])
#         messagebox.showwarning("Record Inserted", "Record Inserted into csv file")


# en = PdfEncryption()# it returns two files that is pdfencrypted and record.csv
# en.recordfile()

"""convert all pdf files into a encrypted and add the time to that """
import os
import PyPDF2
from datetime import datetime
folder=r'C:/Users/Gunnam.Pravallika/PycharmProjects/Assessments of encryption pdf-08-02-22'
files= os.listdir(folder)#list of files which is exist in that above file

for pdf_files in files:
    # print(pdf_files)# it shows all files and folders here\

    if pdf_files.endswith(".pdf"):
        output_file_writer_name=pdf_files.split('.pdf')[0]
          # spliting that pdf files into without extension
        pdf_in_file=open(pdf_files,'rb')
         # open all that pdf filesa

        inputpdf  =PyPDF2.PdfFileReader(pdf_in_file)
        if inputpdf.isEncrypted:
            print("sorry,",pdf_files,"is already Encrypted")
            continue
        page_no=inputpdf.numPages
        output=PyPDF2.PdfFileWriter()

        for i in range(page_no):
            inputpdf=PyPDF2.PdfFileReader(pdf_in_file)
            output.addPage(inputpdf.getPage(i))
            output.encrypt(output_file_writer_name)

        curre_time=datetime.now().replace(microsecond=0)
        new_current_time=datetime.strftime(curre_time,"%Y_%b_%d_%H_%M_%S")
        output_file=output_file_writer_name + new_current_time+".pdf"
        with open(output_file,"wb")as outputStream:
            output.write(outputStream)
        """finding the sizes of the files"""
        file_size=os.path.getsize(output_file)
        print(file_size)
"""code to send a message using smtlib"""
# import smtplib
# mail_content = '''Hello,
#         This is a test mail.
#         In this mail we are sending some attachments.
#         The mail is sent using Python SMTP library.
#         Thank You
#         '''
#         # The mail addresses and password
# sender_address = 'pravallika0533@gmail.com'
# sender_pass = 'Pravallikapapa@123'
# receiver_address = 'vbhaskar441@gmail.com'
#         # Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'hiiiiiii...sended sucessfully'
#         # The subject line
#         # The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# attach_file_name = 'one.pdf'
# attach_file = open( r'C:\Users\Gunnam.Pravallika\PycharmProjects\Assessments of encryption pdf-08-02-22\one.pdf', 'rb')  # Open the file as binary mode
# payload = MIMEBase('application', 'octate-stream')
# payload.set_payload((attach_file).read())
# encoders.encode_base64(payload)  # encode the attachment
#         # add payload header with filename
# payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
# message.attach(payload)
#         # Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
# session.starttls()  # enable security
# session.login(sender_address, sender_pass)  # login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')


# # file_size=os.stat(output_file)
        # print(file_size.st_size)
        #
        # write_file_obj=open(output_file)
        # write_file_obj.seek(0,os.SEEK_END)
        # file_size=write_file_obj.tell()
        # print(file_size)










