def binario(s):
    listaletra = [" ","A", "B", "C", "D", "E",""]
    listabinario = ["00000", "00001", "00010", "00011", "00100", "00101"]
    palavra = ""
    s = str.strip(s)
    i = 0
    while i < len(s):
        indice = listaletra.index(s[i:i+1])
        palavra = palavra+listabinario[indice]
        i+=1
    return palavra
    
        
        
