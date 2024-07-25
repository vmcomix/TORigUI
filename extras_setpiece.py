import bpy

class POSE_OT_SetToggleVisibility(bpy.types.Operator):
    """Toggles path for vehicle"""
    bl_idname = "pose.toggle_set_visibility"
    bl_label = "Toggle Set Visibility"

    coll : bpy.props.StringProperty(name="collection")
    
    def execute(self,context):
        if bpy.data.collections[self.coll].hide_viewport:
            bpy.data.collections[self.coll].hide_viewport = False
        else:
            bpy.data.collections[self.coll].hide_viewport = True
        return {'FINISHED'}

class VIEW3D_PT_TORigUI_SetUI(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TO Rig UI'
    bl_label = "Set Piece - Special Settings"
    bl_parent_id = "VIEW3D_PT_TORigUI"

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        if context.active_object.type == "ARMATURE" and context.active_object.data.get("rig_id") and context.mode == "POSE":
            return ob.data.get("is_toanimate_set")

    def draw(self, context):
        ob = context.active_object
        coll_name = ob.name.replace("RIG-", "") + "-GEO"
        layout = self.layout
        layout.label(text="Disable/Enable Collections")
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.4
        new_row = False
        for collection in bpy.data.collections[coll_name].children:
            if collection.hide_viewport:
                row.operator('pose.toggle_set_visibility', text=collection.name.replace("_", " ").title(), icon="CHECKBOX_DEHLT").coll = collection.name
            else:
                row.operator('pose.toggle_set_visibility', text=collection.name.replace("_", " ").title(), icon="CHECKBOX_HLT").coll = collection.name
            if new_row:
                row = col.row(align=True)
                row.scale_y = 1.4
                new_row = False
            else:
                new_row = True

