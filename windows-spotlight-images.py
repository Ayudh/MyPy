# script to save windows spotlight images
import os
import shutil
import datetime

src_path = 'C:\\Users\\lenovo\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
dest_path = 'C:\\Users\\lenovo\\Desktop'

folder_name = 'Spotlight-Images-'+str(datetime.datetime.now().strftime("%Y-%m-%d"))
dest_path = os.path.join(dest_path, folder_name)
os.mkdir(dest_path)

count = 0
for file in os.listdir(src_path):
  if os.path.getsize(os.path.join(src_path, file)) > 139175L:
    shutil.copy(os.path.join(src_path, file), os.path.join(dest_path, str(count)+'.jpg'))
    count = count + 1