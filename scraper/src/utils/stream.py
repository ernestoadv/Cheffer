import json, os
from datetime import datetime
from pathlib import Path

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        print(obj)
        if hasattr(obj, '__json__'):
            return obj.__json__()
        else:
            return json.JSONEncoder.default(self, obj)

def create_dir(dir):
    # Check whether the specified path exists or not
    isExist = os.path.exists(dir)
    
    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(dir)
        print("\nDirectory does not exist. Creating it...")

def write_json(dir, obj):
    # First, create dir if needed
    create_dir(dir)
    
    # Second, rename outdated files
    for file in os.listdir(dir):
        # Get file stem (without extension)
        file_stem = Path(file).stem
        
        # Check if file is in out directory and ends by .json
        is_json = os.path.isfile(os.path.join(dir, file_stem + '.json'))

        # Just save files that are not in out directory
        if is_json and not 'old' in file:
            os.rename(dir + file, dir + "old." + file)
        
        # File is not to be saved
        if not is_json:
            print('FILE WON\'T BE SAVED: ', file)

    # Name new file
    file_name = "scraper." + datetime.now().strftime("%H_%M_%S-%d_%m_%Y") + '.json'
    
    # Write data into file and save it
    with open(dir + file_name, 'w', encoding='raw_unicode_escape') as write_file:
        json_data = json.dumps(obj, default=lambda x: x.__dict__)
        json.dump(json.JSONDecoder().decode(json_data), write_file, cls = ComplexEncoder, indent = 4, ensure_ascii=False, sort_keys=True)
        print("\nSuccess! Data saved in: " + dir + file_name)
        