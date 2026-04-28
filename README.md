# Mio3 Avatar Tools (English)

A collection of utility tools for bone editing support in Blender.

Originally created by [mio3io](https://github.com/mio3io/mio3_avatar_tools).

The original README.md contents below has been translated from Japanese into English.

## Installation

Download the ZIP file from Code (Big green button) > Download ZIP.

In Blender, navigate to `Edit > Preferences > Add-ons`, click the dropdown arrow in the top-right corner, select `Install from Disk`, choose the downloaded add-on ZIP file, and click the Install button. After installation, check the box to the left of the corresponding add-on to enable it.


## Features

Added to the Right-Click Menu and the Armature Menu.

### Add > Armature

Adds a Humanoid Armature for VRChat.

### Armature > Transform

-   Even Out Bones
-   Align Bones (Based on the first and last bones)

### Armature > Name

-   Assign Sequential Numbers to Bones

### Sidebar > Mio3 Tab

-   Batch Conversion of Bone Name Formats (Experimental): Convert the bone names currently displayed in Pose Mode to a specified format.

This feature has been added on an experimental basis. Since we cannot guarantee that the conversion will be successful, please verify the results after performing the conversion.

The conversion may fail if the original bone names do not follow a specific, recognizable pattern.
Note that the system is designed to convert *only* the bones currently being displayed; therefore, please ensure that only the necessary bones are visible when performing the conversion.

Currently, the only available output formats are "UpperArm_L" and "UpperArm.L".

Examples of Recognized Patterns:

-   UpperArm_L
-   Upper Arm_L
-   UpperArm.L
-   Upper Arm.L
-   L_UpperArm
-   LeftUpperArm
-   UpperArmLeft
-   Skirt
-   SkirtFront2.001
-   SkirtSide2.L.001_end
-   (CustomPrefix)Arm_L

Custom Prefixes

-   If you wish to convert `IK_UpperArm_L` into the format `IK_UpperArm.L`, simply register `IK_` as a custom prefix; it will then be applied exactly as entered. You can also use this feature to remove unwanted prefixes.

<!--
Patterns That May Not Convert as Expected

-   Patterns involving consecutive capital letters—such as `IK_Arm_L`—are typically treated as separate components (e.g., `I_K_Arm_L`). Therefore, please register such sequences as custom prefixes (e.g., registering `IK_` ensures it is applied exactly as entered).
-->
