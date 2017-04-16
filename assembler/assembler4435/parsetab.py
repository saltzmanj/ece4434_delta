
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NOP EI DI SWI USR LD ST MOV LIL LIH ADD ADC SUB SBC AND OR XOR NOT SL SRL SRA RRA RR RL JMP JAL BR BC BO BN BZ REGISTER NUMBER WORD FILL CHK CHK_MACROprogram : inst instlistinstlist : inst instlistinstlist : inst : WORD NUMBER NUMBERinst : FILL NUMBER NUMBERinst : NOPinst : EIinst : DIinst : SWI NUMBERinst : USRinst : LD REGISTER REGISTER NUMBERinst : ST REGISTER REGISTER NUMBERinst : MOV REGISTER REGISTERinst : LIL REGISTER NUMBERinst : LIH REGISTER NUMBERinst : ADD REGISTER REGISTERinst : ADC REGISTER REGISTERinst : SUB REGISTER REGISTERinst : SBC REGISTER REGISTERinst : AND REGISTER REGISTERinst : OR REGISTER REGISTERinst : XOR REGISTER REGISTERinst : NOT REGISTER REGISTERinst : SL REGISTER REGISTERinst : SRL REGISTER REGISTERinst : SRA REGISTER REGISTERinst : RRA REGISTER REGISTERinst : RR REGISTER REGISTERinst : RL REGISTER REGISTERinst : JMP REGISTER NUMBERinst : JAL REGISTER NUMBERinst : BR NUMBERinst : BC NUMBERinst : BO NUMBERinst : BN NUMBERinst : BZ NUMBERinst : CHK CHK_MACRO NUMBER'
    
