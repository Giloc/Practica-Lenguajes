from NT import NT, unstack_hold, unstack_next, accept
from gramaticas import AP

i_if = NT("<If>")
con_if = NT("<Condición>")
cu_if = NT("<Cuerpo>")
v_if = NT("<Variable>")
ig_if = NT("<Igualdad>")
acc_if = NT("<Acceso>")
ti_if = NT("<Tipo>")
nom_if = NT("<Nombre>")
suma_if = NT("<Suma>")
rs_if = NT("<RestoSuma>")
m_if = NT("<Multiplicacion>")
rm_if = NT("<RestoMultiplicacion>")
p_if = NT("<Potenciacion>")
rp_if = NT("<RestoPotenciacion>")
parentesis_if = NT("<Parentesis>")
pal_if = NT("<Palabra>")
restop_if = NT("RestoPalabra")
st_if = NT("<String>")
cierrap_if = NT(")")
doble_igual_if = NT("==")
abrep_if = NT("(")
abre_llave_if = NT("{")
cierra_llave_if = NT("}")
pila_vacia_if = NT("pila vacia")


#Relaciones para declaración de variables
i_if.relations = {"if": ["a", con_if, abrep_if]}
con_if.relations = {"(": [cu_if, abre_llave_if, cierrap_if, suma_if, doble_igual_if, suma_if], "Int": [cu_if, abre_llave_if, cierrap_if, suma_if, doble_igual_if, suma_if], "Float": [cu_if, abre_llave_if, cierrap_if, suma_if, doble_igual_if, suma_if], "String": [cu_if, abre_llave_if, cierrap_if, pal_if, doble_igual_if, pal_if]}
cu_if.relations = {"private": [cierra_llave_if, v_if], "public": [cierra_llave_if, v_if], "int": [cierra_llave_if, v_if], "}": unstack_next}
v_if.relations = {"private": [ig_if, nom_if, ti_if, acc_if], "public": [ig_if, nom_if, ti_if, acc_if], "int": [cierra_llave_if, v_if]}
acc_if.relations = {"private": unstack_next, "public": unstack_next, "int": unstack_hold}
ti_if.relations = {"int": unstack_next}
nom_if.relations = {"Identify": unstack_next}
ig_if.relations = {"=": ["a", suma_if], "}": unstack_next}
suma_if.relations = {"(": [rs_if, m_if], "Int": [rs_if, m_if], "Float":[rs_if, m_if]}
rs_if.relations = {"+": ["a", rs_if, m_if], "-": ["a", rs_if, m_if], "==": unstack_hold, "}": unstack_hold, ")": unstack_hold}
m_if.relations = {"(": [rm_if, p_if], "Int": [rm_if, p_if], "Float": [rm_if, p_if]}
rm_if.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*": ["a", rm_if, p_if], "/": ["a", rm_if, p_if], "%": ["a", rm_if, p_if], "==": unstack_hold, "}": unstack_hold}
p_if.relations = {"(": [rp_if, parentesis_if], "Int": [rp_if, parentesis_if], "Float": [rp_if, parentesis_if]}
rp_if.relations = {"+": unstack_hold, "-": unstack_hold, ")": unstack_hold, "*":unstack_hold, "/": unstack_hold, "%": unstack_hold, "^": ["a", rp_if, parentesis_if], "==": unstack_hold, "}": unstack_hold}
parentesis_if.relations = {"(": ["a", cierrap_if, suma_if], "Int": unstack_next, "Float": unstack_next}
pal_if.relations = {"String": [restop_if, st_if]}
restop_if.relations = {"+": ["a", restop_if, st_if], "==": unstack_hold, ")": unstack_hold}
st_if.relations = {"String": unstack_next}
cierrap_if.relations = {")": unstack_next}
doble_igual_if.relations = {"==": unstack_next}
abrep_if.relations = {"(": unstack_next}
abre_llave_if.relations = {"{": unstack_next}
cierra_llave_if.relations = {"}": unstack_next}
pila_vacia_if.relations = {" ": accept}

ap_if = AP(["private", "public", "=", "int", "Identify" "(", "Int", "Float", "+", "-", ")", "*", "/", "%", "^", "String", "if", "==", "{", "}", " "],
        [v_if, ig_if, acc_if, ti_if, nom_if, suma_if, rs_if, m_if, rm_if, p_if, rp_if, parentesis_if, cierrap_if, i_if, con_if, cu_if, pal_if, restop_if, st_if, doble_igual_if, abrep_if, abre_llave_if, cierra_llave_if, pila_vacia_if],
        [pila_vacia_if, i_if])