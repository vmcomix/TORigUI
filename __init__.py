import bpy
import sys
import requests
from pathlib import Path
from importlib import reload
from bpy.types import AddonPreferences
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class

bl_info = {
	'name' : "TOAnimate Rig UI"
	,'author' : "Vlad Mokhov"
	,'version' : (1, 4, 1)
	,'blender' : (4, 0, 0)
	,'description' : "Add on for displaying the UI panel on TOAnimate rigs."
	,'location': "View 3D > Sidebar(N) > TORigUI"
	,'category': 'Rigging'
}

extra_modules = ['extras_cartoony_max.py', 'vehicle_utils.py', 'extras_space_rover.py', 'extras_cyberbike.py']

missing_modules = []
for module in extra_modules:
    current_directory = Path(__file__).resolve().parent
    if not Path(current_directory / module).exists():
        missing_modules.append(module)

if missing_modules == []:
    pass # all good in the hood
else:
    for module in missing_modules:
        file_url = f'https://raw.githubusercontent.com/vmcomix/TORigUI/master/{module}'
        destination = current_directory / module
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)
        elif response.status_code == 404:
            print("Trouble connecting to github to update TORigUI")
            break
    bpy.ops.script.reload()
 

reload_list = [
                'ui_panel',
                'update',
                'extras_cartoony_max',
                'vehicle_utils',
                'extras_space_rover',
                'extras_cyberbike'
              ]

# This makes sure to reload the modules when running "Reload Scripts"
for module in reload_list:
    if module in locals():
        reload(sys.modules[__name__ + '.' + module])
    else:
        from . import ui_panel
        from . import update
        from . import extras_cartoony_max
        from . import vehicle_utils
        from . import extras_space_rover
        from . import extras_cyberbike


class TORigUIPreferences(AddonPreferences):

    bl_idname = __name__

    update: StringProperty(default="")

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        if self.update == "Update available":
            row.operator("pose.to_rigui_update_addon", text="Update", icon="IMPORT").update = True
        else:
            row.operator("pose.to_rigui_update_addon", text="Check for Update", icon="QUESTION").check_update = True

        row = layout.row()
        if not self.update == "":
            row.label(text=self.update)

class_list = {
    ui_panel.VIEW3D_PT_TORigUI,
    ui_panel.RIGIFY_OT_get_frame_range,
    ui_panel.POSE_OT_rigify_generic_snap,
    ui_panel.POSE_OT_rigify_generic_snap_bake,
    ui_panel.POSE_OT_rigify_clear_keyframes,
    ui_panel.POSE_OT_rigify_limb_ik2fk,
    ui_panel.POSE_OT_rigify_limb_ik2fk_bake,
    ui_panel.POSE_OT_rigify_leg_roll_ik2fk,
    ui_panel.POSE_OT_rigify_leg_roll_ik2fk_bake,
    ui_panel.POSE_OT_rigify_switch_parent,
    ui_panel.POSE_OT_rigify_switch_parent_bake,
    ui_panel.POSE_OT_rigify_finger_fk2ik,
    ui_panel.POSE_OT_rigify_finger_fk2ik_bake,
    ui_panel.POSE_OT_rig_change_resolution,
    ui_panel.POSE_OT_rig_set_mask,
    update.TORigUIAddonUpdate,
    TORigUIPreferences,
    extras_cartoony_max.POSE_OT_MaxCartoonyToggleVisibility,
    vehicle_utils.POSE_OT_VehicleTogglePath,
    vehicle_utils.POSE_OT_VehicleSetFloor,
    vehicle_utils.POSE_OT_VehicleClearFloor,
}

def register():
    for cls in class_list:
        register_class(cls)

    register_class(extras_cartoony_max.VIEW3D_PT_TORigUI_CartoonyMax)
    register_class(extras_space_rover.VIEW3D_PT_TORigUI_SpaceRoverUI)
    register_class(extras_cyberbike.VIEW3D_PT_TORigUI_CyberbikeUI)

def unregister():
    for cls in class_list:
        unregister_class(cls)

    unregister_class(extras_cartoony_max.VIEW3D_PT_TORigUI_CartoonyMax)
    unregister_class(extras_space_rover.VIEW3D_PT_TORigUI_SpaceRoverUI)
    unregister_class(extras_cyberbike.VIEW3D_PT_TORigUI_CyberbikeUI)
