import bpy
from bpy import context
scene = context.scene

bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_post.clear()

PATH = "/Users/johnryan/Desktop/Cornell/blender/bakefiles/"
OBJECT_NAME = ""
def remove_mesh_from_memory(object_name):
    mesh = bpy.data.meshes[object_name]
    mesh.user_clear()
    bpy.data.meshes.remove(mesh)

def run_before_frame_change(scene):
    bpy.ops.object.select_all(action='DESELECT')
    global OBJECT_NAME
    if (OBJECT_NAME != ""):
        obj = bpy.data.objects[OBJECT_NAME]
        bpy.data.scenes[0].objects.unlink(obj)
        bpy.data.objects.remove(obj)
        remove_mesh_from_memory(obj)
def run_after_frame_change(scene):
    global PATH
    frame_num = scene.frame_current
    bpy.ops.import_mesh.ply(filepath=(PATH+str(frame_num)+".ply"))
    global OBJECT_NAME
    OBJECT_NAME = str(frame_num)

bpy.app.handlers.frame_change_pre.append(run_before_frame_change)
bpy.app.handlers.frame_change_post.append(run_after_frame_change)

