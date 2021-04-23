import string
class State:

    def __init__(self, name, accept):
        self.name = name
        self.accept = accept
        self.entries = {}
    
    def AssignTransitions(self, entries):
        self.entries = entries

    def FillDict(self, chars, state, exceptions = ""):
        dic = {}
        for i in range(len(chars)):
            if(chars[i] not in exceptions):
                dic[chars[i]] = state
        self.entries.update(dic)
        return dic

#identify words
state_empty_id = State("empty", False)
state_a_id = State("A", False)
state_b_id = State("B", True)
state_c_id = State("C", False)

state_empty_id.AssignTransitions({"_": state_a_id})
state_empty_id.FillDict(string.ascii_letters, state_b_id)
state_a_id.AssignTransitions({})
state_a_id.FillDict(string.ascii_letters, state_b_id)
state_b_id.AssignTransitions({"_":state_c_id})
state_b_id.FillDict(string.ascii_letters + string.digits, state_b_id)
state_c_id.AssignTransitions({})
state_c_id.FillDict(string.ascii_letters + string.digits, state_b_id)

states_1 = [state_empty_id, state_a_id, state_b_id, state_c_id]
entry_1 = string.digits + string.ascii_letters + "_"

#Reserved words
state_empty_r = State("empty", False)
state_a_r = State("A", False)
state_b_r = State("B", False)
state_c_r = State("C", False)
state_d_r = State("D", True)
state_e_r = State("E", False)
state_f_r = State("F", False)
state_g_r = State("G", False)
state_h_r = State("H", False)
state_j_r = State("J", False)
state_k_r = State("K", False)
state_l_r = State("L", False)
state_m_r = State("M", False)
state_n_r = State("N", False)
state_o_r = State("O", False)
state_q_r = State("Q", False)
state_r_r = State("R", False)

state_empty_r.AssignTransitions({"i":state_a_r, "w":state_b_r, "p":state_c_r})
state_a_r.AssignTransitions({"f":state_d_r, "n":state_e_r})
state_b_r.AssignTransitions({"h":state_f_r})
state_c_r.AssignTransitions({"r": state_g_r, "u":state_h_r})
state_d_r.AssignTransitions({})
state_e_r.AssignTransitions({"t":state_d_r})
state_f_r.AssignTransitions({"i":state_j_r})
state_g_r.AssignTransitions({"i":state_k_r})
state_h_r.AssignTransitions({"b":state_l_r})
state_j_r.AssignTransitions({"l":state_m_r})
state_k_r.AssignTransitions({"v":state_n_r})
state_l_r.AssignTransitions({"l":state_o_r})
state_m_r.AssignTransitions({"e":state_d_r})
state_n_r.AssignTransitions({"a":state_q_r})
state_o_r.AssignTransitions({"i":state_r_r})
state_q_r.AssignTransitions({"t":state_m_r})
state_r_r.AssignTransitions({"c":state_d_r})
states_2 = [state_empty_r, state_a_r, state_b_r, state_c_r, state_d_r, state_e_r, state_f_r, state_g_r, state_h_r, state_j_r, state_k_r, state_l_r, state_m_r, state_n_r, state_o_r, state_q_r, state_r_r]

entry_2 = ["i", "f", "n", "t", "w", "h", "l", "e", "p", "r", "v", "a", "u", "b", "c"]

#operator
state_empty_o = State("empty", False)
state_a_o = State("A", True)
state_b_o = State("B", False)
state_c_o = State("C", True)


state_empty_o.AssignTransitions({"+":state_a_o, "-":state_a_o, "*":state_a_o, "/":state_a_o, "%":state_a_o, "=":state_c_o, "!":state_b_o, "<":state_c_o, ">":state_c_o, "^":state_a_o})
state_a_o.AssignTransitions({})
state_b_o.AssignTransitions({"=":state_a_o})
state_c_o.AssignTransitions({"=":state_b_o})

states_3 = [state_empty_o, state_a_o, state_b_o, state_c_o]
entry_3 = ["+", "-", "*", "/", "%", "=", "!", "<", ">", "^"]

#int
state_empty_i = State("empty", False)
state_a_i = State("A", False)
state_c_i = State("C", True)

