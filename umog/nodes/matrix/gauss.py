from .. import UMOGNode
import bpy
import numpy as np

class GaussNode(UMOGNode):
    bl_idname = "umog_GaussNode"
    bl_label = "Gaussian Blur"
    
    radius = bpy.props.IntProperty(default = 3)
    sigma = bpy.props.FloatProperty(default = 1.0)
    
    def init(self, context):
        self.outputs.new("Mat3SocketType", "Output")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop(self, "radius", text="Radius")
        layout.prop(self, "sigma", text="Sigma")
        
    def preExecute(self, refholder):
        print('begin preExecute gauss')

    def execute(self, refholder):
    
        print('begin gauss')
    
        # generate matrix
        gauss_matrix = np.zeros((self.radius, self.radius), dtype=np.float)
        size = self.radius
        total = 0
        for i in range (-(size - 1)//2, (size - 1)//2 + 1):
            for j in range (-(size - 1)//2, (size - 1)//2 + 1):
                x0 = size//2
                y0 = size//2
                x = x0 + i
                y = y0 + j
                value = np.exp(-((x-x0)**2 + (y-y0)**2)/(2 * self.sigma**2))   
                gauss_matrix[x][y] =  value
                total += value
                
        # normalize matrix
        for i in range(0,size):
            for j in range(0,size):
                gauss_matrix[i][j] = gauss_matrix[i][j]/total
    
        self.outputs[0].matrix_ref = refholder.getRefForMatrix(gauss_matrix)

        for elem in gauss_matrix:
            print(elem)