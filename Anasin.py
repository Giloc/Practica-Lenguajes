
from Analex import Token
from IfAp import ap_if, i_if
from VariableAP import ap_var, v_var
from WhileAP import ap_while, wh_while




def ExecuteAnalizer(code):
        if(code[0].value in v_var.relations.keys()):
                ap_var.grammar = code + [Token(" ", " ")]
                ap_var.current_entry = code[0]
                ap_var.stack = ap_var.init_stack
                return ap_var.Analize()
        elif(code[0].value in i_if.relations.keys()):
                ap_if.grammar = code + [Token(" ", " ")]
                ap_if.current_entry = code[0]
                ap_if.stack = ap_if.init_stack
                return ap_if.Analize()
        elif(code[0].value in wh_while.relations.keys()):
                ap_while.grammar = code + [Token(" ", " ")]
                ap_while.current_entry = code[0]
                ap_while.stack = ap_while.init_stack
                return ap_while.Analize()
