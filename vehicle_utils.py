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