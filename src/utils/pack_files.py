from zipfile import ZipFile
import os

def get_all_file_paths(directory):
  file_paths = []

  for root, directories, files in os.walk(directory):
    for filename in files:
      filepath = os.path.join(root, filename)
      if "__pycache__" in filepath or "venv" in filepath or ".idea" in filepath:
        continue

      file_paths.append(filepath)
  return file_paths


def main(directory):
  file_paths = get_all_file_paths(directory)
  if os.path.exists("../../xdousa00_xslama32_xschin05.zip") and os.path.isfile("../../xdousa00_xslama32_xschin05.zip"):
    os.remove("../../xdousa00_xslama32_xschin05.zip")
  
  with ZipFile('../../xdousa00_xslama32_xschin05.zip', 'w') as zip:
    for file in file_paths:
      zip.write(file)

if __name__ == "__main__":
  main("../../xdousa00_xslama32_xschin05/")