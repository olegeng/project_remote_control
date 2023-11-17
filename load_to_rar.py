import shutil, os
    print(os.path.dirname(__file__))
    directory_to_zip = f'{os.path.dirname(__file__)}/send_to_user'
    zip_file_path = f'{os.path.dirname(__file__)}/zipka.zip'

    shutil.make_archive(zip_file_path.split('.zip')[0], 'zip', directory_to_zip)
    print('ZIP was made!')