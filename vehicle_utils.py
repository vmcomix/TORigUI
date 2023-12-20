import bpy
import json

class POSE_OT_VehicleTogglePath(bpy.types.Operator):
    """Toggles path for vehicle"""
    bl_idname = "pose.toggle_vehicle_path"
    bl_label = "Toggle Vehicle Path"

    # path_tangents : bpy.props.StringProperty(name="Path Tangents")
    # spline_object : bpy.props.StringProperty(name="Spline Object")
    
    def execute(self,context):
        ob = context.active_object
        spline_object = ob.data["vehicle_spline_object"]
        tangents_list = ob.data["vehicle_path_tangents"]
        armature = bpy.context.active_object.data.bones
        for bone in tangents_list:
            if armature[bone].hide == True:
                bpy.data.objects[spline_object].hide_viewport = False
                armature[bone].hide = False       
            else:
                bpy.data.objects[spline_object].hide_viewport = True
                armature[bone].hide = True    
        
        return {'FINISHED'}
    
    
class POSE_OT_VehicleSetFloor(bpy.types.Operator):
    """Sticks the bike wheels to the floor"""
    bl_idname = "pose.vehiclesetfloor"
    bl_label = "Set Floor"
    
    def execute(self,context): 
        ob = context.active_object
        armature = bpy.context.active_object.pose.bones
        try:
            wheels = ob.data["wheels"]
            null = ob.pose.bones["MCH-null"].constraints["Shrinkwrap"]

            for wheel in wheels:
                shrinkwrap = [const for const in armature[wheel].constraints if const.type == "SHRINKWRAP"]
                if len(shrinkwrap) > 0:
                    shrinkwrap = shrinkwrap[0]
                    shrinkwrap.target = null.target
                else:
                    self.report({"ERROR"}, "Shrinkwrap constraint not found")

        except KeyError:
            self.report({"ERROR"}, "Missing data for wheel snapping")
        return {'FINISHED'}
        
class POSE_OT_VehicleClearFloor(bpy.types.Operator):
    """Sticks the bike wheels to the floor"""
    bl_idname = "pose.vehicleclearfloor"
    bl_label = "Clear Floor"
    
    def execute(self,context):      
        ob = context.active_object
        armature = bpy.context.active_object.pose.bones
        try:
            wheels = ob.data["wheels"]
            null = ob.pose.bones["MCH-null"].constraints["Shrinkwrap"]

            for wheel in wheels:
                shrinkwrap = [const for const in armature[wheel].constraints if const.type == "SHRINKWRAP"]
                if len(shrinkwrap) > 0:
                    shrinkwrap = shrinkwrap[0]
                shrinkwrap.target = None
                null.target = None

        except KeyError:
            self.report({"ERROR"}, "Missing data for wheel snapping")
        return {'FINISHED'}

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