
# Tutorial

## Feature Set 1

![FS1](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/fs1.jpg)

-	Construct New Sphere : Click to construct new sphere at location of 3D Cursor. Keep 3D cursor within view in 3D viewport.
-	Delete Selected Object: Select object(s) to delete.
-	Display: Click to render object in Rendered Mode.
-	X: X Coordinate of Center of selected object. Control using float input or slider. Default value is X coordinate of 3D cursor.
-	Y: Y Coordinate of Center of selected object. Control using float input or slider. Default value is Y coordinate of 3D cursor.
-	Z: Z Coordinate of Center of selected object. Control using float input or slider. Default value is Z coordinate of 3D cursor.
-	Set: Click to Enable/Disable Radius setting of sphere.
-	Radius: If Set is Enabled Radius can be increased or decreased. Float input, Default value is 1.0.
-	Smooth Shading: Even out appearance of mesh object.
-	Subdivision Set: Add a Subdivision Surface Modifier.

## Feature Set 2

![FS2](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/fs2.jpg)

-	Browse File: Open the file browser to choose texture file.
-	Apply Texture from File: Once file is selected, click this button to apply the texture and display in Material Preview. If no texture is selected a default material will be used.
-	Remove Texture from Object: Click this button to remove the texture added onto the object from file. It will then return to default material.
-	Solid Mode: Click on this button if texture addition is done or no longer required for editing. This will shift to the Solid Mode.

## Feature Set 3

![FS3](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/fs3.jpg)

-	Check to Select Vertices: Checkbox to enable vertex selection of selected object. Select correct object before use.
-	Delete Selected Vertices: After enabling the checkbox, select vertices from the object and click this button to delete them.
-	Dissolve Selected Vertices: After enabling the checkbox, select vertices from the object and click this button to dissolve them.
-	Vertex Size: Increase or decrease size of vertices. Minimum = 1, Maximum = 32, Default = 3. Input number or use slider to control.
-	Vertex Colour Red Channel: Red channel of vertex colour space.
-	Vertex Colour Green Channel: Green channel of vertex colour space.
-	Vertex Colour Blue Channel: Blue channel of vertex colour space.

### Additional Info

-	Each Feature is built on top of the other. Hence they lie under the same category in the sidebar UI panel.
-	Code uses Render Engine: Cycles, Feature Set: Supported, Device: GPU Compute. To use eevee change Render Engine in Render Properties.
-	Enable python tooltips to view details about the operators and functions used to build the Add-on by hovering on top of the operator.
-	For HDRI background, in Render mode, select view port shading and disable scene world. Select desired HDRI and increase World opacity to view its effect.

An image of a sample project created with this Addon:

![Proj](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/proj.jpg)

