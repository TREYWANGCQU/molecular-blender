#
#  Molecular Blender
#  Filename: periodictable.py
#  Copyright (C) 2014 Shane Parker, Joshua Szekely
#
#  This file is part of Molecular Blender.
#
#  Molecular Blender is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  Molecular Blender is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Molecular Blender; see COPYING.
#  If not, see <http://www.gnu.org/licenses/>.
#

class element():
    def __init__(self, vdw, cov, col, m, n, s):
        self.vdw = vdw
        self.covalent = cov
        self.color = col
        self.mass = m
        self.name= n
        self.symbol = s

default_palette = {
  'h'  : (1.000,1.000,1.000),
  'he' : (0.851,1.000,1.000),
  'li' : (0.800,0.502,1.000),
  'be' : (0.761,1.000,0.000),
  'b'  : (1.000,0.710,0.710),
  'c'  : (0.565,0.565,0.565),
  'n'  : (0.188,0.314,0.973),
  'o'  : (1.000,0.051,0.051),
  'f'  : (0.565,0.878,0.314),
  'ne' : (0.702,0.890,0.961),
  'na' : (0.671,0.361,0.949),
  'mg' : (0.541,1.000,0.000),
  'al' : (0.749,0.651,0.651),
  'si' : (0.941,0.784,0.627),
  'p'  : (1.000,0.502,0.000),
  's'  : (1.000,1.000,0.188),
  'cl' : (0.122,0.941,0.122),
  'ar' : (0.502,0.820,0.890),
  'k'  : (0.561,0.251,0.831),
  'ca' : (0.239,1.000,0.000),
  'sc' : (0.902,0.902,0.902),
  'ti' : (0.749,0.761,0.780),
  'v'  : (0.651,0.651,0.671),
  'cr' : (0.541,0.600,0.780),
  'mn' : (0.612,0.478,0.780),
  'fe' : (0.878,0.400,0.200),
  'co' : (0.941,0.565,0.627),
  'ni' : (0.314,0.816,0.314),
  'cu' : (0.784,0.502,0.200),
  'zn' : (0.490,0.502,0.690),
  'ga' : (0.761,0.561,0.561),
  'ge' : (0.400,0.561,0.561),
  'as' : (0.741,0.502,0.890),
  'se' : (1.000,0.631,0.000),
  'br' : (0.651,0.161,0.161),
  'kr' : (0.361,0.722,0.820),
  'rb' : (0.439,0.180,0.690),
  'sr' : (0.000,1.000,0.000),
  'y'  : (0.580,1.000,1.000),
  'zr' : (0.580,0.878,0.878),
  'nb' : (0.451,0.761,0.788),
  'mo' : (0.329,0.710,0.710),
  'tc' : (0.231,0.620,0.620),
  'ru' : (0.141,0.561,0.561),
  'rh' : (0.039,0.490,0.549),
  'pd' : (0.000,0.412,0.522),
  'ag' : (0.753,0.753,0.753),
  'cd' : (1.000,0.851,0.561),
  'in' : (0.651,0.459,0.451),
  'sn' : (0.400,0.502,0.502),
  'sb' : (0.620,0.388,0.710),
  'te' : (0.831,0.478,0.000),
  'i'  : (0.580,0.000,0.580),
  'xe' : (0.259,0.620,0.690),
  'cs' : (0.341,0.090,0.561),
  'ba' : (0.000,0.788,0.000),
  'la' : (0.439,0.831,1.000),
  'ce' : (1.000,1.000,0.780),
  'pr' : (0.851,1.000,0.780),
  'nd' : (0.780,1.000,0.780),
  'pm' : (0.639,1.000,0.780),
  'sm' : (0.561,1.000,0.780),
  'eu' : (0.380,1.000,0.780),
  'gd' : (0.271,1.000,0.780),
  'tb' : (0.188,1.000,0.780),
  'dy' : (0.122,1.000,0.780),
  'ho' : (0.000,1.000,0.612),
  'er' : (0.000,0.902,0.459),
  'tm' : (0.000,0.831,0.322),
  'yb' : (0.000,0.749,0.220),
  'lu' : (0.000,0.671,0.141),
  'hf' : (0.302,0.761,1.000),
  'ta' : (0.302,0.651,1.000),
  'w'  : (0.129,0.580,0.839),
  're' : (0.149,0.490,0.671),
  'os' : (0.149,0.400,0.588),
  'ir' : (0.090,0.329,0.529),
  'pt' : (0.816,0.816,0.878),
  'au' : (1.000,0.820,0.137),
  'hg' : (0.722,0.722,0.816),
  'tl' : (0.651,0.329,0.302),
  'pb' : (0.341,0.349,0.380),
  'bi' : (0.620,0.310,0.710),
  'po' : (0.671,0.361,0.000),
  'at' : (0.459,0.310,0.271),
  'rn' : (0.259,0.510,0.588),
  'fr' : (0.259,0.000,0.400),
  'ra' : (0.000,0.490,0.000),
  'ac' : (0.439,0.671,0.980),
  'th' : (0.000,0.729,1.000),
  'pa' : (0.000,0.631,1.000),
  'u'  : (0.000,0.561,1.000),
  'np' : (0.000,0.502,1.000),
  'pu' : (0.000,0.420,1.000),
  'am' : (0.329,0.361,0.949),
  'cm' : (0.471,0.361,0.890),
  'bk' : (0.541,0.310,0.890),
  'cf' : (0.631,0.212,0.831),
  'es' : (0.702,0.122,0.831),
  'fm' : (0.702,0.122,0.729),
  'md' : (0.702,0.051,0.651),
  'no' : (0.741,0.051,0.529),
  'lr' : (0.780,0.000,0.400),
  'rf' : (0.800,0.000,0.349),
  'db' : (0.820,0.000,0.310),
  'sg' : (0.851,0.000,0.271),
  'bh' : (0.878,0.000,0.220),
  'hs' : (0.902,0.000,0.180),
  'mt' : (0.922,0.000,0.149)
}

