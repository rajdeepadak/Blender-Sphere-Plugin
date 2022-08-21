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
classes = [SpherePanel, rendermode, SetCenter, SetRadius, ObjectOptions, 
           TextureFile, OT_TestOpenFilebrowser, applytexture, removetexture, 
           returnsolid, ChangeVertices, DeleteVertices, DissolveVertices]

def register():    
    bpy.types.Object.scale_vector = FloatVectorProperty() 
    bpy.types.Object.Set = BoolProperty(default=False,
                                        update=Set)
    bpy.types.Object.radius = FloatProperty(name="           ",
                                            default=1,
                                            update=scale_obj)                                           
    bpy.types.Scene.check = BoolProperty(name="Enable or Disable",
                                         description="Checkbox to Select Vertice",
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