_lr_action_items = {'OR':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[1,-7,-10,1,-8,-6,-32,-34,-35,-9,1,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'ADC':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[2,-7,-10,2,-8,-6,-32,-34,-35,-9,2,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'BR':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[3,-7,-10,3,-8,-6,-32,-34,-35,-9,3,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'LIL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[36,-7,-10,36,-8,-6,-32,-34,-35,-9,36,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'BO':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[4,-7,-10,4,-8,-6,-32,-34,-35,-9,4,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'LIH':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[34,-7,-10,34,-8,-6,-32,-34,-35,-9,34,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'CHK_MACRO':([22,],[55,]),'SL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[6,-7,-10,6,-8,-6,-32,-34,-35,-9,6,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'RRA':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[7,-7,-10,7,-8,-6,-32,-34,-35,-9,7,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'$end':([17,19,21,24,30,33,39,40,45,48,57,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,92,93,94,95,],[-7,-10,0,-3,-8,-6,-32,-34,-35,-9,-1,-3,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-2,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'SRA':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[11,-7,-10,11,-8,-6,-32,-34,-35,-9,11,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'RL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[10,-7,-10,10,-8,-6,-32,-34,-35,-9,10,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'SWI':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[12,-7,-10,12,-8,-6,-32,-34,-35,-9,12,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'RR':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[13,-7,-10,13,-8,-6,-32,-34,-35,-9,13,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'AND':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[14,-7,-10,14,-8,-6,-32,-34,-35,-9,14,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'SBC':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[15,-7,-10,15,-8,-6,-32,-34,-35,-9,15,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'XOR':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[16,-7,-10,16,-8,-6,-32,-34,-35,-9,16,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'EI':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[17,-7,-10,17,-8,-6,-32,-34,-35,-9,17,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'SUB':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[18,-7,-10,18,-8,-6,-32,-34,-35,-9,18,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'REGISTER':([1,2,6,7,8,10,11,13,14,15,16,18,20,25,26,27,28,29,32,34,36,37,38,42,43,46,47,49,50,51,52,53,54,59,60,61,63,65,],[37,38,42,43,44,46,47,49,50,51,52,53,54,59,60,61,62,63,65,66,68,69,70,72,73,75,76,77,78,79,80,81,82,86,87,88,90,91,]),'USR':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[19,-7,-10,19,-8,-6,-32,-34,-35,-9,19,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'MOV':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[26,-7,-10,26,-8,-6,-32,-34,-35,-9,26,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'LD':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[20,-7,-10,20,-8,-6,-32,-34,-35,-9,20,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'CHK':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[22,-7,-10,22,-8,-6,-32,-34,-35,-9,22,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'WORD':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[23,-7,-10,23,-8,-6,-32,-34,-35,-9,23,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'JMP':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[28,-7,-10,28,-8,-6,-32,-34,-35,-9,28,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'ADD':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[25,-7,-10,25,-8,-6,-32,-34,-35,-9,25,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'NUMBER':([3,4,5,9,12,23,31,35,41,44,55,56,62,66,68,82,91,],[39,40,41,45,48,56,64,67,71,74,83,84,89,92,93,94,95,]),'NOT':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[27,-7,-10,27,-8,-6,-32,-34,-35,-9,27,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'JAL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[8,-7,-10,8,-8,-6,-32,-34,-35,-9,8,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'SRL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[29,-7,-10,29,-8,-6,-32,-34,-35,-9,29,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'DI':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[30,-7,-10,30,-8,-6,-32,-34,-35,-9,30,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'BC':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[31,-7,-10,31,-8,-6,-32,-34,-35,-9,31,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'ST':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[32,-7,-10,32,-8,-6,-32,-34,-35,-9,32,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'NOP':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[33,-7,-10,33,-8,-6,-32,-34,-35,-9,33,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'FILL':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[5,-7,-10,5,-8,-6,-32,-34,-35,-9,5,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'BZ':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[35,-7,-10,35,-8,-6,-32,-34,-35,-9,35,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),'BN':([0,17,19,24,30,33,39,40,45,48,58,64,67,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,89,90,92,93,94,95,],[9,-7,-10,9,-8,-6,-32,-34,-35,-9,9,-33,-36,-21,-17,-5,-24,-27,-31,-29,-26,-28,-20,-19,-22,-18,-37,-4,-16,-13,-23,-30,-25,-15,-14,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[21,]),'instlist':([24,58,],[57,85,]),'inst':([0,24,58,],[24,58,58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> inst instlist','program',2,'p_program','lexerparser.py',212),
  ('instlist -> inst instlist','instlist',2,'p_instlist_inst','lexerparser.py',216),
  ('instlist -> <empty>','instlist',0,'p_instlist_empty','lexerparser.py',220),
  ('inst -> WORD NUMBER NUMBER','inst',3,'p_directive_word','lexerparser.py',225),
  ('inst -> FILL NUMBER NUMBER','inst',3,'p_directive_fill','lexerparser.py',230),
  ('inst -> NOP','inst',1,'p_inst_nop','lexerparser.py',234),
  ('inst -> EI','inst',1,'p_inst_ei','lexerparser.py',238),
  ('inst -> DI','inst',1,'p_inst_di','lexerparser.py',242),
  ('inst -> SWI NUMBER','inst',2,'p_inst_swi','lexerparser.py',247),
  ('inst -> USR','inst',1,'p_inst_usr','lexerparser.py',251),
  ('inst -> LD REGISTER REGISTER NUMBER','inst',4,'p_inst_ld','lexerparser.py',256),
  ('inst -> ST REGISTER REGISTER NUMBER','inst',4,'p_inst_st','lexerparser.py',261),
  ('inst -> MOV REGISTER REGISTER','inst',3,'p_inst_mov','lexerparser.py',265),
  ('inst -> LIL REGISTER NUMBER','inst',3,'p_inst_lil','lexerparser.py',270),
  ('inst -> LIH REGISTER NUMBER','inst',3,'p_inst_lih','lexerparser.py',275),
  ('inst -> ADD REGISTER REGISTER','inst',3,'p_inst_add','lexerparser.py',279),
  ('inst -> ADC REGISTER REGISTER','inst',3,'p_inst_adc','lexerparser.py',283),
  ('inst -> SUB REGISTER REGISTER','inst',3,'p_inst_sub','lexerparser.py',287),
  ('inst -> SBC REGISTER REGISTER','inst',3,'p_inst_sbc','lexerparser.py',291),
  ('inst -> AND REGISTER REGISTER','inst',3,'p_inst_and','lexerparser.py',295),
  ('inst -> OR REGISTER REGISTER','inst',3,'p_inst_or','lexerparser.py',299),
  ('inst -> XOR REGISTER REGISTER','inst',3,'p_inst_xor','lexerparser.py',303),
  ('inst -> NOT REGISTER REGISTER','inst',3,'p_inst_not','lexerparser.py',307),
  ('inst -> SL REGISTER REGISTER','inst',3,'p_inst_sl','lexerparser.py',311),
  ('inst -> SRL REGISTER REGISTER','inst',3,'p_inst_srl','lexerparser.py',315),
  ('inst -> SRA REGISTER REGISTER','inst',3,'p_inst_sra','lexerparser.py',319),
  ('inst -> RRA REGISTER REGISTER','inst',3,'p_inst_rra','lexerparser.py',323),
  ('inst -> RR REGISTER REGISTER','inst',3,'p_inst_rr','lexerparser.py',327),
  ('inst -> RL REGISTER REGISTER','inst',3,'p_inst_rl','lexerparser.py',331),
  ('inst -> JMP REGISTER NUMBER','inst',3,'p_inst_jmp','lexerparser.py',335),
  ('inst -> JAL REGISTER NUMBER','inst',3,'p_inst_jal','lexerparser.py',339),
  ('inst -> BR NUMBER','inst',2,'p_inst_br','lexerparser.py',343),
  ('inst -> BC NUMBER','inst',2,'p_inst_bc','lexerparser.py',347),
  ('inst -> BO NUMBER','inst',2,'p_inst_bo','lexerparser.py',351),
  ('inst -> BN NUMBER','inst',2,'p_inst_bn','lexerparser.py',355),
  ('inst -> BZ NUMBER','inst',2,'p_inst_bz','lexerparser.py',359),
  ('inst -> CHK CHK_MACRO NUMBER','inst',3,'p_inst_chk','lexerparser.py',363),
]