import ply.yacc as yacc
from lexico import tokens
from lexico import analizador

resultado_gramatica = []

precedence = (
	('left','CRAFTY_DATA', 'CRAFTY_START', 'IF', 'FOR', 'WHILE', 'START','STOP', 'CRAFTY_LIGHT','CRAFTY_WATER',
    'CRAFTY_WARM','CRAFTY_AIR','LIGHT_UP','LIGHT_DOWN','LIGHT_BLINK','SET_','TRUE','FALSE'),
    ('right', 'END_CRAFTY_DATA', 'END_CRAFTY_START'),
	('right', 'ASIGNAR', 'ENTERO'),
	('right', 'SUMA', 'RESTA'),
	('right', 'MULT', 'DIV'),
	('rigth','IDENTIFICADOR'),
	('left', 'PARIZQ'))
	

def p_program_data(p):
	'''program : data'''
	p[0] = p[1]

def p_program_code(p):
	'''program : code'''
	p[0] = p[1]
	

def p_data(p):
	'''data : CRAFTY_DATA declaracion'''
	p[0] = p[2]

def p_declaracion_entero(p):
	'''declaracion : IDENTIFICADOR ASIGNAR ENTERO'''
	p[0] = [3]
	
def p_declaracion_cadena(p):
	'''declaracion : IDENTIFICADOR ASIGNAR CADENA'''
	p[0] = [3]
	
def p_declaracion_exp(p):
	'''declaracion : expresion'''
	print ("exp 1")

def p_expresion_entero(p):
	'''expresion : ENTERO'''
	print ("exp 2")

def p_expresion_cadena(p):
	'''expresion : CADENA'''
	print ("exp 2")

def p_expresion_op_a(p):
	'''expresion : expresion op_a expresion'''
	print ("exp 3")

def p_expresion_parentesis(p):
	'''expresion : PARIZQ expresion PARDER'''
	print ("exp 4")

def p_op_a_suma(p):
	'''op_a : SUMA'''
	print ("op_a 1")

def p_op_a_resta(p):
	'''op_a : RESTA'''
	print ("op_a 2")

def p_op_a_mult(p):
	'''op_a : MULT'''
	print ("op_a 3")

def p_op_a_div(p):
	'''op_a : DIV'''
	print ("op_a 4")

def p_code(p):
	'''code : CRAFTY_START'''
	print ("code")

def p_bloque_star(p):
	'''bloque : elements PARIZQ START PARDER DOSPUNTOS'''
	print ("bloque 1")

def p_bloque_stop(p):
	'''bloque : elements PARIZQ STOP PARDER DOSPUNTOS'''
	print ("bloque 2")

def p_elemets_1(p):
	'''elements : CRAFTY_LIGHT'''
	print ("elements 1")

def p_elemets_2(p):
	'''elements : CRAFTY_WATER'''
	print ("elements 2")

def p_elemets_3(p):
	'''elements : CRAFTY_WARM'''
	print ("elements 3")

def p_elemets_4(p):
	'''elements : CRAFTY_AIR'''
	print ("elements 4")

def p_cuerpo_1(p):
	'''cuerpo : sent'''
	print ("cuerpo 1") 

def p_cuerpo_2(p):
	'''cuerpo : sentencias'''
	print ("cuerpo 2")

def p_sentencias(p):
	'''sentencias : sent'''
	print ("sentencias 1")

# def p_sentencias2(p):
# 	'''sentencias : sent sentencias'''
# 	print ("sentencias 2")	

def p_sent_1(p):
	'''sent : declaracion'''
	print ("sent 1")

def p_sent_2(p):
	'''sent : bloque'''
	print ("sent 2")

def p_sent_3(p):
	'''sent : ciclos'''
	print ("sent 3")

def p_sent_4(p):
	'''sent : establecer'''
	print ("sent 4")

def p_establecer_1(p):
	'''establecer : IDENTIFICADOR SET_ listaset'''
	print ("establecer")

