from ..umog_node import UMOGNode
import bpy
from ...engine import types, engine
import numpy as np

class ReactionDiffusionNode(UMOGNode):
    bl_idname = "umog_ReactionDiffusionNode"
    bl_label = "Reaction Diffusion"

    feed = bpy.props.FloatProperty(default=0.055)
    kill = bpy.props.FloatProperty(default=0.062)
    Da = bpy.props.FloatProperty(default=0.1)
    Db = bpy.props.FloatProperty(default=0.1)
    dt = bpy.props.FloatProperty(default=1.0)
    iterations = bpy.props.IntProperty(default=1)

    def init(self, context):
        self.inputs.new("TextureSocketType", "in")
        self.outputs.new("TextureSocketType", "out")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop(self, "feed", "Feed")
        layout.prop(self, "kill", "Kill")
        layout.prop(self, "Da", "Da")
        layout.prop(self, "Db", "Db")
        layout.prop(self, "dt", "dt")
        layout.prop(self, "iterations", "iterations")

    def get_operation(self, input_types):
        types.assert_type(input_types[0], types.ARRAY)

        return engine.Operation(
            engine.REACTION_DIFFUSION_STEP,
            [input_types[0]],
            [types.Array(5,0,0,0,0,0)],
            [engine.Argument(engine.ArgumentType.SOCKET, 0), engine.Argument(engine.ArgumentType.BUFFER, 0)],
            [self.iterations])

    def get_buffer_values(self):
        return [np.array([self.feed, self.kill, self.Da, self.Db, self.dt], dtype=np.float32, order="F").reshape((5,1,1,1,1))]

    def update(self):
        pass
