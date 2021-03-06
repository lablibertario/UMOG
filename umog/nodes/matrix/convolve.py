from ..umog_node import *
import numpy as np
import bpy
from ...engine import types, engine

class ConvolveNode(UMOGNode):
    bl_idname = "umog_ConvolveNode"
    bl_label = "Convolve Node"

    def init(self, context):
        self.outputs.new("ArraySocketType", "out")
        self.inputs.new("ArraySocketType", "kernel")
        self.inputs.new("ArraySocketType", "array")
        super().init(context)

    def draw_buttons(self, context, layout):
        pass

    def get_operation(self, input_types):
        kernel = input_types[0]
        array = input_types[1]
        types.assert_type(kernel, types.ARRAY)
        types.assert_type(array, types.ARRAY)

        channels = types.broadcast_channels(kernel, array)

        if (kernel.x_size == 0) != (array.x_size == 0) or (kernel.y_size == 0) != (array.y_size == 0) or (kernel.z_size == 0) != (array.z_size == 0):
            raise types.UMOGTypeError()

        if array.x_size == 0 and array.y_size == 0 and array.z_size == 0:
            raise UMOGTypeError()

        t_start, t_size = types.broadcast_time(kernel, array)

        output_types = [types.Array(channels, array.x_size, array.y_size, array.z_size, t_start, t_size)]

        return engine.Operation(
            engine.CONVOLVE,
            output_types,
            [],
            [engine.Argument(engine.ArgumentType.SOCKET, 0), engine.Argument(engine.ArgumentType.SOCKET, 1)],
            [])
