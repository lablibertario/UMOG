import bpy
import sys
from bpy.types import NodeTree, Node, NodeSocket
import mathutils

#begining of code for debugging
#https://wiki.blender.org/index.php/Dev:Doc/Tools/Debugging/Python_Eclipse
#make this match your current installation
try:
    PYDEV_SOURCE_DIR = "/usr/lib/eclipse/dropins/pydev/plugins/org.python.pydev_5.8.0.201706061859/pysrc"
    import sys
    if PYDEV_SOURCE_DIR not in sys.path:
        sys.path.append(PYDEV_SOURCE_DIR)
    import pydevd
    print("debugging enabled")
except:
    print("no debugging enabled")
#end code for debugging

#will create a breakpoint
#pydevd.settrace()

#the lcoation of this may need changed depending on which file you want to debug
from . import properties, panel, sockets, nodes, operators



class UMOGNodeTree(bpy.types.NodeTree):
    bl_idname = "umog_UMOGNodeTree"
    bl_label = "UMOG"
    bl_icon = "SCULPTMODE_HLT"
        
    def execute(self, refholder):
        print('executing node tree');
        

def drawMenu(self, context):
    if context.space_data.tree_type != "umog_UMOGNodeTree": return
    
    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"
    layout.menu("umog_mesh_menu", text="Mesh", icon = "MESH_DATA")
# from animation nodes
def insertNode(layout, type, text, settings = {}, icon = "NONE"):
    operator = layout.operator("node.add_node", text = text, icon = icon)
    operator.type = type
    operator.use_transform = True
    for name, value in settings.items():
            item = operator.settings.add()
            item.name = name
            item.value = value
    return operator
    
#todo create the menu class
class UMOGMeshMenu(bpy.types.Menu):
    bl_idname = "umog_mesh_menu"
    bl_label = "Mesh Menu"
    
    def draw(self, context):
            layout = self.layout
            insertNode(layout, "umog_GetTextureNode", "Get Texture")
            insertNode(layout, "umog_SetTextureNode", "Set Texture")
            insertNode(layout, "umog_SaveTextureNode", "Save Texture")
            #insertNode(layout, "umog_NoiseGenerationNode", "Noise Generator")
            #insertNode(layout, "umog_Mat3Node", "Matrix 3x3")
            insertNode(layout, "umog_SculptNode", "Sculpt Dynamic Node")
            insertNode(layout, "umog_SculptNDNode", "Sculpt Static Node")
            insertNode(layout, "umog_DisplaceNode", "Displace Node")
            insertNode(layout, "umog_BMeshNode", "BMesh Node")
            insertNode(layout, "umog_BMeshCurlNode", "BMesh Curl Node")
            insertNode(layout, "umog_TextureAlternatorNode", "Texture Alternator")
            insertNode(layout, "umog_IntegerNode", "Integer")
            insertNode(layout, "umog_IntegerFrameNode", "Integer Frame")
            insertNode(layout, "umog_IntegerSubframeNode", "Integer Subframe")
            insertNode(layout, "umog_IntegerMathNode", "Integer Math")
            insertNode(layout, "umog_ReactionDiffusionNode", "Reaction Diffusion Node")


def register():
    print("begin resitration")
    # see for types to register https://docs.blender.org/api/2.78b/bpy.utils.html?highlight=register_class#bpy.utils.register_class
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
    