vmd_colors = {
      "blue" : (0.000000, 0.000000, 1.000000),
       "red" : (1.000000, 0.000000, 0.000000),
      "gray" : (0.350000, 0.350000, 0.350000),
    "orange" : (1.000000, 0.500000, 0.000000),
    "yellow" : (1.000000, 1.000000, 0.000000),
       "tan" : (0.500000, 0.500000, 0.200000),
    "silver" : (0.600000, 0.600000, 0.600000),
     "green" : (0.000000, 1.000000, 0.000000),
     "white" : (1.000000, 1.000000, 1.000000),
      "pink" : (1.000000, 0.600000, 0.600000),
      "cyan" : (0.250000, 0.750000, 0.750000),
    "purple" : (0.650000, 0.000000, 0.650000),
      "lime" : (0.500000, 0.900000, 0.400000),
     "mauve" : (0.900000, 0.400000, 0.700000),
     "ochre" : (0.500000, 0.300000, 0.000000),
   "iceblue" : (0.500000, 0.500000, 0.750000),
     "black" : (0.000000, 0.000000, 0.000000),
   "yellow2" : (0.880000, 0.970000, 0.020000),
   "yellow3" : (0.550000, 0.900000, 0.020000),
    "green2" : (0.000000, 0.900000, 0.040000),
    "green3" : (0.000000, 0.900000, 0.500000),
     "cyan2" : (0.000000, 0.880000, 1.000000),
     "cyan3" : (0.000000, 0.760000, 1.000000),
     "blue2" : (0.020000, 0.380000, 0.670000),
     "blue3" : (0.010000, 0.040000, 0.930000),
    "violet" : (0.270000, 0.000000, 0.980000),
   "violet2" : (0.450000, 0.000000, 0.900000),
   "magenta" : (0.900000, 0.000000, 0.900000),
  "magenta2" : (1.000000, 0.000000, 0.660000),
      "red2" : (0.980000, 0.000000, 0.230000),
      "red3" : (0.810000, 0.000000, 0.000000),
   "orange2" : (0.890000, 0.350000, 0.000000),
   "orange3" : (0.960000, 0.720000, 0.000000)
}

