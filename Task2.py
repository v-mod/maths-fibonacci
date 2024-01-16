import SeqManager
def find_pairs(target_number, sequence_length):
    pairs = []
    for i in range(target_number + 1):
        for j in range(target_number + 1):
            sequence = [i, j]
            for k in range(sequence_length - 2):
                next_number = sequence[-1] + sequence[-2]
                sequence.append(next_number)
            if sequence[-1] == target_number:
                pairs.append((i, j))
    return pairs

target_number = 100
sequence_length = 6

pairs = find_pairs(target_number, sequence_length)
print("Possible pairs of starting numbers:")
for pair in pairs:
    print(pair)
    FibSeq=SeqManager.Sequence([pair[0],pair[1]])
    print(FibSeq.generateSeq(4))

    
