import sys
import ast
from function_map import function_map




def main():
    func = function_map[sys.argv[1]]
    args_dict = {}
    for idx in range(2, len(sys.argv), 2):
        args_dict[sys.argv[idx]] = ast.literal_eval(sys.argv[idx+1])
    print(func(**args_dict))

if __name__ == "__main__":
    main()




