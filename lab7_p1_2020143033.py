import re

def find_functions_and_calls(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    function_pattern = re.compile(r'^\s*def\s+(\w+)\s*\(')
    call_pattern = re.compile(r'(\w+)\s*\(')

    functions = {}
    for i, line in enumerate(lines):
        function_match = function_pattern.match(line)
        if function_match:
            func_name = function_match.group(1)
            functions[func_name] = {'def': i + 1, 'calls': set()}

    for i, line in enumerate(lines):
        call_matches = call_pattern.findall(line)
        for call in call_matches:
            if call in functions:
                functions[call]['calls'].add(i + 1)

    for func, details in functions.items():
        calls_excluding_def = sorted(details['calls'] - {details['def']})
        print(f"{func}: def in {details['def']}, calls in {calls_excluding_def}")

if __name__ == "__main__":
    find_functions_and_calls('input_7_1.txt')