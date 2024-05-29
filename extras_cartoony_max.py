import bpy

class POSE_OT_MaxCartoonyToggleVisibility(bpy.types.Operator):
    """Lil MaxToggle Visibility"""
    bl_idname = "pose.max_cartoony_toggle_vis"
    bl_label = "Toggle Visibility for Lil Max"
    
    hide_bones : bpy.props.StringProperty(default="")
    hide_geo : bpy.props.StringProperty(default="")
    keyed_only: bpy.props.BoolProperty(default=True)
    
    def execute(self,context):
        
        if self.hide_bones == "left_thumb":
            bones = ['thumb_deformer_01.L', 
                    'thumb_deformer_03.L', 
                    'thumb_deformer_05.L', 
                    'thumb_deformer_07.L', 
                    'thumb_deformer_02.L', 
                    'thumb_deformer_04.L', 
                    'thumb_deformer_06.L', 
                    'thumb_deformer_08.L']
        
        elif self.hide_bones == "left_index_f":
            bones = ['f_index_deformer_01.L', 
                     'f_index_deformer_04.L', 
                     'f_index_deformer_07.L', 
                     'f_index_deformer_010.L', 
                     'f_index_deformer_02.L', 
                     'f_index_deformer_05.L', 
                     'f_index_deformer_08.L', 
                     'f_index_deformer_011.L', 
                     'f_index_deformer_03.L', 
                     'f_index_deformer_06.L', 
                     'f_index_deformer_09.L', 
                     'f_index_deformer_012.L']
        
        elif self.hide_bones == "left_middle_f":
            bones = ['f_middle_deformer_01.L',
                     'f_middle_deformer_04.L', 
                     'f_middle_deformer_07.L', 
                     'f_middle_deformer_010.L', 
                     'f_middle_deformer_02.L', 
                     'f_middle_deformer_05.L', 
                     'f_middle_deformer_08.L', 
                     'f_middle_deformer_011.L', 
                     'f_middle_deformer_03.L', 
                     'f_middle_deformer_06.L', 
                     'f_middle_deformer_09.L', 
                     'f_middle_deformer_012.L']
            
        elif self.hide_bones == "left_pinky_f":
            bones = ['f_pinky_deformer_01.L',
                     'f_pinky_deformer_04.L', 
                     'f_pinky_deformer_07.L', 
                     'f_pinky_deformer_010.L', 
                     'f_pinky_deformer_02.L', 
                     'f_pinky_deformer_05.L', 
                     'f_pinky_deformer_08.L', 
                     'f_pinky_deformer_011.L', 
                     'f_pinky_deformer_03.L', 
                     'f_pinky_deformer_06.L', 
                     'f_pinky_deformer_09.L', 
                     'f_pinky_deformer_012.L']
        
        elif self.hide_bones == "right_thumb":
            bones = ['thumb_deformer_01.R',
                     'thumb_deformer_03.R', 
                     'thumb_deformer_05.R', 
                     'thumb_deformer_07.R', 
                     'thumb_deformer_02.R',
                     'thumb_deformer_04.R', 
                     'thumb_deformer_06.R', 
                     'thumb_deformer_08.R']
        
        elif self.hide_bones == "right_index_f":
            bones = ['f_index_deformer_01.R',
                     'f_index_deformer_04.R', 
                     'f_index_deformer_07.R', 
                     'f_index_deformer_010.R', 
                     'f_index_deformer_02.R', 
                     'f_index_deformer_05.R', 
                     'f_index_deformer_08.R', 
                     'f_index_deformer_011.R', 
                     'f_index_deformer_03.R', 
                     'f_index_deformer_06.R', 
                     'f_index_deformer_09.R', 
                     'f_index_deformer_012.R']
        
        elif self.hide_bones == "right_middle_f":
            bones = ['f_middle_deformer_01.R',
                     'f_middle_deformer_04.R', 
                     'f_middle_deformer_07.R', 
                     'f_middle_deformer_010.R', 
                     'f_middle_deformer_02.R', 
                     'f_middle_deformer_05.R', 
                     'f_middle_deformer_08.R', 
                     'f_middle_deformer_011.R', 
                     'f_middle_deformer_03.R', 
                     'f_middle_deformer_06.R', 
                     'f_middle_deformer_09.R', 
                     'f_middle_deformer_012.R']
        
        elif self.hide_bones == "right_pinky_f":
            bones = ['f_pinky_deformer_01.R',
                     'f_pinky_deformer_04.R', 
                     'f_pinky_deformer_07.R', 
                     'f_pinky_deformer_010.R', 
                     'f_pinky_deformer_02.R', 
                     'f_pinky_deformer_05.R', 
                     'f_pinky_deformer_08.R', 
                     'f_pinky_deformer_011.R', 
                     'f_pinky_deformer_03.R', 
                     'f_pinky_deformer_06.R', 
                     'f_pinky_deformer_09.R', 
                     'f_pinky_deformer_012.R']
                     
        elif self.hide_bones == "head":
            bones = ['head_deformer_02.L',
                     'head_deformer_02_mid', 
                     'head_deformer_07_mid', 
                     'head_deformer_06.L', 
                     'head_deformer_09.L', 
                     'head_deformer_02.R', 
                     'head_deformer_06.R', 
                     'head_deformer_09.R', 
                     'head_deformer_03_mid', 
                     'head_deformer_04_mid', 
                     'head_deformer_05_mid', 
                     'head_deformer_06_mid', 
                     'head_deformer_03.L', 
                     'head_deformer_04.L', 
                     'head_deformer_07.L', 
                     'head_deformer_10.L', 
                     'head_deformer_03.R', 
                     'head_deformer_04.R', 
                     'head_deformer_07.R', 
                     'head_deformer_10.R', 
                     'head_deformer_01_mid', 
                     'head_deformer_08_mid', 
                     'head_deformer_01.L', 
                     'head_deformer_05.L', 
                     'head_deformer_08.L', 
                     'head_deformer_01.R', 
                     'head_deformer_05.R', 
                     'head_deformer_08.R', 
                     'head_deformer_11_mid', 
                     'head_deformer_10_mid', 
                     'head_deformer_09_mid', 
                     'head_deformer_11.L', 
                     'head_deformer_12.L', 
                     'head_deformer_13.L', 
                     'head_deformer_11.R', 
                     'head_deformer_12.R', 
                     'head_deformer_13.R']

        elif self.hide_bones == "torso":
            bones = ['torso_deformer_01.L',
                     'torso_deformer_04_mid', 
                     'torso_deformer_01_mid', 
                     'torso_deformer_01.R', 
                     'torso_deformer_02.L', 
                     'torso_deformer_05_mid', 
                     'torso_deformer_02_mid', 
                     'torso_deformer_02.R', 
                     'torso_deformer_03.L', 
                     'torso_deformer_06_mid', 
                     'torso_deformer_03_mid', 
                     'torso_deformer_03.R']
        
        elif self.hide_bones == "right_arm":
            bones = ['arm_deformer_05.R',
                     'arm_deformer_010.R', 
                     'arm_deformer_015.R', 
                     'arm_deformer_020.R', 
                     'arm_deformer_04.R', 
                     'arm_deformer_09.R', 
                     'arm_deformer_014.R', 
                     'arm_deformer_019.R', 
                     'arm_deformer_03.R', 
                     'arm_deformer_08.R', 
                     'arm_deformer_013.R', 
                     'arm_deformer_018.R', 
                     'arm_deformer_02.R', 
                     'arm_deformer_07.R', 
                     'arm_deformer_012.R', 
                     'arm_deformer_017.R', 
                     'arm_deformer_01.R', 
                     'arm_deformer_06.R', 
                     'arm_deformer_011.R', 
                     'arm_deformer_016.R']

        elif self.hide_bones == "left_arm":
            bones = ['arm_deformer_01.L',
                     'arm_deformer_06.L', 
                     'arm_deformer_011.L', 
                     'arm_deformer_016.L', 
                     'arm_deformer_02.L', 
                     'arm_deformer_07.L', 
                     'arm_deformer_012.L', 
                     'arm_deformer_017.L', 
                     'arm_deformer_03.L', 
                     'arm_deformer_08.L', 
                     'arm_deformer_013.L', 
                     'arm_deformer_018.L', 
                     'arm_deformer_05.L', 
                     'arm_deformer_010.L', 
                     'arm_deformer_015.L', 
                     'arm_deformer_020.L', 
                     'arm_deformer_04.L', 
                     'arm_deformer_09.L', 
                     'arm_deformer_014.L', 
                     'arm_deformer_019.L']

        elif self.hide_bones == "right_leg":
            bones = ['foot_deformer_012.R',
                     'foot_deformer_013.R', 
                     'foot_deformer_014.R', 
                     'foot_deformer_015.R', 
                     'foot_deformer_07.R', 
                     'foot_deformer_09.R', 
                     'foot_deformer_010.R', 
                     'foot_deformer_011.R', 
                     'foot_deformer_01.R', 
                     'foot_deformer_02.R', 
                     'foot_deformer_03.R', 
                     'foot_deformer_04.R', 
                     'leg_deformer_013.R', 
                     'leg_deformer_014.R', 
                     'leg_deformer_015.R', 
                     'leg_deformer_016.R', 
                     'foot_deformer_05.R', 
                     'foot_deformer_06.R', 
                     'foot_deformer_08.R', 
                     'leg_deformer_09.R', 
                     'leg_deformer_010.R', 
                     'leg_deformer_011.R', 
                     'leg_deformer_012.R', 
                     'leg_deformer_05.R', 
                     'leg_deformer_06.R', 
                     'leg_deformer_07.R', 
                     'leg_deformer_08.R', 
                     'leg_deformer_01.R', 
                     'leg_deformer_02.R', 
                     'leg_deformer_03.R', 
                     'leg_deformer_04.R']
        
        elif self.hide_bones == "left_leg":
            bones = ['leg_deformer_01.L',
                     'leg_deformer_02.L', 
                     'leg_deformer_03.L', 
                     'leg_deformer_04.L', 
                     'leg_deformer_05.L', 
                     'leg_deformer_06.L', 
                     'leg_deformer_07.L', 
                     'leg_deformer_08.L', 
                     'leg_deformer_013.L', 
                     'leg_deformer_014.L', 
                     'leg_deformer_015.L', 
                     'leg_deformer_016.L', 
                     'foot_deformer_012.L', 
                     'foot_deformer_013.L', 
                     'foot_deformer_014.L', 
                     'foot_deformer_015.L', 
                     'foot_deformer_07.L', 
                     'foot_deformer_09.L', 
                     'foot_deformer_010.L',
                     'foot_deformer_011.L', 
                     'foot_deformer_01.L', 
                     'foot_deformer_02.L', 
                     'foot_deformer_03.L', 
                     'foot_deformer_04.L', 
                     'foot_deformer_05.L', 
                     'foot_deformer_06.L', 
                     'foot_deformer_08.L', 
                     'leg_deformer_09.L', 
                     'leg_deformer_010.L', 
                     'leg_deformer_011.L', 
                     'leg_deformer_012.L']
                     
        elif self.hide_bones == "left_hand_stretch":
            bones = ['hand_stretch_base.L', 'hand_stretch_end.L']
        
        elif self.hide_bones == "right_hand_stretch":
            bones = ['hand_stretch_base.R', 'hand_stretch_end.R']
            
        elif self.hide_bones == "head_tweakers":
            bones = ['head_deformer_03_mid', 'head_deformer_04_mid', 'head_deformer_05_mid', 'head_deformer_06_mid', 'head_deformer_03.L', 'head_deformer_04.L', 'head_deformer_07.L', 'head_deformer_10.L', 'head_deformer_03.R', 'head_deformer_04.R', 'head_deformer_07.R', 'head_deformer_10.R', 'head_deformer_02.L', 'head_deformer_02_mid', 'head_deformer_07_mid', 'head_deformer_06.L', 'head_deformer_09.L', 'head_deformer_02.R', 'head_deformer_06.R', 'head_deformer_09.R', 'head_deformer_01_mid', 'head_deformer_08_mid', 'head_deformer_01.L', 'head_deformer_05.L', 'head_deformer_08.L', 'head_deformer_01.R', 'head_deformer_05.R', 'head_deformer_08.R', 'head_deformer_11_mid', 'head_deformer_10_mid', 'head_deformer_09_mid', 'head_deformer_11.L', 'head_deformer_12.L', 'head_deformer_13.L', 'head_deformer_11.R', 'head_deformer_12.R', 'head_deformer_13.R']
        
        if self.hide_geo == "left_leg":
            geo = ['mc_shorts_geo.L', 'mc_legs_geo.L', 'mc_shoe_geo.L', 'mc_shoe_logo_geo.L', 'mc_shoe_geo_multiple.L', 'mc_legs_geo_multiple1.L', 'mc_shorts_geo_multiple1.L', 'mc_shoe_logo_geo_multiple1.L', 'mc_shoe_geo_multiple2.L', 'mc_shoe_logo_geo_multiple2.L', 'mc_legs_geo_multiple2.L', 'mc_shorts_geo_multiple2.L']
        
        elif self.hide_geo == "right_leg":
            geo = ['mc_shorts_geo.R', 'mc_legs_geo.R', 'mc_shoe_geo.R', 'mc_shoe_logo_geo.R', 'mc_legs_geo_multiple1.R', 'mc_shoe_geo_multiple.R', 'mc_shorts_geo_multiple1.R', 'mc_legs_geo_multiple2.R', 'mc_shoe_geo_multiple2.R', 'mc_shorts_geo_multiple2.R', 'mc_shoe_logo_geo_multiple1.R', 'mc_shoe_logo_geo_multiple2.R']
            
        elif self.hide_geo == "left_arm":
            geo = ['mc_arms_geo.L', 'mc_hands_geo.L', 'mc_hand_detail_geo.L', 'mc_arms_geo_multiple1.L', 'mc_hand_detail_geo_multiple1.L', 'mc_hands_geo_multiple1.L', 'mc_arms_geo_multiple2.L', 'mc_hand_detail_geo_multiple2.L', 'mc_hands_geo_multiple2.L', 'mc_arms_geo_multiple1.L', 'mc_hand_detail_geo_multiple1.L', 'mc_hands_geo_multiple1.L', 'mc_arms_geo_multiple2.L', 'mc_hand_detail_geo_multiple2.L', 'mc_hands_geo_multiple2.L']
            
        elif self.hide_geo == "right_arm":
            geo = ['mc_arms_geo.R', 'mc_hands_geo.R', 'mc_hand_detail_geo.R', 'mc_arms_geo_multiple2.R', 'mc_hands_geo_multiple2.R', 'mc_hand_detail_geo_multiple2.R', 'mc_arms_geo_multiple1.R', 'mc_hands_geo_multiple1.R', 'mc_hand_detail_geo_multiple1.R', 'mc_arms_geo_multiple2.R', 'mc_hands_geo_multiple2.R', 'mc_hand_detail_geo_multiple2.R']
            
        elif self.hide_geo == "torso":
            geo = ['mc_torso_geo', 'mc_torso_detail_geo', 'mc_neck_geo']
            
        elif self.hide_geo == "head":
            geo = ['mc_head_base_open_mouth_geo', 'mc_lower_teeth_geo', 'mc_upper_teeth_geo', 'mc_tongue_geo', 'mc_nose_geo', 'mc_nose_geo', 'mc_ears_geo.L', 'mc_ears_geo.R', 'mc_eyes_geo.L', 'mc_eyes_geo.R', 'mc_brows_geo', 'mc_hair_side_geo', 'mc_hair_top_geo', 'mc_head_base_closed_mouth_geo', 'mc_mouth_closed', 'mc_freckles_geo']
        
        if not self.hide_bones == "":
            
            MC = context.active_object.data
            
            if self.keyed_only == False:
                hidden = False
                for bone in bones:
                    if MC.bones[bone].hide == True:
                        hidden = True
                        break          
             
                if hidden:
                    bpy.ops.pose.select_all(action='DESELECT') 
            
                for bone in bones:
                    if hidden:
                        MC.bones[bone].hide = False
                        MC.bones[bone].select = True
                    else:
                        MC.bones[bone].hide = True
            else:
                
                action = context.active_object.animation_data.action
                hidden = False
                keyed_bones = []
                if not action == None:
                    for bone in bones:
                        for i in range(3):
                            loc = action.fcurves.find('pose.bones["' + bone + '"].location', index=i) is not None
                            rot = action.fcurves.find('pose.bones["' + bone + '"].rotation_euler', index=i) is not None
                            scale = action.fcurves.find('pose.bones["' + bone + '"].scale', index=i) is not None
                            
                            if loc or rot or scale:
                                has_keys = True
                                break
                            else:
                                has_keys = False
                                continue
                        
                        
                        if has_keys:
                            keyed_bones.append(bone)
                    
                    if not keyed_bones == []:
                        for bone in keyed_bones:  
                            if MC.bones[bone].hide == True:
                                hidden = True
                        
                        for bone in keyed_bones:
                            if hidden:
                                MC.bones[bone].hide = False
                                MC.bones[bone].select = True
                            else:
                                MC.bones[bone].hide = True
                    else:
                        self.report({'ERROR'}, "Sculptors have no keys set")
                else:
                    self.report({'ERROR'}, "This rig has no keys set")
        
        
        if not self.hide_geo == "":
            MC = bpy.data.objects
        
            hidden = False
            for ob in geo:
                if MC[ob].hide_viewport == True:
                    hidden = True
                    break
                    
            for ob in geo:
                if hidden:
                    MC[ob].hide_viewport = False
                else:
                    MC[ob].hide_viewport = True
        
        
        self.hide_bones = ""
        self.hide_geo = ""
        return {'FINISHED'}

