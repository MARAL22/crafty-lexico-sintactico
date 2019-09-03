import ply.lex as lex

# resultado del analisis
resultado_lexema = []
resultado_error = []
#errores = []

reservada = (
    # Palabras Reservadas
    'CRAFTY_DATA','END_CRAFTY_DATA','CRAFTY_START','END_CRAFTY_START','CRAFTY_LIGHT','CRAFTY_WATER',
    'CRAFTY_WARM','CRAFTY_AIR','LIGHT_UP','LIGHT_DOWN','LIGHT_BLINK','SET_','TRUE',
    'FALSE','WARM_UP','WARM_DOWN','WATER_UP','WATER_DOWN','AIR_UP','AIR_DOWN','START','STOP')


tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'CADENA',
    'ASIGNAR',
    'DELAY',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
   'IF',
    'ELSE',
   'WHILE',
   'FOR',
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'PARIZQ',
    'PARDER',
    'DOSPUNTOS'
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'

t_ASIGNAR = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_DOSPUNTOS = r':'
t_PARIZQ = r'\('
t_PARDER = r'\)'



#PALABRAS RESERVADAS

def t_CRAFTY_DATA(t):
    r'CRAFTY_DATA'
    return t


def t_END_CRAFTY_DATA(t):
    r'END_CRAFTY_DATA'
    return t

def t_CRAFTY_START(t):
    r'CRAFTY_START'
    return t

def t_END_CRAFTY_START(t):
    r'END_CRAFTY_START'
    return t

def t_CRAFTY_LIGTH(t):
    r'CRAFTY_LIGHT'
    return t

def t_CRAFTY_WATER(t):
    r'CRAFTY_WATER'
    return t

def t_CRAFTY_WARM(t):
    r'CRAFTY_WARM'
    return t

def t_CRAFTY_AIR(t):
    r'CRAFTY_AIR'
    return t


def t_LIGHT_UP(t):
    r'LIGHT_UP'
    return t

def t_LIGHT_DOWN(t):
    r'LIGHT_DOWN'
    return t

def t_LIGHT_BLINK(t):
    r'LIGHT_BLINK'
    return t
def t_AIR_UP(t):
    r'AIR_UP'
    return t

def t_AIR_DOWN(t):
    r'AIR_DOWN'

def t_SET_(t):
    r'SET_'
    return t


def t_TRUE(t):
    r'TRUE'
    return t

def t_START(t):
    r'START'
    return t

def t_STOP(t):
    r'STOP'
    return t


#END PALABRAS RES

def t_DELAY(t):
    r'DELAY'
    return t
def t_ELSE(t):
    r'ELSE'
    return t

def t_IF(t):
    r'IF'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_FOR(t):
    r'FOR'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'CI+\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'"+\"?(\w+ \ *\w*\d* \ *)\"?"'
   return t


def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t



def t_DISTINTO(t):
    r'@='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global errores
    estado = "** Token no valido en la Linea {:4} Componente Lexico {:16}".format(str(t.lineno), str(t.value))
    resultado_error.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Token {:16} Componente Lexico {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

def errorLexico(data):
    #global resultado_lexema
    global resultado_error

    analizador = lex.lex()
    analizador.input(data)

    resultado_error.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
    return resultado_error

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)