from ..umog_node import *
from ...engine import types, engine
import bpy

class IteratedDisplaceNode(UMOGNode):
    bl_idname = "umog_IteratedDisplaceNode"
    bl_label = "Iterated Displace Node"

    iterations = bpy.props.IntProperty(default = 1)

    def init(self, context):
        self.inputs.new("MeshSocketType", "mesh")
        self.inputs.new("ArraySocketType", "texture")
        self.outputs.new("MeshSocketType", "out")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop(self, "iterations", "iterations")

    def get_operation(self, input_types):
        types.assert_type(input_types[0], types.MESH)
        types.assert_type(input_types[1], types.ARRAY)

        return engine.Operation(
            engine.ITERATED_DISPLACE,
            [types.Mesh()],
            [],
            [engine.Argument(engine.ArgumentType.SOCKET, 0), engine.Argument(engine.ArgumentType.SOCKET, 1)],
            [self.iterations])

    def update(self):
        pass
