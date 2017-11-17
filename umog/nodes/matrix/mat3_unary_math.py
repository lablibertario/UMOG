from .. import UMOGNode
import bpy
import numpy as np
from numpy import linalg as la

class MatrixUnaryMathNode(UMOGNode):
    bl_idname = "umog_MatrixUnaryMathNode"
    bl_label = "UMOG Matrix Unary Math"
    bl_width_min = 200

    matrix_output_operations = bpy.props.EnumProperty(items=
                                            (('0', 'Inverse', 'inversion'),
                                            ('1', 'Transpose', 'transpose'),
                                            ),
                                            name="Matrix Output")
                                         
    float_output_operations = bpy.props.EnumProperty(items=
                                            (('0', 'Frobenius Norm', 'F-norm'),
                                            ('1', '1-Norm', '1-norm'),
                                            ('2', '2-Norm', '2-norm'),
                                            ('3', 'Inf-Norm', 'inf-norm'),
                                            ('4', 'Determinant', 'determinant'),
                                            ),
                                            name="Float Output")
    def init(self, context):
        self.outputs.new("Mat3SocketType", "Matrix Out")
        self.outputs.new("FloatSocketType", "Float Out")
        self.inputs.new("Mat3SocketType", "Matrix")
        super().init(context)

    def execute(self, refholder):
    
        input_matrix = refholder.matrices[self.inputs[0].links[0].from_socket.matrix_ref]
        answer_matrix = np.zeros(16)
        answer_float = 0.0
    
        if self.float_output_operations == '0':
            answer_float = la.norm(input_matrix, 'fro')
            
        elif self.float_output_operations == '1':
            answer_float = la.norm(input_matrix, 1)

        elif self.float_output_operations == '2':
            answer_float = la.norm(input_matrix, 2)            
        
        elif self.float_output_operations == '3':
            answer_float = la.norm(input_matrix, np.inf)
            
        elif self.float_output_operations == '4': 
            answer_float = la.det(input_matrix)
            
        if self.matrix_output_operations == '0':
            if la.det(input_matrix) == 0:
                print("Matrix has no inverse")
            else
                answer_matrix = la.inv(input_matrix)
        
        elif self.matrix_output_operations == '1':
            answer_matrix = np.transpose(input_matrix)
            
        print("FLOAT OUTPUT:")
        print(answer_float)
        print("MATRIX OUTPUT:")
        print(answer_matrix)
            
        self.outputs[0].matrix_ref = refholder.getRefForMatrix(answer_matrix) 
        self.outputs[1].value = answer_float
            
    def draw_buttons(self, context, layout):
        layout.prop(self, "matrix_output_operations", 'Matrix Out')
        layout.prop(self, "float_output_operations", 'Float Out')