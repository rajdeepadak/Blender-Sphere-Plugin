bl_info = {"name" : "Sphere Plugin",
           "author" : "Rajdeep Adak",
           "version" : (1, 0),
           "blender" : (2, 91, 2),
           "location" : "View3D > Toolbar > Sphere Plugin",
           "Description" : "Addon to modify a Sphere",
           "warning" : "",
           "wiki_url" : "",
           "category" : "UI Panel Addon"}

# Imports ------------------------------------------------------------------------------------
import os 
import bpy
from bpy_extras.io_utils import ImportHelper 
from bpy import context, data, ops
from mathutils import Vector
from bpy.types import (Panel, Operator, AddonPreferences,
                       PropertyGroup)
from bpy.props import (FloatProperty, FloatVectorProperty, IntProperty, EnumProperty,
                       BoolProperty, StringProperty, PointerProperty)               
# --------------------------------------------------------------------------------------------

# Update Functions ---------------------------------------------------------------------------           

# --------------------------------------------------------------------------------------------
    
# Feature Set 2 ----------------------------------------------------------------------------------
class TextureFile(Panel):
    bl_label = "Add Texture (Feature Set 2)"
    bl_idname = "PT_Texture_File"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sphere Plugin'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        row = layout.row()
        
        if obj:
            row.label(text = "Choose File:")             
            row.operator("test.open_filebrowser", 
                         icon = 'FILEBROWSER')
            col = layout.column()
            col.operator("apply.texturefile", 
                         icon = 'MATFLUID',
                         text = "Apply Texture from File")  
            col.operator("remove.texturefile", 
                         icon = 'CANCEL',
                         text = "Remove Texture from Object")             
            col.operator("return.solidview", 
                         icon = 'SHADING_SOLID',
                         text = "Solid Mode")   
        else:
            row.label(text = "Construct Sphere to Enable", 
                      icon = 'SORT_DESC')                           

class OT_TestOpenFilebrowser(Operator, ImportHelper): 
    bl_idname = "test.open_filebrowser" 
    bl_label = "Browse File" 
     
    filter_glob: StringProperty(default='*.jpg;*.jpeg;*.png;*.tif;*.tiff;*.bmp',                                  
                                options={'HIDDEN'})                               
                               
    def execute(self, context): 
        filename, extension = os.path.splitext(self.filepath) 
        
        mat = bpy.data.materials.new(name="New_Mat")
        mat.use_nodes = True
        
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImage.image = bpy.data.images.load(self.filepath)
        mat.node_tree.links.new(bsdf.inputs['Base Color'], 
                                texImage.outputs['Color'])
 
        ob = context.view_layer.objects.active

        if ob.data.materials:
            ob.data.materials[0] = mat
        else:
            ob.data.materials.append(mat)
            
        bpy.context.space_data.shading.type = 'SOLID'
        return {'FINISHED'}          
        
class applytexture(Operator): 
    bl_idname = "apply.texturefile" 
    bl_label = "Apply Texture and display in Material view" 
                                                              
    def execute(self, context):
        bpy.context.space_data.shading.type = 'MATERIAL'
        return {'FINISHED'}

class removetexture(Operator):
    bl_idname = "remove.texturefile" 
    bl_label = "Remove Texture" 
                                                              
    def execute(self, context):
        mat = bpy.data.materials.new(name="New_Mat")
        mat.use_nodes = True
        
        ob = context.view_layer.objects.active

        if ob.data.materials:
            ob.data.materials[0] = mat
        else:
            ob.data.materials.append(mat)
        return {'FINISHED'}

class returnsolid(Operator): 
    bl_idname = "return.solidview" 
    bl_label = "Return to Solid View" 
                                                              
    def execute(self, context):
        bpy.context.space_data.shading.type = 'SOLID'
        return {'FINISHED'}

# End of Feature Set 2 -----------------------------------------------------------------                     
                
# ---------------------------- Register/ Unregister ------------------------------------
classes = [TextureFile, OT_TestOpenFilebrowser, applytexture, removetexture, 
           returnsolid]

def register():                                                                                                                              
    for cls in classes:
        bpy.utils.register_class(cls)   
    
def unregister():  
    for cls in classes:
        bpy.utils.unregister_class(cls)   
        
if __name__ == "__main__":
    register()        
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)