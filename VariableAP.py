from NT import NT, unstack_hold, unstack_next, accept
from gramaticas import AP

v_var = NT("<Variable>")
acc_var = NT("<Acceso>")
ti_var = NT("<Tipo>")
nom_var =  NT("<Nombre>")
ig_var = NT("<Igualdad>")
suma_var = NT("<Suma>")
rs_var = NT("<RestoSuma>")
m_var = NT("<Multiplicacion>")
rm_var = NT("<RestoMultiplicacion>")
p_var = NT("<Potenciacion>")
rp_var = NT("<RestoPotenciacion>")
parentesis_var = NT("<Parentesis>")
cierrap_var = NT(")")
pila_vacia_var = NT("pila vacia")

v_var.relations = {"private": [ig_var, nom_var, ti_var, acc_var], "public": [ig_var, nom_var, ti_var, acc_var], "int": [ig_var, nom_var, ti_var, acc_var]}
acc_var.relations = {"private": unstack_next, "public": unstack_next, "int": unstack_hold}
ti_var.relations = {"int": unstack_next}
nom_var.relations = {"Identify": unstack_next}
ig_var.relations = {"=": ["a", suma_var], " ": unstack_hold}
suma_var.relations = {"(": [rs_var, m_var], "Int": [rs_var, m_var], "Float": [rs_var, m_var]}
rs_var.relations = {"+": ["a", rs_var, m_var], "-": ["a", rs_var, m_var], ")": unstack_hold, " ": unstack_hold}
m_var.relations = {"(": [rm_var, p_var], "Int": [rm_var, p_var], "Float": [rm_var, p_var]}
rm_var.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*": ["a", rm_var, p_var], "/": ["a", rm_var, p_var], "%": ["a", rm_var, p_var], " ": unstack_hold}
p_var.relations = {"(": [rp_var, parentesis_var], "Int": [rp_var, parentesis_var], "Float": [rp_var, parentesis_var]}
rp_var.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*": unstack_hold, "/": unstack_hold, "%": unstack_hold, "^": ["a", rp_var, parentesis_var], " ": unstack_hold}
parentesis_var.relations = {"(": ["a", cierrap_var, suma_var], "Int": unstack_next, "Float": unstack_next}
cierrap_var.relations = {")": unstack_next}
pila_vacia_var.relations = {" ": accept}

ap_var = AP(["private", "public", "=", "int", "Identify" "(", "Int", "Float", "+", "-", ")", "*", "/", "%", "^", " "],
            [v_var, acc_var, ti_var, nom_var, ig_var, suma_var, rs_var, m_var, rm_var, p_var, rp_var, parentesis_var, cierrap_var, pila_vacia_var],
            [pila_vacia_var, v_var])