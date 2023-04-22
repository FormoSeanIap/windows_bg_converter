import os
import shutil

def copy_to_desktop(path, new_folder_name='windows_bg_images'):
    os.mkdir(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', new_folder_name))
    new_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', new_folder_name)
    for filename in os.listdir(path):
        shutil.copy(os.path.join(path, filename), new_path)
    return new_path

def convert_to_jpg(path):
    for filename in os.listdir(path):
        if not filename.endswith('.jpg'):
            os.rename(os.path.join(path, filename), os.path.join(path, filename + '.jpg'))

if __name__ == '__main__':
    old_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets')
    new_path = copy_to_desktop(old_path)
    convert_to_jpg(new_path)