state_empty_i.AssignTransitions({"+":state_a_i, "-":state_a_i, "0":state_c_i, "1":state_c_i, "2":state_c_i, "3":state_c_i,
                                    "4":state_c_i, "5":state_c_i, "6":state_c_i, "7":state_c_i, "8":state_c_i, "9":state_c_i})
state_a_i.AssignTransitions({"0":state_c_i, "1":state_c_i, "2":state_c_i, "3":state_c_i, "4":state_c_i, 
                            "5":state_c_i, "6":state_c_i, "7":state_c_i, "8":state_c_i, "9":state_c_i})
state_c_i.AssignTransitions({"0":state_c_i, "1":state_c_i, "2":state_c_i, "3":state_c_i, "4":state_c_i, 
                            "5":state_c_i, "6":state_c_i, "7":state_c_i, "8":state_c_i, "9":state_c_i})

states_4 = [state_empty_i, state_a_i, state_c_i]
entry_4 = ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#float
state_empty_f = State("Empty", False)
state_a_f = State("A", False)
state_b_f = State("B", False)
state_c_f = State("C", False)
state_d_f = State("D", True)

state_empty_f.AssignTransitions({"+":state_a_f, "-":state_a_f, ".":state_b_f, "0":state_c_f, "1":state_c_f, "2":state_c_f, "3":state_c_f,
                                    "4":state_c_f, "5":state_c_f, "6":state_c_f, "7":state_c_f, "8":state_c_f, "9":state_c_f})
state_a_f.AssignTransitions({".":state_b_f, "0":state_c_f, "1":state_c_f, "2":state_c_f, "3":state_c_f,
                                    "4":state_c_f, "5":state_c_f, "6":state_c_f, "7":state_c_f, "8":state_c_f, "9":state_c_f})
state_b_f.AssignTransitions({"0":state_d_f, "1":state_d_f, "2":state_d_f, "3":state_d_f, "4":state_d_f, 
                            "5":state_d_f, "6":state_d_f, "7":state_d_f, "8":state_d_f, "9":state_d_f})
state_c_f.AssignTransitions({".":state_d_f, "0":state_c_f, "1":state_c_f, "2":state_c_f, "3":state_c_f,
                                    "4":state_c_f, "5":state_c_f, "6":state_c_f, "7":state_c_f, "8":state_c_f, "9":state_c_f})                                                                                       
state_d_f.AssignTransitions({"0":state_d_f, "1":state_d_f, "2":state_d_f, "3":state_d_f, "4":state_d_f, 
                            "5":state_d_f, "6":state_d_f, "7":state_d_f, "8":state_d_f, "9":state_d_f})

states_5 = [state_empty_f, state_a_f, state_b_f, state_c_f, state_d_f]
entry_5 = ["+", "-", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#string
state_empty_s = State("Empty", False)
state_a_s = State("A", False)
state_b_s = State("B", False)
state_e_s = State("E", True)

state_empty_s.AssignTransitions({'"':state_a_s, "'":state_b_s})
state_a_s.AssignTransitions({'"':state_e_s})
state_a_s.FillDict(string.printable, state_a_s, '"')
state_b_s.AssignTransitions({"'":state_e_s})
state_b_s.FillDict(string.printable, state_b_s, "'")

states_6 = [state_empty_s, state_a_s, state_b_s, state_e_s]
entry_6 = string.printable

#separator
state_empty_sep = State("Empty", False)
state_a_sep = State("A", True)
state_b_sep = State("B", True)
state_c_sep = State("C", True)
state_d_sep = State("D", True)
state_e_sep = State("E", True)

state_empty_sep.AssignTransitions({";":state_a_sep, "(":state_b_sep, ")":state_c_sep, "{":state_d_sep, "}":state_e_sep})
state_a_sep.AssignTransitions({})
state_b_sep.AssignTransitions({})
state_c_sep.AssignTransitions({})
state_d_sep.AssignTransitions({})
state_e_sep.AssignTransitions({})

states_7 = [state_empty_sep, state_a_sep, state_b_sep, state_c_sep, state_d_sep, state_e_sep]
entrry_7 = [";", "(", ")", "{", "}"]