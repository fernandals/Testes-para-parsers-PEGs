# Copyright (c) 2017 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from .tree import *


def simple_space_transformer(node):

    for child in node.children:
        simple_space_transformer(child)

    if isinstance(node, UnparserRule):
        new_children = []
        for child in node.children:
            new_children.extend([child, UnlexerRule(src=' ')])
        node.children = new_children

    return node

def dot_space_transformer(node):
   
    for child in node.children:
        dot_space_transformer(child)

    if isinstance(node, UnparserRule):
        new_children = []

        for child in node.children:
            
            if child.name == "stmt_list":
                new_children.extend( [UnlexerRule(src='\n'), child, UnlexerRule(src='\n'), UnlexerRule(src="    ")] )
            elif child.parent.name == "stmt_list":
                if child.name == "stmt":
                    if len(child.parent.children) == 1:
                        new_children.extend( [UnlexerRule(src="    "), child, UnlexerRule(src='\n')] )
                    else:
                        new_children.extend( [UnlexerRule(src="    "), child] )
                else:
                    new_children.extend( [child, UnlexerRule(src='\n')] )
            else:
                new_children.extend([child, UnlexerRule(src=' ')])

            node.children = new_children

    return node

def abnf_space_transformer(node):
    
    for child in node.children:
        simple_space_transformer(child)

    if isinstance(node, UnparserRule):
        new_children = []
        for child in node.children:
        
            space = 0
            for e in child.children:
                space+=1
                if str(e) == '=':
                    break 
            print("number of spaces = ",  space)

            line = str(child).split('/')
            cont = 0
            for l in line:
                if cont != 0:
                    new_children.extend([' '*space])

                if cont == len(line)-1:
                    new_children.extend([l, UnlexerRule(src='\n')])
                else: 
                    new_children.extend([l, UnlexerRule(src='/'), UnlexerRule(src='\n')])
                cont+=1

        node.children = new_children

    return node

