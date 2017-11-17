from .. import UMOGNode
import bpy
import numpy as np

class Mat3Node(UMOGNode):
    bl_idname = "umog_Mat3Node"
    bl_label = "Matrix"
    bl_width_min = 240

    row1 = bpy.props.FloatVectorProperty(name = "", size=4, default=(1, 0, 0, 0))
    row2 = bpy.props.FloatVectorProperty(name = "", size=4, default=(0, 1, 0, 0))
    row3 = bpy.props.FloatVectorProperty(name = "", size=4, default=(0, 0, 1, 0))
    row4 = bpy.props.FloatVectorProperty(name = "", size=4, default=(0, 0, 0, 1))
    
    matrix = {}
    
    def init(self, context):
        self.outputs.new("Mat3SocketType", "Output")
        self.newInput("Float", "Alpha", "alpha", value = 1.0)
        self.newOutput("Float", "Test", "text")
        super().init(context)

    def draw_buttons(self, context, layout):
        layout.prop(self, 'row1')
        layout.prop(self, 'row2')
        layout.prop(self, 'row3')
        layout.prop(self, 'row4')

    def preExecute(self, refholder):
        new_matrix = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        
        self.matrix[0] = self.row1
        self.matrix[1] = self.row2
        self.matrix[2] = self.row3
        self.matrix[3] = self.row4
        
        for i in range (0, 4):
            for j in range (0, 4):
                new_matrix[i][j] = self.matrix[i][j]
        
        self.outputs[0].matrix_ref = refholder.getRefForMatrix(new_matrix)
        
    def execute(self, refholder):
        print('begin print matrix')        
        for i in range (0, 4):
            print_string = ""
            for j in range (0, 4):
                print_string += str(self.matrix[i][j]) + "   "
            print(print_string)