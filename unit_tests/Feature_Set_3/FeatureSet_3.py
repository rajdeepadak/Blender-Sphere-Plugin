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
def checkbox(self, context):
    for obj in bpy.data.objects:
        if (self.check == True):
            print ("Property Enabled")
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='DESELECT')  

        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            print ("Property Disabled")
            
def vertexsize(self, context):
    bpy.context.preferences.themes['Default'].view_3d.vertex_size = self.v_size
    
def vertexselectcolor(self, context):        
    bpy.context.preferences.themes['Default'].view_3d.vertex_select = (self.R, self.G, self.B)
# --------------------------------------------------------------------------------------------

# Feature Set 3-------------------------------------------------------------------------
class ChangeVertices(Panel):
    bl_idname = "change.vertices"
    bl_label = "Vertex Modifier (Feature Set 3)"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"    
    bl_category = "Sphere Plugin"
    
    def draw(self, context):        
        scene = context.scene
        obj = context.active_object
        
        layout = self.layout
        row = layout.row()
         
        if obj:
            row.prop(scene, "check", text=" Check to Select Vertices")           
            if obj.mode == 'EDIT': 
                row = layout.row()
                row.label(text = "Select Vertices of Object from 3D View")
                
                col = layout.column()
                col.operator("delete.vertices", 
                             icon = 'UV_VERTEXSEL',
                             text = "Delete Selected Vertices")
                         
                col.operator("dissolve.vertices",
                             icon = 'UV_FACESEL',
                             text = "Dissolve Selected Vertices")
                             
                row = layout.row()
                row.label(text = "Vertex Size", icon='PARTICLE_POINT')            
                row.prop(scene, "v_size", toggle=True)
                             
                row = layout.row()             
                row.label(text = "Change Color of Selected Vertices", icon='SORT_ASC')
                
                row = layout.row()
                row.label(text = "Red", icon='COLORSET_01_VEC')
                row.prop(scene, "R", toggle=True)
                
                row = layout.row()
                row.label(text = "Green", icon='COLORSET_03_VEC')
                row.prop(scene, "G", toggle=True)
                
                row = layout.row()
                row.label(text = "Blue", icon='COLORSET_04_VEC')
                row.prop(scene, "B", toggle=True)
                
            else:
                pass
                
        else:
                col = layout.column()
                col.label(text = "Construct Sphere to Enable",
                          icon = 'SORT_DESC')

class DeleteVertices(Operator): 
    bl_idname = "delete.vertices" 
    bl_label = "Delete vertices" 
                                                         
    def execute(self, context):
        bpy.ops.mesh.delete(type='VERT')
        
        return {'FINISHED'}
        
class DissolveVertices(Operator): 
    bl_idname = "dissolve.vertices" 
    bl_label = "Dissolve vertices" 
                                                         
    def execute(self, context):
        bpy.ops.mesh.dissolve_verts()
    
        return {'FINISHED'}
           
# End of Feature Set 3 -----------------------------------------------------------------
                 
# ---------------------------- Register/ Unregister ------------------------------------
classes = [ChangeVertices, DeleteVertices, DissolveVertices]

def register():                                              
    bpy.types.Scene.check = BoolProperty(name="Enable or Disable",
                                         description="Checkbox to Select Vertices",
                                         default = False,
                                         update = checkbox)                                          
    bpy.types.Scene.v_size = IntProperty(name = '            ',
                                         description = 'Change Vertex Size',
                                         min = 1,
                                         max = 32,
                                         default = 3,
                                         update = vertexsize)    
    bpy.types.Scene.R = FloatProperty(name = '              ',
                                      description = 'Change Red Channel',
                                      min = 0.0,
                                      max = 1.0,
                                      default = 1.0,
                                      update = vertexselectcolor)                                           
    bpy.types.Scene.G = FloatProperty(name = '               ',
                                      description = 'Change green Channel',
                                      min = 0.0,
                                      max = 1.0,
                                      default = 0.48,
                                      update = vertexselectcolor)                                           
    bpy.types.Scene.B = FloatProperty(name = '               ',
                                      description = 'Change Blue Channel',
                                      min = 0.0,
                                      max = 1.0,
                                      default = 0.0,
                                      update = vertexselectcolor)
                                            
    for cls in classes:
        bpy.utils.register_class(cls)   
    
def unregister():  
    for cls in classes:
        bpy.utils.unregister_class(cls)   
        
if __name__ == "__main__":
    register()        
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)