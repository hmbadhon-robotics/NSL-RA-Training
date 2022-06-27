input_array = [-123,-40,2,-50,-40,-123,-50,-40,-100,2,100,-123]

def encoding(input_array):
    my_map={}
    val = 0
    for i in input_array:
        if i not in my_map:
            my_map[i]=val
            val=val+1
    return my_map

def encode_array(encoding_map,input_array):
    encoded_array = []
    for i in input_array:
        x = encoding_map[i]
        encoded_array.append(x)
        #print(x)
    return encoded_array

def compress_array(encoded_array):
    compress_array = [ [] for k in range(100)]
    #print(compress_array)
    for i,val in enumerate(encoded_array):
            compress_array[val].append(i)
    return compress_array

encoding_list = encoding(input_array)
encoded_array = encode_array(encoding_list,input_array)

print(encoded_array)

compressed_array = compress_array(encoded_array)
print(compressed_array)


