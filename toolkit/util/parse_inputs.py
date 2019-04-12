#!/usr/bin/env python
# parse_inputs.py

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import sys



def __check_args():
    if sys.argv[1:]:
        arg_val = sys.argv
        del arg_val[0]
        return arg_val
    else:
        return False



def __check_stdin(strip_newline_stdin=False):
    if not sys.stdin.isatty():
        out_list = []
        for line in sys.stdin.readlines():
            if strip_newline_stdin:
                out_list.append(line.strip())
            else:
                out_list.append(line)
        #print(out_list)
        return out_list
    else:
        return False



def parse_inputs(strip_newline_stdin=False):
    arg_result = __check_args()
    stdin_result = __check_stdin(strip_newline_stdin)

    if arg_result:
        return arg_result
    elif stdin_result:
        return stdin_result
    else:
        return False
