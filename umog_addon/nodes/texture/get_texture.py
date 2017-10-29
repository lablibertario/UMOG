from ... base_types import UMOGNode
from ..umog_node import UMOGNode
from ...engine import types, engine, mesh
import bpy


class GetTextureNode(bpy.types.Node, UMOGNode):
    bl_idname = "umog_TextureNode"
    bl_label = "Texture Node"
    assignedType = "Texture2"

    texture_name = bpy.props.StringProperty()

    def create(self):
        socket = self.newOutput(
            self.assignedType, "Texture", drawOutput=True, drawLabel=False)
        socket.display.refreshableIcon = False
        socket.display.packedIcon = False

    def draw(self, layout):
        # only one template_preview can exist per screen area https://developer.blender.org/T46733
        # make sure that at most one preview can be opened at any time
        pass

    def init(self, context):
        self.outputs.new("ArraySocketType", "Output")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop_search(self, "texture_name", bpy.data, "textures", icon="TEXTURE_DATA", text="")
        try:
            if self.select and (len(bpy.context.selected_nodes) == 1):
                layout.template_preview(self.outputs[0].getTexture())
        except:
            pass

    def execute(self, refholder):
        # print("get texture node execution, texture: " + self.texture)
        # print("texture handle: " + str(self.outputs[0].texture_index))
        # print(refholder.np2dtextures[self.outputs[0].texture_index])
        pass

    def preExecute(self, refholder):
        try:
        # consider saving the result from this
        # self.outputs[0].texture_index = refholder.getRefForTexture2d(
        #     self.texture)
                layout.template_preview(bpy.data.textures[self.texture_name])
        except:
            pass

    def get_operation(self):
        return engine.Operation(
            engine.CONST,
            [],
            [types.Array(1, 100, 100, 1, 0, 1)],
            [types.Array(1, 100, 100, 1, 0, 1)],
            [])

    def get_buffer_values(self):
        return [mesh.array_from_texture(bpy.data.textures[self.texture_name], 100, 100)]

    def update(self):
        pass
