#!/usr/bin/env python3
import ply.yacc as yacc
import ply.lex as lex
import sys

###############################
# LEXER definitions
###############################
opcodes = [
    'NOP',
    'EI',
    'DI',
    'SWI',
    'USR',
    'LD',
    'ST',
    'MOV',
    'LIL',
    'LIH',
    'ADD',
    'ADC',
    'SUB',
    'SBC',
    'AND',
    'OR',
    'XOR',
    'NOT',
    'SL',
    'SRL',
    'SRA',
    'RRA',
    'RR',
    'RL',
    'JMP',
    'JAL',
    'BR',
    'BC',
    'BO',
    'BN',
    'BZ',
    '[WORD]',
    '[FILL]',
    'CHK'
]

registers = [
    'R0',
    'R1',
    'R2',
    'R3',
    'R4',
    'R5',
    'R6',
    'R7',
    'R8',
    'R9',
    'R10',
    'R11',
    'R12',
    'R13',
    'R14',
    'R15',
]

tokens = (
    'NOP',
    'EI',
    'DI',
    'SWI',
    'USR',
    'LD',
    'ST',
    'MOV',
    'LIL',
    'LIH',
    'ADD',
    'ADC',
    'SUB',
    'SBC',
    'AND',
    'OR',
    'XOR',
    'NOT',
    'SL',
    'SRL',
    'SRA',
    'RRA',
    'RR',
    'RL',
    'JMP',
    'JAL',
    'BR',
    'BC',
    'BO',
    'BN',
    'BZ',
    'REGISTER',
    'NUMBER',
    'WORD',
    'FILL',
    'CHK_MACRO',
)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def t_CHK_MACRO(t):
    r'INST_CHECK'

def t_comment_eol_1(t):
    r'--[^\n]*'

def t_comment_eol_2(t):
    r';[^\n]*'

def t_comment_eol_3(t):
    r'//[^\n]*'

def t_opcode_register(t):
    r'[a-zA-Z]+([0-9]+)?'
    if t.value.upper() in opcodes:
        t.type = t.value.upper()
        t.value = t.value.upper()
    elif t.value.upper() in register_aliases:
        t.type = 'REGISTER'
        t.value = t.value.upper()
    else:
        print(bcolors.FAIL + "Syntax Error (line " + \
            str(t.lexer.lineno)+ "): " + bcolors.ENDC + \
            "Invalid opcode " + bcolors.BOLD + t.value)
        exit(1)
    return t


def t_number_hex(t):
    r'(\-)?0x[0-9a-fA-F]+'
    t.type = 'NUMBER'
    t.value = int(t.value, 16)
    return t

def t_NUMBER(t):
    r'(\-)?[0-9]+'
    t.value = int(t.value)
    return t

def t_WORD(t):
    r'(?i)\[WORD\]'
    t.value = t.value.upper()
    return t

def t_FILL(t):
    r'(?i)\[FILL]'
    t.value = t.value.upper()
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t,'
def t_error(t):
    print("LINE: " + str(t.lexer.lineno) + " Illegal token '" + str(t.value[0])+ "'")
    exit(1)

###############################
# Parser Definitions
###############################

def p_program(p):
    'program : inst instlist'
    p[0] = p[1] + p[2]

def p_instlist_inst(p):
    'instlist : inst instlist'
    p[0] = p[1] + p[2]

def p_instlist_empty(p):
    'instlist : '
    p[0] = []

def p_directive_word(p):
    'inst : WORD NUMBER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_directive_fill(p):
    'inst : FILL NUMBER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_nop(p):
    'inst : NOP'
    p[0] = [(p[1], None, None, None, p.lineno(1))]

def p_inst_ei(p):
    'inst : EI'
    p[0] = [(p[1], None, None, None, p.lineno(1))]

def p_inst_di(p):
    'inst : DI'
    p[0] = [(p[1], None, None, None, p.lineno(1))]

# TODO -- Add number range validation
def p_inst_swi(p):
    'inst : SWI NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

def p_inst_usr(p):
    'inst : USR'
    p[0] = [(p[1], None, None, None, p.lineno(1))]

# Add number validation
def p_inst_ld(p):
    'inst : LD REGISTER REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], p[4], p.lineno(1))]

# Add number validation
def p_inst_st(p):
    'inst : ST REGISTER REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], p[4], p.lineno(1))]

def p_inst_mov(p):
    'inst : MOV REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

# Add number validation
def p_inst_lil(p):
    'inst : LIL REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

