from .. import UMOGNode
import bpy
import numpy as np

class LaplaceNode(UMOGNode):
    bl_idname = "umog_LaplaceNode"
    bl_label = "Laplace Filter"
    
    
    radius = bpy.props.IntProperty(default = 3)
    
    def init(self, context):
        self.outputs.new("Mat3SocketType", "Output")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop(self, "radius", text="Radius")
        
    def preExecute(self, refholder):
        print('begin preExecute laplace')

    def execute(self, refholder):
    
        print('begin laplace')
    
        # generate matrix
        size = self.radius
        laplace_matrix = np.ones((size, size), dtype=np.int)
        
        center = size // 2
        laplace_matrix[center][center] = 1 - (size * size)
        
        self.outputs[0].matrix_ref = refholder.getRefForMatrix(laplace_matrix)

        for elem in laplace_matrix:
            print(elem)