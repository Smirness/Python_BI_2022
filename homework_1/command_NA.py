# Commands
commands_list = [
    'transcribe', 'complement', 'reverse', 'reverse complement'
]

transcribe = {
    'A': 'A',
    'a': 'a',
    'T': 'U',
    't': 'u',
    'U': 'T',
    'u': 'T',
    'C': 'C',
    'c': 'c',
    'G': 'G',
    'g': 'g',
}

complement = {
    'A': 'T',
    'a': 't',
    'T': 'A',
    't': 'a',
    'C': 'G',
    'c': 'g',
    'G': 'C',
    'g': 'c',
}


# input command + cheking
command = input('Enter command:')

while command != 'exit':
    
    check_com = False
    while check_com == False:
        if command in commands_list:
            check_com = True
        else:
            print('Invalid alphabet. Try again!')
            print('Enter command:')
            command = input()
        
    
    # input sequence + cheking
    sequence = input('Enter sequence:')

    check_seq = False
    while check_seq == False:
        if 'u' in sequence.lower() and 't' in sequence.lower():
            print('Invalid alphabet. Try again!')
            sequence = input('Enter sequence:')
                
        for nt in sequence:
            if nt in 'AaTtUuCcGg':
                check_seq = True
            else:
                print('Invalid alphabet. Try again!')
                sequence = input('Enter sequence:')
                

    # proccessing
    result = ''
    if command == 'transcribe':
            for nt in sequence:
                result += transcribe[nt]
            
    elif command == 'complement':
        for nt in sequence:
            result += complement[nt]
            
    elif command == 'reverse':
        result = sequence[::-1]
        
    elif command == 'reverse complement':
        for nt in sequence:
            result += complement[nt]
        result = result[::-1]
    
    #output        
    print(result)
    command = input('Enter command:')

else:
    print('Good luck')