# Add number validation
def p_inst_lih(p):
    'inst : LIH REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_add(p):
    'inst : ADD REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_adc(p):
    'inst : ADC REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sub(p):
    'inst : SUB REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sbc(p):
    'inst : SBC REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_and(p):
    'inst : AND REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_or(p):
    'inst : OR REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_xor(p):
    'inst : XOR REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_not(p):
    'inst : NOT REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sl(p):
    'inst : SL REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_srl(p):
    'inst : SRL REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sra(p):
    'inst : SRA REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rra(p):
    'inst : RRA REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rr(p):
    'inst : RR REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rl(p):
    'inst : RL REGISTER REGISTER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_jmp(p):
    'inst : JMP REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_jal(p):
    'inst : JAL REGISTER NUMBER'
    p[0] = [(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_br(p):
    'inst : BR NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bc(p):
    'inst : BC NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bo(p):
    'inst : BO NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bn(p):
    'inst : BN NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bz(p):
    'inst : BZ NUMBER'
    p[0] = [(p[1], p[2], None, None, p.lineno(1))]

# Error rule for syntax errors
def p_error(p):
    print("LINE: " + str(p.lineno) + " Syntax error on token: " + str(p.value))
    exit(1)

###############################
# Function for converting an instruction to a string
###############################

def number_to_binary(num, length):
    if num < 0:
        return bin(num % (1<<length))[2:]
    else:
        return bin(num)[2:].rjust(length, '0')

def inst_to_binary(inst, caddr):
    opcode, p1, p2, p3, lineno = inst
    if opcode == "NOP":
        return ["0000000000000000", 1]
    elif opcode == "EI":
        return ["0000000000001001", 1]
    elif opcode == "DI":
        return ["0000000000001000", 1]
    elif opcode == "SWI":
        if int(p1) < 0 or int(p1) > 7:
            print("LINE: " + str(lineno) + " Invalid Integer");
            exit(1)

        num_str = number_to_binary(p1, 3)

        return ["0000000000010" + num_str, 1]
    elif opcode == "USR":
        return ["0000000000011000", 1]
    elif opcode == "LD":
        if int(p3) < 0 or int(p3) > 31:
            print("LINE: " + str(lineno) + " Invalid Integer");
            exit(1)

        num_str = number_to_binary(p3, 5)

        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["001" + r1 + r2 + num_str, 1]
    elif opcode == "ST":
        if int(p3) < 0 or int(p3) > 31:
            print("LINE: " + str(lineno) + " Invalid Integer");
            exit(1)

        num_str = number_to_binary(p3, 5)

        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["010" + r1 + r2 + num_str, 1]

    elif opcode == "MOV":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["011" + r1 + r2 + "00000", 1]

    elif opcode == "LIL":
        if int(p2) < -128 or int(p2) > 127:
            print("LINE: " + str(lineno) + " Invalid Integer");
            exit(1)

        num_str = number_to_binary(p2, 8)

        r1 = number_to_binary(int(p1[1:]), 4)

        return ["100" + r1 + "0" + num_str, 1]

    elif opcode == "LIH":
        if int(p2) < -128 or int(p2) > 127:
            print("LINE: " + str(lineno) + " Invalid Integer");
            exit(1)

        num_str = number_to_binary(p2, 8)

        r1 = number_to_binary(int(p1[1:]), 4)

        return ["100" + r1 + "1" + num_str, 1]
    elif opcode == "ADD":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00000", 1]

    elif opcode == "ADC":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00001", 1]

    elif opcode == "SUB":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00010", 1]

    elif opcode == "SBC":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00011", 1]

    elif opcode == "AND":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return "101" + r1 + r2 + "00100"

    elif opcode == "OR":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00101", 1]

    elif opcode == "XOR":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00110", 1]
    elif opcode == "NOT":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "00111", 1]

    elif opcode == "SL":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01000", 1]

    elif opcode == "SRL":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01001", 1]

    elif opcode == "SRA":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01010", 1]

    elif opcode == "RRA":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01110", 1]

    elif opcode == "RR":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01101", 1]

    elif opcode == "RL":
        r1 = number_to_binary(int(p1[1:]), 4)
        r2 = number_to_binary(int(p2[1:]), 4)

        return ["101" + r1 + r2 + "01100", 1]

    elif opcode == "JMP":
        if p2 < -128 or p2 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p2, 8)

        r1 = number_to_binary(int(p1[1:]), 4)

        return ["110" + r1 + "0" + num_str, 1]

    elif opcode == "JAL":
        if p2 < -128 or p2 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p2, 8)

        r1 = number_to_binary(int(p1[1:]), 4)

        return ["110" + r1 + "1" + num_str, 1]

    elif opcode == "BR":
        if p1 < -128 or p1 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p1, 8)

        return ["111" + "0000" + "0" + num_str, 1]

    elif opcode == "BC":
        if p1 < -128 or p1 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p1, 8)

        return ["111" + "1000" + "0" + num_str,1]

    elif opcode == "BO":
        if p1 < -128 or p1 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p1, 8)

        return ["111" + "0100" + "0" + num_str, 1]
    elif opcode == "BN":
        if p1 < -128 or p1 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p1, 8)
        # print (inst)

        return ["111" + "0010" + "0" + num_str, 1]

    elif opcode == "BZ":
        if p1 < -128 or p1 > 127:
            print("LINE: " + str(lineno)) + " Invalid Integer";
            exit(1)

        num_str = number_to_binary(p1, 8)

        return ["111" + "0001" + "0" + num_str, 1]
    elif opcode == "[WORD]":
        num_str = number_to_binary(p1, 16);
        reps = int(p2)
        ret_str = "";
        for i in range(0, reps):
            ret_str += num_str
            if(i != reps-1):
                ret_str += "\n"
        return [ret_str, 1]

    elif opcode == "[FILL]":
        num_to_fill = number_to_binary(p1, 16);
        fill_to = int(p2)
        if fill_to < caddr:
            print("LINE: " + str(lineno) + " can't fill to an address less or equal to than the current address")
            exit(1)
        ret_str = ""
        for i in range(caddr+1, fill_to+1):
            ret_str += num_to_fill
            if (i != fill_to):
                ret_str += "\n"
        return [ret_str, (fill_to + 1 - caddr - 1)]

    else:
        print("DIDN'T DEAL WITH " + opcode)
        exit(1)


###############################
# Runs lexer and parser
###############################

lexer = lex.lex()
input_file = open(sys.argv[1], 'r')

lexer.input(input_file.read())

parser = yacc.yacc()
parser = yacc.parse(lexer=lexer)

to_print = ""
caddr = 0
for expr in parser:
    result = inst_to_binary(expr, caddr)
    to_print += result[0] + "\n"
    caddr += result[1]

to_print = to_print[:-1]
# Prints out the reserved memory locations
# for i in range(8):
    # print("0000000000001000")

# Prints out the binary form of the instructions
print (to_print)