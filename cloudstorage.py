import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)    
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BAEJV80nOC284N3dD7kLaulf0Os38ugtv6vHaFHvHT-6iR0EqwZ0AfOS8t6k8H4OwPuU5GZMSWk7LvN-IX07A7EYCGjmvgTjvy_thXF5_xVTg0higpu4jPaqLs-McH2S4Xh0hPk'
    t1 = TransferData(access_token)
    file_from = input("Write the file path which you want to be transfered: ") 
    file_to = input("Enter the file path to transfer in the dropbox: ")
    t1.upload_file(file_from, file_to)
    print("The file was moved successfully.")

main()    