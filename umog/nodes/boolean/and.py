from ..umog_node import *
from ...engine import types, engine
import bpy

class AndNode(UMOGNode):
    bl_idname = "umog_AndNode"
    bl_label = "And Node"

    def init(self, context):
        self.inputs.new("FloatSocketType", "a")
        self.inputs.new("FloatSocketType", "b")
        self.outputs.new("FloatSocketType", "out")
        super().init(context)

    def get_operation(self, input_types):
        output_types = types.binary_scalar(input_types[0], input_types[1])

        return engine.Operation(
            engine.AND,
            output_types,
            [],
            [engine.Argument(engine.ArgumentType.SOCKET, 0), engine.Argument(engine.ArgumentType.SOCKET, 1)],
            [])

    def update(self):
        pass
