import pathlib
import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir) / "compressed2.zip"
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["average.py", "cli_todo.py"], dest_dir="dest")