class VIEW3D_PT_TORigUI_CartoonyMax(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TO Rig UI'
    bl_label = "Lil Max - Special Settings"
    bl_parent_id = "VIEW3D_PT_TORigUI"

    @classmethod
    def poll(cls, context):
        bone = context.active_pose_bone
        if context.active_pose_bone:
            if context.object.name == "RIG-Max_Cartoony" or context.object.name == "RIG-Lil_Max":
                if "settings" in bone.name and \
                    bone.get("fk_bones") and \
                    bone.get("ik_bones"):
                        return True
        return False
            

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        bone = context.active_pose_bone

        if "settings" in bone.name and \
            bone.get("fk_bones") and \
            bone.get("ik_bones"):

            if bone.name.endswith("L"):
                side = "left"
            else:
                side = "right"

            if "arm" in bone.name:
                limb = "arm"
            else:
                limb = "leg"

            op = row.operator('pose.max_cartoony_toggle_vis',text = f'Toggle {limb.capitalize()} Sculptors', icon='SCULPTMODE_HLT')
            op.hide_bones = side+"_"+limb
            op.keyed_only = False
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Toggle Keyed', icon='KEYFRAME')
            op.hide_bones = side+"_"+limb
            op.keyed_only = True

            if not limb == "arm":
                return

            op = layout.operator('pose.max_cartoony_toggle_vis',text = 'Toggle Hand Stretch', icon='EMPTY_SINGLE_ARROW')
            op.hide_bones = side+"_hand_stretch"
            op.keyed_only = False
            
            layout.separator() 

            layout.label(text="Toggle Finger Sculptors:")
            col = layout.column(align=True)
            row = col.row(align=True)
            
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Thumb', icon='SCULPTMODE_HLT')
            op.hide_bones = side+"_thumb"
            op.keyed_only = False
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Keyed', icon='KEYFRAME')
            op.hide_bones = side+"_thumb"
            op.keyed_only = True
            
            row = col.row(align=True)
            
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Index', icon='SCULPTMODE_HLT')
            op.hide_bones = side+"_index_f"
            op.keyed_only = False
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Keyed', icon='KEYFRAME')
            op.hide_bones = side+"_index_f"
            op.keyed_only = True
            
            row = col.row(align=True)
            
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Middle', icon='SCULPTMODE_HLT')
            op.hide_bones = side+"_middle_f"
            op.keyed_only = False
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Keyed', icon='KEYFRAME')
            op.hide_bones = side+"_index_f"
            op.keyed_only = True
            
            row = col.row(align=True)
           
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Pinky', icon='SCULPTMODE_HLT')
            op.hide_bones = side+"_pinky_f"
            op.keyed_only = False
            op = row.operator('pose.max_cartoony_toggle_vis',text = 'Keyed', icon='KEYFRAME')
            op.hide_bones = side+"_pinky_f"
            op.keyed_only = True

