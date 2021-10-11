from NT import NT, unstack_hold, unstack_next, accept
from gramaticas import AP

wh_while = NT("<While>")
con_while = NT("<Condición>")
v_while = NT("<Variable>")
ig_while = NT("<Igualdad>")
acc_while = NT("<Acceso>")
ti_while = NT("<Tipo>")
nom_while = NT("<Nombre>")
suma_while = NT("<Suma>")
rs_while = NT("<RestoSuma>")
m_while = NT("<Multiplicacion>")
rm_while = NT("<RestoMultiplicacion>")
p_while = NT("<Potenciacion>")
rp_while = NT("<RestoPotenciacion>")
parentesis_while = NT("<Parentesis>")
pal_while = NT("<Palabra>")
restop_while = NT("RestoPalabra")
st_while = NT("<String>")
cierrap_while = NT(")")
desig_while = NT("!=")
abrep_while = NT("(")
and_while = NT("&&")
abre_llave_while = NT("{")
cierra_llave_while = NT("}")
pila_vacia_while = NT("pila vacia")

wh_while.relations = {"while": ["a", con_while, abrep_while]}
con_while.relations = {"(": [cierra_llave_while, v_while, abre_llave_while, cierrap_while, pal_while, desig_while, suma_while], "Int": [cierra_llave_while, v_while, abre_llave_while, cierrap_while, pal_while, desig_while, suma_while], "Float": [cierra_llave_while, v_while, abre_llave_while, cierrap_while, pal_while, desig_while, suma_while], "String": [cierra_llave_while, suma_while, abre_llave_while, cierrap_while, v_while, and_while, pal_while]}
v_while.relations = {"private": [ig_while, nom_while, ti_while, acc_while], "public": [ig_while, nom_while, ti_while, acc_while], "int": [ig_while, nom_while, ti_while, acc_while]}
ig_while.relations = {"=": ["a", suma_while], "}": unstack_hold}
acc_while.relations = {"private": unstack_next, "public": unstack_next, "int": unstack_hold}
ti_while.relations = {"int": unstack_next}
nom_while.relations = {"Identify": unstack_next}
suma_while.relations = {"(": [rs_while, m_while], "Int": [rs_while, m_while], "Float": [rs_while, m_while]}
rs_while.relations = {"+": ["a", rs_while, m_while], "-": ["a", rs_while, m_while], ")": unstack_hold, "!=": unstack_hold, "}": unstack_hold}
m_while.relations = {"(": [rm_while, p_while], "Int": [rm_while, p_while], "Float": [rm_while, p_while]}
rm_while.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*": ["a", rm_while, p_while], "/": ["a", rm_while, p_while], "%": ["a", rm_while, p_while], "!=": unstack_hold, "}": unstack_hold}
p_while.relations = {"(": [rp_while, parentesis_while], "Int": [rp_while, parentesis_while], "Float": [rp_while, parentesis_while]}
rp_while.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*": unstack_hold, "/": unstack_hold, "%": unstack_hold, "^": ["a", rp_while, parentesis_while], "!=": unstack_hold, "}": unstack_hold}
parentesis_while.relations = {"(": ["a", cierrap_while, suma_while], "Int": unstack_next, "Float": unstack_next}
pal_while.relations = {"String": [restop_while, st_while]} 
restop_while.relations = {"+": ["a", restop_while, st_while], ")": unstack_hold, "!=": unstack_hold, "&&": unstack_hold}
st_while.relations = {"String": unstack_next}
cierrap_while.relations = {")": unstack_next}
desig_while.relations = {"!=": unstack_next}
abrep_while.relations = {"(": unstack_next}
and_while.relations = {"&&": unstack_next}
abre_llave_while.relations = {"{": unstack_next}
cierra_llave_while.relations = {"}": unstack_next}
pila_vacia_while.relations = {" ": accept}

ap_while = AP(["while", "(", "!=", ")", "{", "}", "&&", "+", "-", "*", "/", "%", "^", "Int", "Float", "String", "=", "private", "public", "int", "Identify", " "],
                [wh_while, con_while, v_while, ig_while, acc_while, ti_while, nom_while, suma_while, rs_while, m_while, rm_while, p_while, rp_while, parentesis_while, pal_while, restop_while, st_while, cierrap_while, desig_while, abrep_while, and_while, abre_llave_while, cierra_llave_while, pila_vacia_while],
                [pila_vacia_while, wh_while])