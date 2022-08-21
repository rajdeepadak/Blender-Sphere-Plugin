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
def Set(self, context):
    if self.Set:
        self.scale_vector = self.scale.copy()
        self["radius"] = 1

def scale_obj(self, context):
    self.scale = self.radius * Vector(self.scale_vector)
# --------------------------------------------------------------------------------------------
    
# Feature Set 1 ------------------------------------------------------------------------------       
class SpherePanel(Panel):
    bl_label = "Sphere Panel (Feature Set 1)"
    bl_idname = "PT_SpherePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sphere Plugin'
        
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Click button to display sphere")
        
        col = layout.column()
        col.operator("mesh.primitive_uv_sphere_add", 
                     icon = 'MESH_UVSPHERE',
                     text = "Construct New Sphere")
                     
        col.operator("object.delete", 
                     icon = 'PANEL_CLOSE',
                     text = "Delete Selected Object")
                     
        col.operator("render.mode", 
                     icon = 'SHADING_RENDERED',
                     text = "Display")
                                          
class rendermode(Operator): 
    bl_idname = "render.mode" 
    bl_label = "Display in Render Mode" 
                                                              
    def execute(self, context):
        bpy.context.space_data.shading.type = 'RENDERED'
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        return {'FINISHED'}
               
class SetCenter(Panel):
    bl_label = "Center of Sphere"
    bl_idname = "PT_Set_Center"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sphere Plugin'
    bl_parent_id = 'PT_SpherePanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        row = layout.row()
        row.label(text = "Enter Center Coordinates:")

        col = layout.column() 
        if obj:
            col.prop(obj, "location", text="")
            
        else:
            col.label(text = 'Constuct Sphere to Enable', 
                      icon = 'SORT_DESC')

class SetRadius(Panel):
    bl_label = "Radius of Sphere"
    bl_idname = "PT_Set_Radius"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sphere Plugin'
    bl_parent_id = 'PT_SpherePanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
          
        row = layout.row()  
        if obj:      
            row.prop(obj, "Set", toggle=True)           
            if obj.Set:
                row = layout.row()
                row.label(text = 'Radius', icon ='GIZMO')
                row.prop(obj, 'radius')        
        else:
            row.label(text = 'Constuct Sphere to Enable',
                      icon = 'SORT_DESC')
        
class ObjectOptions(Panel):
    bl_label = "Sphere Modification"
    bl_idname = "PT_Object_Options"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sphere Plugin'
    bl_parent_id = 'PT_SpherePanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("object.shade_smooth", icon = 'MOD_SMOOTH',
                     text = "Smooth Shading")
        col.operator("object.subdivision_set", icon = 'ALIASED',
                     text = "Subdivision Set")                                     
# End of Feature Set 1 ---------------------------------------------------------------------------
                 
# ---------------------------- Register/ Unregister ------------------------------------
classes = [SpherePanel, rendermode, SetCenter, SetRadius, ObjectOptions]

def register():    
    bpy.types.Object.scale_vector = FloatVectorProperty() 
    bpy.types.Object.Set = BoolProperty(default=False,
                                        update=Set)
    bpy.types.Object.radius = FloatProperty(name="           ",
                                            default=1,
                                            update=scale_obj)                                                                                    
    for cls in classes:
        bpy.utils.register_class(cls)   
    
def unregister():  
    for cls in classes:
        bpy.utils.unregister_class(cls)   
        
if __name__ == "__main__":
    register()        
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)