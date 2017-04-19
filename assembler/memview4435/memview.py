#!/usr/bin/env python3
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[37m'
    NORMAL = '\033[39m'


def RegNumToSymbol(rnum, no_alias = False):
	a = 1;
	if no_alias:
		a = 0

	if rnum == "0000":
		return ("r0","rax")[a]
	elif rnum == "0001":
		return ("r1","rbx")[a]
	elif rnum == "0010":
		return ("r2","rcx")[a]
	elif rnum == "0011":
		return ("r3","rdx")[a]
	elif rnum == "0100":
		return ("r4","rdi")[a]
	elif rnum == "0101":
		return ("r5","rsi")[a]
	elif rnum == "0110":
		return "r6"
	elif rnum == "0111":
		return "r7"
	elif rnum == "1000":
		return "r8"
	elif rnum == "1001":
		return "r9"
	elif rnum == "1010":
		return "r10"
	elif rnum == "1011":
		return "r11"
	elif rnum == "1100":
		return "r12"
	elif rnum == "1101":
		return "r13"
	elif rnum == "1110":
		return ("r14","rjl")[a]
	elif rnum == "1111":
		return ("r15","rct")[a]	

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def BinToHexStr(binstr, signed = False):
	if signed:
		out = twos_comp(int(binstr,2), len(binstr))
		return str(out)
	else:
		return str(hex(int(binstr, 2)))

def CalculateBranchAddress(caddr, offset):
	addrint = int(caddr, 16)
	target = addrint + int(offset);
	return "0x%0.4X" % target 

def Dissassemble(hexstr, addr):
	binstr = bin(int(hexstr, 16))[2:]
	if len(binstr) < 16:
		binstr = "0"*(16-len(binstr)) + binstr
	retstr = ""
	# print(binstr)
	if addr == "0x0000":
		retstr += "(JMP " + hexstr + ")"
	elif binstr[0:3] == "000":
		if binstr[4] == "1":
			retstr += "CHK\t"
			if binstr[5:8] == "000":
				retstr += "INST_CHECK" + BinToHexStr(binstr[8:])
		elif binstr[11:13] == "01" and binstr[15] == "1":
			retstr += "EI\t"
		elif binstr[11:13] == "01" and binstr[15] == "0":
			retstr += "DI\t"
		elif binstr[11:13] == "10":
			retstr += "SWI \t" + BinToHexStr(binstr[13:]) 
		else:
			retstr += ""
	elif binstr[0:3] == "001":
		r1 = RegNumToSymbol(binstr[3:7])
		r2 = RegNumToSymbol(binstr[7:11])
		os = BinToHexStr(binstr[10:])
		retstr += "LD \t{}, {}, {}".format(r1, r2, os)
	elif binstr[0:3] == "010":
		r1 = RegNumToSymbol(binstr[3:7])
		r2 = RegNumToSymbol(binstr[7:11])
		os = BinToHexStr(binstr[10:])
		retstr += "ST \t{}, {}, {}".format(r1, r2, os)
	elif binstr[0:3] == "011":
		r1 = RegNumToSymbol(binstr[3:7])
		r2 = RegNumToSymbol(binstr[7:11])
		retstr += "MOV \t{}, {}".format(r1, r2)
	elif binstr[0:3] == "100":
		if binstr[7] == "0":
			inst = "LIL"
		elif binstr[7] == "1":
			inst = "LIH"

		r1 = RegNumToSymbol(binstr[3:7])
		sv = BinToHexStr(binstr[8:])
		retstr += "{} \t{}, {}".format(inst, r1, sv)
	elif binstr[0:3] == "101":
		op = ""
		if binstr[12:] == "0000":
			op = "ADD"
		elif binstr[12:] == "0001":
			op = "ADC"
		elif binstr[12:] == "0010":
			op = "SUB"
		elif binstr[12:] == "0011":
			op = "SBC"
		elif binstr[12:] == "0100":
			op = "AND"
		elif binstr[12:] == "0101":
			op = "OR"
		elif binstr[12:] == "0110":
			op = "XOR"
		elif binstr[12:] == "0111":
			op = "NOT"
		elif binstr[12:] == "1000":
			op = "SL"
		elif binstr[12:] == "1001":
			op = "SRL"
		elif binstr[12:] == "1010":
			op = "SRA"
		elif binstr[12:] == "1110":
			op = "RRA"
		elif binstr[12:] == "1101":
			op = "RR"
		elif binstr[12:] == "1100":
			op = "RL"

		r1 = RegNumToSymbol(binstr[3:7])
		r2 = RegNumToSymbol(binstr[7:11])

		retstr += "{} \t{}, {}".format(op, r1, r2)

	elif binstr[0:3] == "110":
		if binstr[7] == "0":
			op = "JMP"
		elif binstr[7] == "1":
			op = "JAL"
		r1 = RegNumToSymbol(binstr[3:7])
		os = BinToHexStr(binstr[8:])
		retstr += "{} \t{}, {}".format(op, r1, os)

	elif binstr[0:3] == "111":
		op = ""
		if binstr[3:7] == "0000":
			op = "BR"
		elif binstr[3:7] == "1000":
			op = "BC"
		elif binstr[3:7] == "0100":
			op = "BO"
		elif binstr[3:7] == "0010":
			op = "BN"
		elif binstr[3:7] == "0001":
			op = "BZ"

		sos = BinToHexStr(binstr[8:], signed = True)
		target = CalculateBranchAddress(addr, sos)
		retstr += "{} \t{} <{}>".format(op, sos, target)

	return retstr

def ReadMemoryInitFile(fpath):
	meminputfile = open(fpath, 'r')
	datalines = [];
	
	for line in meminputfile:
		lhex = "0x%0.4X" % int(line.strip(), 2)
		datalines.append(lhex)

	return datalines

if __name__ == "__main__":

	dl = ReadMemoryInitFile(sys.argv[1])
	print("  addr \t|  data")
	print("-------\t| ------")
	for (i, elem) in enumerate(dl):
		addr = "0x%0.4X" % i
		inst_decode = Dissassemble(elem, addr)
		print("{} \t: {} \t| {}".format(addr, elem, inst_decode))