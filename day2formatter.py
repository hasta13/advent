#!/usr/bin/python3
f = open("day2input_raw")
f_out = open("day2input_cleaned", "w")

i = 0
endline = False
for l in f:
    l = l.strip()
    #print("line: " + l)
    i += 1
    #if i == 3:
    #    break
    #continue
    for w in l.split(" "):
        #print(w)
        #continue
        if not endline:
            #print(w + " ", end="")
            f_out.write(w + " ")
        if endline:
            f_out.write(w + "\n")
            #print(w)
        endline = not endline
