import bpy

class VIEW3D_PT_TORigUI_VehicleUI(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TO Rig UI'
    bl_label = "Vehicle Rig - Special Settings"
    bl_parent_id = "VIEW3D_PT_TORigUI"

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob.data.get("is_toanimate_vehicle") and "settings" in context.active_bone.name

    def draw(self, context):
        if "settings" in context.active_pose_bone.name:
            ob = context.active_object
            layout = self.layout
            row = layout.row()
            row.operator("pose.toggle_vehicle_path", text="Toggle Path")

            row = layout.row()
            try:
                row.prop(ob.pose.bones["MCH-null"].constraints["Shrinkwrap"], "target")
            except KeyError:
                pass
            row = layout.row(align=True)
            row.operator("pose.vehiclesetfloor", text="Set Floor")
            row.operator("pose.vehicleclearfloor", text="Clear Floor")
            if ob.data.get("wheels"):
                col = layout.column(align=True)
                row = col.row(align=True)
                row.label(text="Wheels attached to floor:")
                positions = {"front":"Front", "back":"Back"}
                sides = {".L":"Left", ".R":"Right"}

                for wheel in ob.data.get("wheels"):
                    for key in positions.keys():
                        if key in wheel:
                            pos = positions[key]
                            break

                    for key in sides.keys():
                        if key in wheel:
                            side = sides[key]
                            break

                    row = col.row(align=True)
                    row.prop(ob.pose.bones[wheel].constraints["Shrinkwrap"], "influence", text=pos + " " + side + " Wheel")
            layout.separator()

            col = layout.column(align=True)
            row = col.row(align=True)
            row.scale_y = 1.4
            row.prop(context.active_pose_bone, '["drive"]', text="Drive", slider=True)

            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["path_rotation"]', text="Rotate along path", slider=True)

            row = col.row(align=True)
            row.prop(context.active_pose_bone, '["wheel_auto_spin"]', text="Wheel Auto Spin", slider=True)
            row.prop(context.active_pose_bone, '["wheel_spin_rate"]', text="Wheel Spin Rate")

            layout.separator()
            row = layout.row(align=True)
            row.prop(context.active_pose_bone, '["light_brightness"]', text="Light Brightness", slider=True)

            row = layout.row(align=True)
            row.prop(context.active_pose_bone, '["glass_visibility"]', text="Glass Visibility")