def p_establecer_2(p):
	'''establecer : IDENTIFICADOR SET_ DELAY ENTERO'''
	print ("establecer2")

def p_establecer_3(p):
	'''establecer : IDENTIFICADOR SET_ LIGHT_BLINK ENTERO'''
	print ("establecer3")


def p_listaset_1(p):
	'''listaset : AIR_DOWN'''
	print ("listaset1")

def p_listaset_2(p):
	'''listaset : AIR_UP'''
	print ("listaset2")

def p_listaset_3(p):
	'''listaset : LIGHT_DOWN'''
	print ("listaset3")

def p_listaset_4(p):
	'''listaset : LIGHT_UP'''
	print ("listaset4")

def p_listaset_5(p):
	'''listaset : WARM_DOWN'''
	print ("listaset5")

def p_listaset_6(p):
	'''listaset : WARM_UP'''
	print ("listaset6")		

def p_listaset_7(p):
	'''listaset : WATER_DOWN'''
	print ("listaset7")

def p_listaset_8(p):
	'''listaset : WATER_UP'''
	print ("listaset8")	

def p_listaset_9(p):
	'''listaset : TRUE'''
	print ("listaset9")

def p_listaset_10(p):
	'''listaset : FALSE'''
	print ("listaset10")	

def p_ciclos_1(p):
	'''ciclos : cicloif'''
	print("ciclos 1")


def p_ciclos_2(p):
	'''ciclos : ciclofor'''
	print("ciclos 2")

def p_ciclos_3(p):
	'''ciclos : ciclowhile'''
	print("ciclos 3")

def p_cicloif_1(p):
	'''cicloif : IF PARIZQ cond PARDER DOSPUNTOS cuerpo'''
	print ("ciclo_if 1")

def p_ciclo_if_2(p):
	'''cicloif : IF PARIZQ cond PARDER DOSPUNTOS cuerpo ELSE DOSPUNTOS cuerpo'''
	print ("ciclo_if 2")

def p_cond_1(p):
	'''cond : DISTINTO cond'''
	print ("cond 1") 

def p_cond_2(p):
	'''cond : cond op_log cond'''
	print ("cond 2") 
	
def p_cond_3(p):
	'''cond : expresion op_rel expresion'''
	print ("cond 3")

def p_op_log_1(p):
	'''op_log : AND'''
	print ("cond 1") 

def p_op_log_2(p):
	'''op_log : OR'''
	print ("cond 2")

def p_op_rel_1(p):
	'''op_rel : MAYORQUE'''
	print ("op_rel 1")

def p_op_rel_2(p):
	'''op_rel : MENORQUE'''
	print ("op_rel 2")

def p_op_rel_3(p):
	'''op_rel : MAYORIGUAL'''
	print ("op_rel 3")

def p_op_rel_4(p):
	'''op_rel : MENORIGUAL'''
	print ("op_rel 4")

def p_op_rel_5(p):
	'''op_rel : IGUAL'''
	print ("op_rel 5")

def p_op_rel_6(p):
	'''op_rel : DISTINTO'''
	print ("op_rel 6")


def p_ciclofor(p):
	'''ciclofor : FOR PARIZQ cond PARDER DOSPUNTOS cuerpo'''
	print ("ciclo_for")

def p_ciclowhile(p):
	'''ciclowhile : WHILE PARIZQ cond PARDER DOSPUNTOS cuerpo'''
	print ("ciclo_while")

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {} en la linea {}".format( str(t.type),str(t.value),str(t.lineno))
        resultado_gramatica.append(resultado)
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        resultado_gramatica.append(resultado)
        print(resultado)
    



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

# if __name__ == '__main__':
#     while True:
#         try:
#             s = input(' ingresa dato >>> ')
#         except EOFError:
#             continue
#         if not s: continue

#         # gram = parser.parse(s)
#         # print("Resultado ", gram)

#         prueba_sintactica(s)
















