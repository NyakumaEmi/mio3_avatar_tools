import bpy
from bpy.types import Panel, PropertyGroup
from bpy.props import (
    BoolProperty,
    IntProperty,
    StringProperty,
    EnumProperty,
    PointerProperty,
    CollectionProperty,
)
from .operators import convert
from .operators import convert_preset
from .operators import distribute
from .operators import numbering
from .operators import add_armature


bl_info = {
    "name": "Mio3 Avatar Tools",
    "author": "mio",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Mio3",
    "description": "Avatar Armature Bone Setup support. Translated from Japanese to English.",
    "category": "Tools",
}


def menu(self, context):
    menu_transform(self, context)
    menu_name(self, context)


def menu_transform(self, context):
    self.layout.separator()
    self.layout.operator("armature.mio3_bone_align")
    self.layout.operator("armature.mio3_bone_evenly")


def menu_name(self, context):
    self.layout.separator()
    self.layout.operator("armature.mio3_bone_numbering")


def menu_armature_add(self, context):
    self.layout.separator()
    self.layout.operator("armature.mio3_add_humanoid", icon="ARMATURE_DATA")


class MIO3BONE_PT_Main(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mio3"
    bl_label = "Mio3 Avatar Tools"

    def draw(self, context):
        layout = self.layout


class MIO3BONE_PG_PrefixItem(PropertyGroup):
    name: StringProperty(name="Prefix")


class MIO3BONE_PG_Main(PropertyGroup):
    show_prefix: BoolProperty(name="Custom Prefix")
    prefix_list: CollectionProperty(name="List", type=MIO3BONE_PG_PrefixItem)
    prefix_active_index: IntProperty()
    remove_prefix: BoolProperty(name="Remove Prefix", default=False)
    input_prefix: StringProperty(name="Prefix", default="Twist_")
    convert_types: EnumProperty(
        name="After Format",
        description="",
        items=[
            ("UpperArm_L", "UpperArm_L (Recommended)", ""),
            ("UpperArm.L", "UpperArm.L", ""),
        ],
        default="UpperArm_L",
    )
    preset_reverse: BoolProperty(name="Invert Transformation")


classes = [
    MIO3BONE_PG_PrefixItem,
    MIO3BONE_PG_Main,
    MIO3BONE_PT_Main,
]

modules = [
    convert,
    convert_preset,
    distribute,
    numbering,
    add_armature,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    for module in modules:
        module.register()
    bpy.types.VIEW3D_MT_transform_armature.append(menu_transform)
    bpy.types.VIEW3D_MT_edit_armature_names.append(menu_name)
    bpy.types.VIEW3D_MT_armature_context_menu.append(menu)
    bpy.types.VIEW3D_MT_armature_add.append(menu_armature_add)
    bpy.types.Scene.mio3bone = PointerProperty(type=MIO3BONE_PG_Main)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    for module in reversed(modules):
        module.unregister()
    bpy.types.VIEW3D_MT_transform_armature.remove(menu_transform)
    bpy.types.VIEW3D_MT_edit_armature_names.remove(menu_name)
    bpy.types.VIEW3D_MT_armature_context_menu.remove(menu)
    bpy.types.VIEW3D_MT_armature_add.remove(menu_armature_add)
    del bpy.types.Scene.mio3bone


if __name__ == "__main__":
    register()
