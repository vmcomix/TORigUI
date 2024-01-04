
import bpy

class VIEW3D_PT_TORigUI_CyberbikeUI(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TO Rig UI'
    bl_label = "Cyberbike - Special Settings"
    bl_parent_id = "VIEW3D_PT_TORigUI"

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob.data.get("is_toanimate_vehicle") and context.active_bone.name == "COG-main" and "Cyberbike" in ob.name

    def draw(self, context):
        if context.active_pose_bone.name == "COG-main":
            ob = context.active_object
            layout = self.layout
            row = layout.row()
            row.operator("pose.toggle_vehicle_path", text="Toggle Path")

            row = layout.row()
            try:
                row.prop(ob.pose.bones["MCH-null"].constraints["Shrinkwrap"], "target")
            except KeyError:
                pass
            col = layout.column(align=True)
            row = col.row(align=True)
            row.operator("pose.vehiclesetfloor", text="Set Floor")
            row.operator("pose.vehicleclearfloor", text="Clear Floor")
            col = layout.column(align=True)
            row = col.row(align=True)
            row.label(text="Wheels attached to floor:")
            row = col.row(align=True)
            row.prop(ob.pose.bones["MCH-bike_pivot_front_aim"].constraints["Shrinkwrap"], "influence", text="Front Wheel")
            row = col.row(align=True)
            row.prop(ob.pose.bones["MCH-bike_pivot_back_aim"].constraints["Shrinkwrap"], "influence", text="Back Wheel")

            col.separator()

            col = layout.column(align=True)
            row = col.row(align=True)
            row.scale_y = 1.4
            row.prop(context.active_pose_bone, '["drive"]', text="Drive", slider=True)

            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["path_rotation"]', text="Rotate along path", slider=True)

            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["spin_rate"]', text="Wheel Spin Rate")

            col.separator()

            col = layout.column(align=True)
            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["wheel_auto_spin_front"]', text="Wheel Auto Spin Front", slider=True)
            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["wheel_auto_spin_back"]', text="Wheel Auto Spin Back", slider=True)

            col.separator()
            row = layout.row(align=True)
            row.prop(context.active_pose_bone, '["emission"]', text="Light Brightness", slider=True)