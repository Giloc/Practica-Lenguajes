class State:

    def __init__(self, name, accept):
        self.name = name
        self.accept = accept
        self.entries = None
    
    def AssignTransitions(self, entries):
        self.entries = entries

#identify words
state_1 = State("A", False)
state_2 = State("B", True)
entry = ["a", "b", "c", "_"]
state_1.AssignTransitions({"a":state_2, "b":state_2, "c":state_2, "_":state_1})
state_2.AssignTransitions({"a":state_2, "b":state_2, "c":state_2, "_":state_2})
states = [state_1, state_2]

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
state_i_r = State("I", True)
state_j_r = State("J", False)
state_k_r = State("K", False)
state_l_r = State("L", False)
state_m_r = State("M", False)
state_n_r = State("N", False)
state_o_r = State("O", False)
state_p_r = State("P", True)
state_q_r = State("Q", False)
state_r_r = State("R", False)
state_s_r = State("S", True)
state_t_r = State("T", True)
state_u_r = State("U", False)

state_empty_r.AssignTransitions({"i":state_a_r, "w":state_b_r, "p":state_c_r})
state_a_r.AssignTransitions({"f":state_d_r, "n":state_e_r})
state_b_r.AssignTransitions({"h":state_f_r})
state_c_r.AssignTransitions({"r": state_g_r, "u":state_h_r})
state_d_r.AssignTransitions({})
state_e_r.AssignTransitions({"t":state_i_r})
state_f_r.AssignTransitions({"i":state_j_r})
state_g_r.AssignTransitions({"i":state_k_r})
state_h_r.AssignTransitions({"b":state_l_r})
state_i_r.AssignTransitions({})
state_j_r.AssignTransitions({"l":state_m_r})
state_k_r.AssignTransitions({"v":state_n_r})
state_l_r.AssignTransitions({"l":state_o_r})
state_m_r.AssignTransitions({"e":state_p_r})
state_n_r.AssignTransitions({"a":state_q_r})
state_o_r.AssignTransitions({"i":state_r_r})
state_p_r.AssignTransitions({})
state_q_r.AssignTransitions({"t":state_u_r})
state_r_r.AssignTransitions({"c":state_t_r})
state_s_r.AssignTransitions({})
state_t_r.AssignTransitions({})
state_u_r.AssignTransitions({"e":state_s_r})
states_2 = [state_empty_r, state_a_r, state_b_r, state_c_r, state_d_r, state_e_r, state_f_r, state_g_r, state_h_r, state_i_r, state_j_r, state_k_r, state_l_r, state_m_r, state_n_r, state_o_r, state_p_r, state_q_r, state_r_r, state_s_r, state_t_r, state_u_r]

entry_2 = ["i", "f", "n", "t", "w", "h", "l", "e", "p", "r", "v", "a", "u", "b", "c"]

#operator
state_empty_o = State("empty", False)
state_a_o = State("A", True)
state_b_o = State("B", True)
state_c_o = State("C", True)
state_d_o = State("D", True)
state_e_o = State("E", True)
state_f_o = State("F", True)
state_g_o = State("G", True)
state_h_o = State("H", False)
state_i_o = State("I", True)
state_j_o = State("J", True)
state_k_o = State("K", True)
state_l_o = State("L", True)
state_m_o = State("M", True)
state_n_o = State("N", True)

state_empty_o.AssignTransitions({"+":state_a_o, "-":state_b_o, "*":state_c_o, "/":state_d_o, "%":state_e_o, "=":state_f_o, "!":state_h_o, "<":state_j_o, ">":state_k_o, "^":state_n_o})
state_a_o.AssignTransitions({})
state_b_o.AssignTransitions({})
state_c_o.AssignTransitions({})
state_d_o.AssignTransitions({})
state_e_o.AssignTransitions({})
state_f_o.AssignTransitions({"=":state_g_o})
state_g_o.AssignTransitions({})
state_h_o.AssignTransitions({"=":state_i_o})
state_i_o.AssignTransitions({})
state_j_o.AssignTransitions({"=":state_l_o})
state_k_o.AssignTransitions({"=":state_m_o})
state_l_o.AssignTransitions({})
state_m_o.AssignTransitions({})
state_n_o.AssignTransitions({})

states_3 = [state_empty_o, state_a_o, state_b_o, state_c_o, state_d_o, state_e_o, state_f_o, state_g_o, state_h_o, state_i_o, state_j_o, state_k_o, state_l_o, state_m_o, state_n_o]
entry_3 = ["+", "-", "*", "/", "%", "=", "!", "<", ">", "^"]