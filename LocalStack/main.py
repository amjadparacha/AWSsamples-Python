# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from S3 import S3Bucket, FileS3Bucket

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    S3Bucket.create_bucket_main()
    FileS3Bucket.upload_file_main()
    FileS3Bucket.download_file_main()
    FileS3Bucket.delete_file_main()
    S3Bucket.delete_bucket_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
