#!/usr/bin/env python3

#global scope
first_name = 'Global'

def display_name():
  #local scope
  last_name = 'local'
  return f'{first_name} is a global variable, while {last_name} is a local variable'

print(display_name())