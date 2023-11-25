import bpy
import os
import requests
from pathlib import Path
from bpy.props import BoolProperty

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def download_repository_files():
    files = ['__init__.py', 'ui_panel.py']
    for file in files:
        file_url = f'https://raw.githubusercontent.com/vmcomix/TORigUI/master/{file}'
        destination = Path(os.path.split(__file__)[0]) / file
        download_file(file_url, destination)

def latest_commit_sha():
    url = f'https://api.github.com/repos/vmcomix/TORigUI/commits/master'
    response = requests.get(url)
    if response.status_code == 200:
        commit_data = response.json()
        latest_commit_sha = commit_data['sha']
        return latest_commit_sha
    else:
            print(f'Error getting latest commit. Status code: {response.status_code}')
            return None

class RigUIAddonUpdate(bpy.types.Operator):
    bl_idname = "pose.rigui_update_addon"
    bl_label = "Update add-on"
    bl_description = "Download and install new version."
    bl_options = {"REGISTER"}

    check_update: BoolProperty(default=False)

    update: BoolProperty(default=False)

    def execute(self, context):

        current_directory = Path(__file__).resolve().parent

        if self.check_update:
            if Path(current_directory / "hash" / latest_commit_sha()).exists():
                context.preferences.addons["TORigUI"].preferences.update = "Up to date"
            else:
                context.preferences.addons["TORigUI"].preferences.update = "Update available"
            self.check_update = False
        elif self.update:
            for file in current_directory.iterdir():
                if file.is_file() and len(file.stem) == 40:
                    hash = file.stem

            old_hash = current_directory / "hash" / hash
            new_hash = current_directory / "hash" /latest_commit_sha()

            old_hash.rename(new_hash)
            download_repository_files()

            context.preferences.addons["TORigUI"].preferences.update = "Updated!"
            self.update = False
            bpy.ops.script.reload()


        return {'FINISHED'}
