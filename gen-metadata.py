
from paralex import paralex_factory

package = paralex_factory("Ngkolmpu Verbal Paradigms",
    {
     "paradigms": {"path": "Ngkolmpu_v_paradigms.csv"},
     "cells": {"path": "Ngkolmpu_v_cells.csv"},
     "paradigms": {"path": "Ngkolmpu_v_paradigms.csv"},
     "features-values": {"path": "Ngkolmpu_v_features.csv"},
     "lexemes": {"path": "Ngkolmpu_v_lexemes.csv"},
     "sounds": {"path": "Ngkolmpu_v_sounds.csv"}
     },
     citation="Carroll, MJ (2022). Ngkolmpu Verbal Paradigms Paralex dataset. Online.",
     version="1.0.0",
     keywords=["Ngkolmpu", "paradigms"],
     id="",
     contributors=[{'title': 'MJ Carroll', 'role': 'author'}],
     licenses=[{'name': 'GPL-3.0',
               'title': 'GNU General Public License 3.0',
               'path': 'https://opensource.org/licenses/GPL-3.0'}],
               )
package.to_json("Ngkolmpu.package.json")