vmd_palette = {
  "ac" : vmd_colors["ochre"],
  "ag" : vmd_colors["ochre"],
  "al" : vmd_colors["ochre"],
  "am" : vmd_colors["ochre"],
  "ar" : vmd_colors["ochre"],
  "as" : vmd_colors["ochre"],
  "at" : vmd_colors["ochre"],
  "au" : vmd_colors["ochre"],
   "b" : vmd_colors["ochre"],
  "ba" : vmd_colors["ochre"],
  "be" : vmd_colors["ochre"],
  "bh" : vmd_colors["ochre"],
  "bi" : vmd_colors["ochre"],
  "bk" : vmd_colors["ochre"],
  "br" : vmd_colors["ochre"],
   "c" : vmd_colors["cyan"],
  "ca" : vmd_colors["ochre"],
  "cd" : vmd_colors["ochre"],
  "ce" : vmd_colors["ochre"],
  "cf" : vmd_colors["ochre"],
  "cl" : vmd_colors["ochre"],
  "cm" : vmd_colors["ochre"],
  "co" : vmd_colors["ochre"],
  "cr" : vmd_colors["ochre"],
  "cs" : vmd_colors["ochre"],
  "cu" : vmd_colors["ochre"],
  "db" : vmd_colors["ochre"],
  "ds" : vmd_colors["ochre"],
  "dy" : vmd_colors["ochre"],
  "er" : vmd_colors["ochre"],
  "es" : vmd_colors["ochre"],
  "eu" : vmd_colors["ochre"],
   "f" : vmd_colors["ochre"],
  "fe" : vmd_colors["ochre"],
  "fm" : vmd_colors["ochre"],
  "fr" : vmd_colors["ochre"],
  "ga" : vmd_colors["ochre"],
  "gd" : vmd_colors["ochre"],
  "ge" : vmd_colors["ochre"],
   "h" : vmd_colors["white"],
  "he" : vmd_colors["ochre"],
  "hf" : vmd_colors["ochre"],
  "hg" : vmd_colors["ochre"],
  "ho" : vmd_colors["ochre"],
  "hs" : vmd_colors["ochre"],
   "i" : vmd_colors["ochre"],
  "in" : vmd_colors["ochre"],
  "ir" : vmd_colors["ochre"],
   "k" : vmd_colors["ochre"],
  "kr" : vmd_colors["ochre"],
  "la" : vmd_colors["ochre"],
  "li" : vmd_colors["ochre"],
  "lr" : vmd_colors["ochre"],
  "lu" : vmd_colors["ochre"],
  "md" : vmd_colors["ochre"],
  "mg" : vmd_colors["ochre"],
  "mn" : vmd_colors["ochre"],
  "mo" : vmd_colors["ochre"],
  "mt" : vmd_colors["ochre"],
   "n" : vmd_colors["blue"],
  "na" : vmd_colors["ochre"],
  "nb" : vmd_colors["ochre"],
  "nd" : vmd_colors["ochre"],
  "ne" : vmd_colors["ochre"],
  "ni" : vmd_colors["ochre"],
  "no" : vmd_colors["ochre"],
  "np" : vmd_colors["ochre"],
   "o" : vmd_colors["red"],
  "os" : vmd_colors["ochre"],
   "p" : vmd_colors["tan"],
  "pa" : vmd_colors["ochre"],
  "pb" : vmd_colors["ochre"],
  "pd" : vmd_colors["ochre"],
  "pm" : vmd_colors["ochre"],
  "po" : vmd_colors["ochre"],
  "pr" : vmd_colors["ochre"],
  "pt" : vmd_colors["ochre"],
  "pu" : vmd_colors["ochre"],
  "ra" : vmd_colors["ochre"],
  "rb" : vmd_colors["ochre"],
  "re" : vmd_colors["ochre"],
  "rf" : vmd_colors["ochre"],
  "rg" : vmd_colors["ochre"],
  "rh" : vmd_colors["ochre"],
  "rn" : vmd_colors["ochre"],
  "ru" : vmd_colors["ochre"],
   "s" : vmd_colors["yellow"],
  "sb" : vmd_colors["ochre"],
  "sc" : vmd_colors["ochre"],
  "se" : vmd_colors["ochre"],
  "sg" : vmd_colors["ochre"],
  "si" : vmd_colors["ochre"],
  "sm" : vmd_colors["ochre"],
  "sn" : vmd_colors["ochre"],
  "sr" : vmd_colors["ochre"],
  "ta" : vmd_colors["ochre"],
  "tb" : vmd_colors["ochre"],
  "tc" : vmd_colors["ochre"],
  "te" : vmd_colors["ochre"],
  "th" : vmd_colors["ochre"],
  "ti" : vmd_colors["ochre"],
  "tl" : vmd_colors["ochre"],
  "tm" : vmd_colors["ochre"],
   "u" : vmd_colors["ochre"],
   "v" : vmd_colors["ochre"],
   "w" : vmd_colors["ochre"],
   "x" : vmd_colors["purple"],
  "xe" : vmd_colors["ochre"],
   "y" : vmd_colors["ochre"],
  "yb" : vmd_colors["ochre"],
  "zn" : vmd_colors["silver"],
  "zr" : vmd_colors["ochre"]
}

