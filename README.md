
# Blender-Sphere-Plugin

A Blender Addon created for submission to FOSSEE's IITB Semester Long Internship 2021

##Task Description:

Create a Blender Add-On/Plugin that contains 3 'feature sets'. 
Each feature set builds on top of it's feature set and progresses 
in difficulty level

Following are expectations on the 3 feature sets:

## Feature Sets

1. Feature Set 1
-	The UI Panel will contain 3 Text boxes to accept 3 values 
    representing X, Y, Z coordinates (of the center of the intended 
    sphere) and a slider that is used to set a value representing 
    the radius of the intended sphere.
-   The UI Panel will contain a button called 'Display' that 
    will then render the Sphere in the blender interface.

2. Feature Set 2
-   Add a file input field to the UI Panel created in the 
    Feature Set 1, the uploaded file will be used as a texture file.
-   Clicking on a new 'Apply Texture' button should apply the 
    texture file on to the sphere.

3. Feature Set 3
-   Add a checkbox to the UI Panel.
-   Checking the checkbox to True, user can select vertices along
    the surface of the sphere.
-   Clicking on a new 'Change' button should delete the selected 
    vertices or display them in a different colour.
    
## Installation

### Compatibility
Compatible with Blender versions: 2.83, 2.91, 2.93. Download preferred Blender version from [Blender Downloads](https://download.blender.org/release/)

Download/clone this repository into Blender's addon system path.

```bash
  https://github.com/rajdeepadak/Blender-Sphere-Plugin.git
```

if you are unaware of Blender's addon system path run the following command
in Blender's internal python console. Open this path and then clone the repo.

```bash
  bpy.utils.user_resource('SCRIPTS', "addons")
```
![App Screenshot](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/addonpath.png)

Inside Blender go to:
Edit -> Preferences -> Add-ons 
Search "Sphere Plugin" in search box in the Add- ons and enable the checkbox.

![App Screenshot](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/addon_install.png)

To view and use the Add-on, press n with the cursor in 3D viewport or left click side arrow to view sidebar. 
An add-on named "Sphere Plugin" will be added along with the other options (View, Tool, Item) in the Viewport Sidebar as shown below.

![App Screenshot](https://github.com/rajdeepadak/Blender-Sphere-Plugin/blob/master/Images/addon.png)

## Tutorials

To view video tutorials: 

https://user-images.githubusercontent.com/65621480/185776184-b63a5a14-16f7-408e-ad80-78dfd013cc08.mp4

Check [Read Tutorial]() for more info.
