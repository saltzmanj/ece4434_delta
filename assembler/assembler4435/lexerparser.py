#!/usr/bin/env python3
import sys
import ply.lex as lex
import ply.yacc as yacc

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
    {'R0' : ['R0', 'RAX']},
    {'R1' : ['R1', 'RBX']},
    {'R2' : ['R2', 'RCX']},
    {'R3' : ['R3', 'RDX']},
    {'R4' : ['R4', 'RDI']},
    {'R5' : ['R5', 'RSI']},
    {'R6' : ['R6']},
    {'R7' : ['R7']},
    {'R8' : ['R8']},
    {'R9' : ['R9']},
    {'R10' : ['R10']},
    {'R11' : ['R11']},
    {'R12' : ['R12']},
    {'R13' : ['R13']},
    {'R14' : ['R14', 'RJL']},
    {'R15' : ['R15', 'RCT']},
]

register_aliases = []
for r in registers:
    for x in list(r.values()):
        register_aliases.extend(x)

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
    'CHK',
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

check_macros = [
    "INST_CHECK"
]
def throw_syntax_error(line, msg, value):
    print(bcolors.BOLD + bcolors.FAIL + "Syntax Error (line " + \
            str(line) + "): " + bcolors.ENDC + \
            str(msg)+ " "+ bcolors.BOLD +" "+str(value))   
    exit(1) 

# Lexer Definitions
# 
# These are basically a series of regexes that 'tokenize' the input: 
#   they determine what token each input is

def t_comment_eol_1(t):
    r'--[^\n]*'

def t_comment_eol_2(t):
    r';[^\n]*'

def t_comment_eol_3(t):
    r'//[^\n]*'

def t_opcode_register(t):
    r'[a-zA-Z_]+([0-9]+)?'
    if t.value.upper() in check_macros:
        t.type = 'CHK_MACRO'
        t.value = t.value.upper()
    elif t.value.upper() in opcodes:
        t.type = t.value.upper()
        t.value = t.value.upper()
    elif t.value.upper() in register_aliases:
        t.type = 'REGISTER'
        t.value = t.value.upper()
    else:
        print(bcolors.BOLD + bcolors.FAIL + "Syntax Error (line " + \
            str(t.lexer.lineno) + "): " + bcolors.ENDC + \
            "Invalid opcode or register " + bcolors.BOLD + t.value)
        exit(1)
    return t

# def t_CHK_MACRO(t):
#     r'INST_CHECK'
#     t.type = 'CHK_MACRO'
#     return t

def t_number_hex(t):
    r'(\-)?0x[0-9a-fA-F]+'
    t.type = 'NUMBER'
    t.value = int(t.value, 16)
    return t

def t_NUMBER(t):
    r'(-)?[0-9]+'
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
    print(bcolors.BOLD + bcolors.FAIL + "Syntax Error (line " + \
            str(t.lexer.lineno) + "): " + bcolors.ENDC + \
            "Invalid token " + bcolors.BOLD + t.value)
    exit(1)

########################
# Parser Definitions   #
########################

class ParseData:
    def __init__(self,op = None,a1 = None,a2 = None,a3 = None, \
            ln = None):
        self.opcode = op
        self.arg1 = a1
        self.arg2 = a2
        self.arg3 = a3
        self.lineno = ln

    def validate_range(self, argnum, min, max):
        z = [self.arg1, self.arg2, self.arg3]
        v = z[argnum - 1]
        if v < min or v > max:
            throw_syntax_error(self.lineno, "Invalid range for  " \
                "operand", v)
    def __str__(self):
       return str(encoded)


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

    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_directive_fill(p):
    'inst : FILL NUMBER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_nop(p):
    'inst : NOP'
    p[0] = [ParseData(p[1], None, None, None, p.lineno(1))]

def p_inst_ei(p):
    'inst : EI'
    p[0] = [ParseData(p[1], None, None, None, p.lineno(1))]

def p_inst_di(p):
    'inst : DI'
    p[0] = [ParseData(p[1], None, None, None, p.lineno(1))]

# TODO -- Add number range validation
def p_inst_swi(p):
    'inst : SWI NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_usr(p):
    'inst : USR'
    p[0] = [ParseData(p[1], None, None, None, p.lineno(1))]

# Add number validation
def p_inst_ld(p):
    'inst : LD REGISTER REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], p[4], p.lineno(1))]

# Add number validation
def p_inst_st(p):
    'inst : ST REGISTER REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], p[4], p.lineno(1))]

def p_inst_mov(p):
    'inst : MOV REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

# Add number validation
def p_inst_lil(p):
    'inst : LIL REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