def generate_table(palette_name):
    palette = {}
    if (palette_name == "vmd"):
        palette = vmd_palette
    else:
        palette = default_palette

    elements = {
    # key  :         vdw,   cov,               color,  mass, full name , symbol
      'h'  : element(1.20, 0.31, palette['h' ],   1.0, "Hydrogen", "h"),
      'he' : element(1.40, 0.28, palette['he'],   4.0, "Helium", "he"),
      'li' : element(1.82, 1.28, palette['li'],   6.9, "Lithium", "li"),
      'be' : element(1.00, 0.96, palette['be'],   9.0, "Beryllium", "be"),
      'b'  : element(1.00, 0.84, palette['b' ],  10.8, "Boron", "b"),
      'c'  : element(1.70, 0.76, palette['c' ],  12.0, "Carbon", "c"),
      'n'  : element(1.55, 0.71, palette['n' ],  14.0, "Nitrogen", "n"),
      'o'  : element(1.52, 0.66, palette['o' ],  16.0, "Oxygen", "o"),
      'f'  : element(1.47, 0.57, palette['f' ],  19.0, "Fluorine", "f"),
      'ne' : element(1.54, 0.58, palette['ne'],  20.2, "Neon", "ne"),
      'na' : element(2.27, 1.66, palette['na'],  23.0, "Sodium", "na"),
      'mg' : element(1.73, 1.41, palette['mg'],  24.3, "Magnesium", "mg"),
      'al' : element(1.84, 1.21, palette['al'],  27.0, "Aluminum", "al"),
      'si' : element(2.10, 1.11, palette['si'],  28.1, "Silicon", "si"),
      'p'  : element(1.80, 1.07, palette['p' ],  31.0, "Phosphorus", "p"),
      's'  : element(1.80, 1.05, palette['s' ],  32.1, "Sulfur", "s"),
      'cl' : element(1.75, 1.02, palette['cl'],  35.5, "Chlorine", "cl"),
      'ar' : element(1.88, 1.06, palette['ar'],  39.9, "Argon", "ar"),
      'k'  : element(2.75, 2.03, palette['k' ],  39.1, "Potassium", "k"),
      'ca' : element(2.31, 1.76, palette['ca'],  40.1, "Calcium", "ca"),
      'sc' : element(1.00, 1.70, palette['sc'],  45.0, "Scandium", "sc"),
      'ti' : element(1.00, 1.36, palette['ti'],  47.9, "Titanium", "ti"),
      'v'  : element(1.00, 1.53, palette['v' ],  50.9, "Vanadium", "v"),
      'cr' : element(1.00, 1.39, palette['cr'],  52.0, "Chromium", "cr"),
      'mn' : element(1.00, 1.39, palette['mn'],  54.9, "Manganese", "mn"),
      'fe' : element(1.00, 1.32, palette['fe'],  55.8, "Iron", "fe"),
      'co' : element(1.00, 1.26, palette['co'],  58.9, "Cobalt", "co"),
      'ni' : element(1.63, 1.24, palette['ni'],  58.7, "Nickel", "ni"),
      'cu' : element(1.45, 1.32, palette['cu'],  63.5, "Copper", "cu"),
      'zn' : element(1.42, 1.22, palette['zn'],  65.4, "Zinc", "zn"),
      'ga' : element(1.87, 1.22, palette['ga'],  69.7, "Gallium", "ga"),
      'ge' : element(1.00, 1.20, palette['ge'],  72.6, "Germanium", "ge"),
      'as' : element(1.85, 1.19, palette['as'],  74.9, "Arsenic", "as"),
      'se' : element(1.90, 1.20, palette['se'],  79.0, "Selenium", "se"),
      'br' : element(1.85, 1.20, palette['br'],  79.9, "Bromine", "br"),
      'kr' : element(2.02, 1.16, palette['kr'],  83.8, "Krypton", "kr"),
      'rb' : element(1.00, 2.20, palette['rb'],  85.5, "Rubidium", "rb"),
      'sr' : element(1.00, 1.95, palette['sr'],  87.6, "Strontium", "sr"),
      'y'  : element(1.00, 1.90, palette['y' ],  88.9, "Yttrium", "y"),
      'zr' : element(1.00, 1.75, palette['zr'],  91.2, "Zirconium", "zr"),
      'nb' : element(1.00, 1.64, palette['nb'],  92.9, "Niobium", "nb"),
      'mo' : element(1.00, 1.54, palette['mo'],  95.9, "Molybdenum", "mo"),
      'tc' : element(1.00, 1.47, palette['tc'],  98.0, "Technetium", "tc"),
      'ru' : element(1.00, 1.46, palette['ru'], 101.1, "Ruthenium", "ru"),
      'rh' : element(1.00, 1.42, palette['rh'], 102.9, "Rhodium", "rh"),
      'pd' : element(1.63, 1.39, palette['pd'], 106.4, "Palladium", "pd"),
      'ag' : element(1.72, 1.45, palette['ag'], 107.9, "Silver", "ag"),
      'cd' : element(1.58, 1.44, palette['cd'], 112.4, "Cadmium", "cd"),
      'in' : element(1.93, 1.42, palette['in'], 114.8, "Indium", "in"),
      'sn' : element(2.17, 1.39, palette['sn'], 118.7, "Tin", "sn"),
      'sb' : element(1.00, 1.39, palette['sb'], 121.8, "Antimony", "sb"),
      'te' : element(2.06, 1.38, palette['te'], 127.6, "Tellurium", "te"),
      'i'  : element(1.98, 1.39, palette['i' ], 126.9, "Iodine", "i"),
      'xe' : element(2.16, 1.40, palette['xe'], 131.3, "Xenon", "xe"),
      'cs' : element(1.00, 2.44, palette['cs'], 132.9, "Cesium", "cs"),
      'ba' : element(2.68, 2.15, palette['ba'], 137.3, "Barium", "ba"),
      'la' : element(1.00, 2.07, palette['la'], 138.9, "Lanthanum", "la"),
      'ce' : element(1.00, 2.04, palette['ce'], 140.1, "Cerium", "ce"),
      'pr' : element(1.00, 2.03, palette['pr'], 140.9, "Praseodymium", "pr"),
      'nd' : element(1.00, 2.01, palette['nd'], 144.2, "Neodymium", "nd"),
      'pm' : element(1.00, 1.99, palette['pm'], 145.0, "Promethium", "pm"),
      'sm' : element(1.00, 1.98, palette['sm'], 150.4, "Samarium", "sm"),
      'eu' : element(1.00, 1.98, palette['eu'], 152.0, "Europium", "eu"),
      'gd' : element(1.00, 1.96, palette['gd'], 157.2, "Gadolinium", "gd"),
      'tb' : element(1.00, 1.94, palette['tb'], 158.9, "Terbium", "tb"),
      'dy' : element(1.00, 1.92, palette['dy'], 162.5, "Dysprosium", "dy"),
      'ho' : element(1.00, 1.92, palette['ho'], 164.9, "Holmium", "ho"),
      'er' : element(1.00, 1.89, palette['er'], 167.3, "Erbium", "er"),
      'tm' : element(1.00, 1.90, palette['tm'], 168.9, "Thulium", "tm"),
      'yb' : element(1.00, 1.87, palette['yb'], 173.0, "Ytterbium", "yb"),
      'lu' : element(1.00, 1.87, palette['lu'], 175.0, "Lutetium", "lu"),
      'hf' : element(1.00, 1.75, palette['hf'], 178.5, "Hafnium", "hf"),
      'ta' : element(1.00, 1.70, palette['ta'], 180.9, "Tantalum", "ta"),
      'w'  : element(1.00, 1.62, palette['w' ], 183.8, "Tungsten", "w"),
      're' : element(1.00, 1.51, palette['re'], 186.2, "Rhenium", "re"),
      'os' : element(1.00, 1.44, palette['os'], 190.2, "Osmium", "os"),
      'ir' : element(1.00, 1.41, palette['ir'], 192.2, "Iridium", "ir"),
      'pt' : element(1.75, 1.36, palette['pt'], 195.1, "Platinum", "pt"),
      'au' : element(1.66, 1.36, palette['au'], 197.0, "Gold", "au"),
      'hg' : element(1.55, 1.32, palette['hg'], 200.6, "Mercury", "hg"),
      'tl' : element(1.96, 1.45, palette['tl'], 204.4, "Thallium", "tl"),
      'pb' : element(2.02, 1.46, palette['pb'], 207.2, "Lead", "pb"),
      'bi' : element(1.00, 1.48, palette['bi'], 209.0, "Bismuth", "bi"),
      'po' : element(1.00, 1.40, palette['po'], 209.0, "Polonium", "po"),
      'at' : element(1.00, 1.50, palette['at'], 210.0, "Astatine", "at"),
      'rn' : element(2.20, 1.50, palette['rn'], 222.0, "Radon", "rn"),
      'fr' : element(1.00, 2.60, palette['fr'], 223.0, "Francium", "fr"),
      'ra' : element(1.00, 2.21, palette['ra'], 226.0, "Radium", "ra"),
      'ac' : element(1.00, 2.15, palette['ac'], 227.0, "Actinium", "ac"),
      'th' : element(1.00, 2.06, palette['th'], 232.0, "Thorium", "th"),
      'pa' : element(1.00, 2.00, palette['pa'], 231.0, "Protactinium", "pa"),
      'u'  : element(1.00, 1.96, palette['u' ], 238.0, "Uranium", "u"),
      'np' : element(1.00, 1.90, palette['np'], 237.0, "Neptunium", "np"),
      'pu' : element(1.00, 1.87, palette['pu'], 244.0, "Plutonium", "pu"),
      'am' : element(1.00, 1.80, palette['am'], 243.0, "Americium", "am"),
      'cm' : element(1.00, 1.69, palette['cm'], 247.0, "Curium", "cm"),
      'bk' : element(1.00, 1.00, palette['bk'], 247.0, "Berkelium", "bk"),
      'cf' : element(1.00, 1.00, palette['cf'], 251.0, "Californium", "cf"),
      'es' : element(1.00, 1.00, palette['es'], 252.0, "Einsteinium", "es"),
      'fm' : element(1.00, 1.00, palette['fm'], 257.0, "Fermium", "fm"),
      'md' : element(1.00, 1.00, palette['md'], 258.0, "Mendelevium", "md"),
      'no' : element(1.00, 1.00, palette['no'], 259.0, "Nobelium", "no"),
      'lr' : element(1.00, 1.00, palette['lr'], 262.0, "Lawrencium", "lr"),
      'rf' : element(1.00, 1.00, palette['rf'], 261.0, "Rutherfordium", "rf"),
      'db' : element(1.00, 1.00, palette['db'], 262.0, "Dubnium", "db"),
      'sg' : element(1.00, 1.00, palette['sg'], 266.0, "Seaborgium", "sg"),
      'bh' : element(1.00, 1.00, palette['bh'], 264.0, "Bohrium", "bh"),
      'hs' : element(1.00, 1.00, palette['hs'], 277.0, "Hassium", "hs"),
      'mt' : element(1.00, 1.00, palette['mt'], 268.0, "Meitnerium", "mt")
    }
    return elements

symbols = [ "empty",
            "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al",
            "si", "p", "s", "cl", "ar", "k", "ca", "sc", "ti", "v", "cr", "mn", "fe",
            "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr",
            "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn",
            "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd", "pm", "sm",
            "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w",
            "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn",
            "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf",
            "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds",
            "rg", "cn", "uut", "fl", "uup", "lv", "uus", "uuo"
          ]