# Add number validation
def p_inst_lih(p):
    'inst : LIH REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_add(p):
    'inst : ADD REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_adc(p):
    'inst : ADC REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sub(p):
    'inst : SUB REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sbc(p):
    'inst : SBC REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_and(p):
    'inst : AND REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_or(p):
    'inst : OR REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_xor(p):
    'inst : XOR REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_not(p):
    'inst : NOT REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sl(p):
    'inst : SL REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_srl(p):
    'inst : SRL REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_sra(p):
    'inst : SRA REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rra(p):
    'inst : RRA REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rr(p):
    'inst : RR REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_rl(p):
    'inst : RL REGISTER REGISTER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_jmp(p):
    'inst : JMP REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_jal(p):
    'inst : JAL REGISTER NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_inst_br(p):
    'inst : BR NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bc(p):
    'inst : BC NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bo(p):
    'inst : BO NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bn(p):
    'inst : BN NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_bz(p):
    'inst : BZ NUMBER'
    p[0] = [ParseData(p[1], p[2], None, None, p.lineno(1))]

def p_inst_chk(p):
    'inst : CHK CHK_MACRO NUMBER'
    p[0] = [ParseData(p[1], p[2], p[3], None, p.lineno(1))]

def p_error(p):
    print(bcolors.BOLD + bcolors.FAIL + "Syntax Error (line " + \
            str(p.lexer.lineno) + "): " + bcolors.ENDC + \
            "Invalid sequence " + bcolors.BOLD + p.value)
    exit(1)

# Helper Functions
def number_to_binary(num, length):
    if num < 0:
        return bin(num % (1<<length))[2:]
    else:
        return bin(num)[2:].rjust(length, '0')

def get_reg_id(rname):
    for r in registers:
        if rname in list(r.values())[0]:
            p = list(r.keys())[0]
            # print(p)
            return number_to_binary(int(p[1:]), 4)
    return ""
# Compilation function
#   Converts a properly parsed ParseData object into a writeable 
#   binary object


class MachineInstruction:
    encoded   = []
    word_len  = 0
    def __init__(self, en, wl):
        self.encoded = en
        self.word_len = wl

    def __str__(self):
        strout = '';
        for (ind, el) in enumerate(self.encoded):
            strout += el;
            if(ind != len(self.encoded) - 1):
                strout += "\n"
        return strout
    
    @classmethod
    def from_single(cls, en):
        encoded = [en]
        word_len = 1
        return cls(encoded, word_len)
    
    @classmethod
    def from_list(cls, ens):
        encoded = ens
        word_len = len(ens)
        return cls(encoded, word_len)

def instr_to_machine_code(inst, caddr):
    mi_ret = None

    if inst.opcode == "NOP":
        nopliteral = '0'*16
        mi_ret = MachineInstruction.from_single(nopliteral)
    
    elif inst.opcode == "EI":
        eiliteral = "0000000000001001"
        mi_ret = MachineInstruction.from_single(eiliteral)
    
    elif inst.opcode == "DI":
        diliteral = "0000000000001000"
        mi_ret = MachineInstruction.from_single(diliteral)
    
    elif inst.opcode == "SWI":
        swinum = int(inst.arg1)
        if swinum < 0 or swinum > 7:
            throw_syntax_error(inst.lineno, "Invalid SWI",inst.arg1)
        
        num_str = number_to_binary(inst.arg1, 3)
        swi = "0000000000010" + num_str
        mi_ret = MachineInstruction.from_single(swi)

    elif inst.opcode == "USR":
        # TODO: usr et al
        usr = "0000000000011000"
        mi_ret =  MachineInstruction.from_single(usr)

    elif inst.opcode == "LD":
        ldos = inst.arg3
        if ldos < 0 or ldos > 31:
            throw_syntax_error(inst.lineno, "Invalid offset", ldos)
        
        offset_bin = number_to_binary(ldos, 5)
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        ldbin = "001" + r1_bin + r2_bin + offset_bin
        mi_ret =  MachineInstruction.from_single(ldbin)
        # print(ldbin)
    elif inst.opcode == "ST":
        inst.validate_range(3, 0, 31)
        stos = inst.arg3
    
        offset_bin = number_to_binary(stos, 5)
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        stbin = "010" + r1_bin + r2_bin + offset_bin
        mi_ret =  MachineInstruction.from_single(stbin)

    elif inst.opcode == "MOV":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)
        mvbin = "011" + r1_bin + r2_bin + "00000"
        mi_ret =  MachineInstruction.from_single(mvbin)

    elif inst.opcode == "LIL":
        # inst.validate_range(2, 0, 255)
        imm_os = number_to_binary(inst.arg2, 8)
        r1_bin = get_reg_id(inst.arg1)

        lilbin = "100" + r1_bin + "0" + imm_os
        mi_ret = MachineInstruction.from_single(lilbin)
    elif inst.opcode == "LIH":
        # inst.validate_range(2, 0, 255)
        imm_os = number_to_binary(inst.arg2, 8)
        r1_bin = get_reg_id(inst.arg1)

        lilbin = "100" + r1_bin + "1" + imm_os
        mi_ret = MachineInstruction.from_single(lilbin)
    elif inst.opcode == "ADD":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00000"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "ADC":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00001"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "SUB":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00010"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "SBC":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00011"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "AND":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00100"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "OR":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00101"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "XOR":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00110"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "NOT":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "00111"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "SL":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "01000"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "SRL":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "02001"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "SRA":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "01010"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "RRA":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "01110"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "RR":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "01101"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "RL":
        r1_bin = get_reg_id(inst.arg1)
        r2_bin = get_reg_id(inst.arg2)

        arth_bin = "101" + r1_bin + r2_bin + "01100"
        mi_ret = MachineInstruction.from_single(arth_bin)
    elif inst.opcode == "JMP":
        offset_bin = number_to_binary(inst.arg2, 8)
        r1_bin = get_reg_id(inst.arg1)
        jal_bin = "110" + r1_bin + "0" + offset_bin
        mi_ret = MachineInstruction.from_single(jal_bin)

    elif inst.opcode == "JAL":
        offset_bin = number_to_binary(inst.arg2, 8)
        r1_bin = get_reg_id(inst.arg1)
        jal_bin = "110" + r1_bin + "1" + offset_bin
        mi_ret = MachineInstruction.from_single(jal_bin)

    elif inst.opcode == "BR":
        target_bin = number_to_binary(inst.arg1, 8)
        br_bin = "111" + "0000" + "0" + target_bin
        mi_ret = MachineInstruction.from_single(br_bin)

    elif inst.opcode == "BC":
        target_bin = number_to_binary(inst.arg1, 8)
        br_bin = "111" + "1000" + "0" + target_bin
        mi_ret = MachineInstruction.from_single(br_bin)

    elif inst.opcode == "BO":
        target_bin = number_to_binary(inst.arg1, 8)
        br_bin = "111" + "0100" + "0" + target_bin
        mi_ret = MachineInstruction.from_single(br_bin)

    elif inst.opcode == "BN":
        target_bin = number_to_binary(inst.arg1, 8)
        br_bin = "111" + "0010" + "0" + target_bin
        mi_ret = MachineInstruction.from_single(br_bin)

    elif inst.opcode == "BZ":
        target_bin = number_to_binary(inst.arg1, 8)
        br_bin = "111" + "0001" + "0" + target_bin
        mi_ret = MachineInstruction.from_single(br_bin)

    elif inst.opcode == "[WORD]":
        lit_str = number_to_binary(inst.arg1, 16)
        reps = int(inst.arg2)
        lit_list = [lit_str] * reps
        mi_ret = MachineInstruction.from_list(lit_list)

    elif inst.opcode == "[FILL]":
        num_to_fill = number_to_binary(inst.arg1, 16)
        fill_to = int(inst.arg2)
        if fill_to < caddr:
            throw_syntax_error(inst.lineno, "Can't [fill] in reverse"
                " direction.", inst.arg2)
        lit_list = [num_to_fill] * (fill_to - caddr)
        mi_ret = MachineInstruction.from_list(lit_list)

    elif inst.opcode == "CHK":
        offset_bin = number_to_binary(inst.arg2, 9)
        check_type = ""
        if inst.arg1 == "INST_CHECK":
            check_type = "000"
        else:
            throw_syntax_error(inst.lineno, "Invalid check type:", \
                inst.arg1)
            exit(1)
        check_bin = "000" + "1" + check_type + offset_bin
        mi_ret = MachineInstruction.from_single(check_bin)

    else:
        throw_syntax_error(inst.lineno, "Invalid opcode:", \
            inst.opcode)


    return mi_ret

# Run lexer and parser
if __name__ == "__main__":
    lexer = lex.lex()
    input_file = open(sys.argv[1], 'r')
    lexer.input(input_file.read())
    # for el in lexer:
        # print(el)
    parser = yacc.yacc()
    parser = yacc.parse(lexer=lexer)
    to_print = ""
    caddr = 0
    for expr in parser:
        result = instr_to_machine_code(expr, caddr)
        mc = result
        for i in range(0, mc.word_len):
            to_print += mc.encoded[0] + "\n"
            caddr += 1

    print(to_print[:-1])