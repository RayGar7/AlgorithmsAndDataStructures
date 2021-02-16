height_level_keys = [
    ":M:", ":H:", ":L:", ":SM:", ":SH:", ":SL:",
]

# this is not handling dual buttons like ":A+B+K" or ":a+b:", that would have to be hanled on the while loop in line 15
def height_level_string_to_list(value):

    if (value):
        height_level_list = []
        i = 0
        save_point = i
        while (i < len(value) - 1):
            if (value[i] == ":"):
                j = i + 1
                while(j < len(value)):
                    if (value[j] == ":"):
                        height_level_list.append(value[i:j+1])
                        i = j + 1
                        save_point = i
                        break
                    else:
                        j += 1
            else:
                i += 1
                if (i == len(value)):
                    height_level_list.append(value[save_point:i])
                elif (value[i] == ":"):
                    height_level_list.append(value[save_point:i])
                    save_point = i
        value = height_level_list
    else:
       value = ["-"]
    return value


# sample inputs:
# sample_inputs = [":H:", ":H::H:", ":H::H::M::M::M:", ":H::L:", ":M::M::SM:", ":SL:", None, "Hello", ":H::H::M:×5", "Hello this is my :H: people aren't supposed to do this but here is another one :SL:. "]
# for si in sample_inputs:
#     print(height_level_string_to_list(si))

# print(height_level_string_to_list(":H::H::M:×5:L:"))

#print(height_level_string_to_list(":AT:"))


#print(height_level_string_to_list(":H:M::SM:"))



#these strings can be turned into images
command_smilies = [
    ":1:", ":2:", ":3:", ":4:", ":6:", ":7:", ":8:", ":9:",
    ":A:", ":B:", ":K:", ":G:",  
    ":(1):", ":(2):", ":(3):", ":(4):", ":(6):", ":(7):", ":(8):", ":(9):",
    ":(A):", ":(B):", ":(K):", ":(G):",
    "*", "+", ":+:",            # + means multiple buttons, ":+:" means ":(5):"
    ":a-small:", ":b-small:", ":k-small:", ":g-small:",
    ":a:", ":b:", ":k:", ":g:",
    ":aB:", ":bA:", ":kA:", ":kB:",
    ":SC:", ":RE:", "RE",
]

command_dict = {
    "A": ":A:",
    "B": ":B:",
    "K": ":K:",
    "G": ":G:",

    # ":(K):": ,
    # ":(K": ,
    # "K):": ,
    # ":(K)": ,
    # "(K):": ,

    # ":(G):": ,
    # ":(G": ,
    # "G):": ,
    # ":(G)": ,
    # "(G):": ,


    # ":SC:": ,
    # ":RE:": ,
    # "RE": ,


    "a": ":a-small:",
    "b": ":b-small:",
    "k": ":k-small:",
    "g": ":g-small:",

    # ":a-small": ,
    # "a-small:": ,

    # ":b-small:": ,
    # ":b-small": ,
    # "b-small:": ,

    # ":k-small:": ,
    # ":k-small": ,
    # "k-small:": ,

    # ":g-small:": ,
    # ":g-small": ,
    # "g-small:": ,

    # ":a:": ,
    # ":a": ,
    # "a:": ,

    # ":b:": ,
    # ":b": ,
    # "b:": ,

    # ":k:": ,
    # ":k": ,
    # "k:": ,
    
    # ":g:": ,
    # ":g": ,
    # "g:": ,

    # ":aB:": ,
    # ":bA:": ,
    # ":kA:": ,
    # ":kB:": ,


    "*": "*",
    "+": ":+:",
    ":+:": ":+:",
}

def command_string_to_list(move):
    #value = move.command
    value = move
    command_list = []


    i = 0
    save_point = 0
    while (i < len(value) - 1):
        if (value[i] == ":" and not (value[i+1] == ":" or value[i+1] == " ")):
            j = i + 1
            while(j < len(value)):
                if (value[j] == ":"):
                    command_list.append(value[i:j+1])
                    i = j + 1
                    save_point = i
                    break
                else:
                    j += 1
        elif (value[i] == ":" and (value[i+1] == ":" or value[i+1] == " ")):
            command_list.append(value[i])
            i = i + 1
            save_point = i
        else:
            i += 1
            if (i == len(value) - 1):
                command_list.append(value[save_point:i+1])
            elif (value[i] == ":"):
                command_list.append(value[save_point:i])
                save_point = i

                


    return command_list


def handle_multiple_inputs(command_list=[]):
    new = []

    for command in command_list:
        if (command in command_smilies):
            new.append(command)
        else:
            if (command[0] == ":" and command[-1] == ":"):
                # split the element into multiple smilies
                i = 1
                length = len(command)-1
                while (i < length):
                    if (command[i] in command_dict.keys()):
                        new.append(command_dict[command[i]])
                    else:
                        new.append(command[i])

                    i += 1
                
            else:
                # leave as is
                new.append(command)
    return new



move = ":2::3::6::A+B+K:::A:::A:::B:::B:::K:::K:::A:::B:::K:::K:::K:::K:::B+K:"
print(command_string_to_list(move))
#move = ":A:::A::"
#move = "::A::"
#move = ":A:: :A::"      # ok
#move = ":A: ::A::"      # ok
#move = ":A: : :A::"  
#move = ":aB: ~ Ronin Technique"   
#move = ":6::A: ~ Ronin Technique"
#move = ":LH::RE::A:"

# now I gotta handle button combinations like ":A+B:"
move = ":aB:"                          #ok
print(command_string_to_list(move))
move = ":aB: ~ Ronin Technique"        #ok
print(command_string_to_list(move))
move = ":bA:"                          #ok
print(command_string_to_list(move))
move = ":bK:"
print(command_string_to_list(move))
move = ":A+B:"      # ok
print(command_string_to_list(move))
move = ":LH: :A+B:"
print(command_string_to_list(move))
move = ":6::A+B:"
print(command_string_to_list(move))
move = ":6::(A+B):"
print(command_string_to_list(move))
move = ":2::A+B:"
print(command_string_to_list(move))
move = "RG :2::A+B:"
print(command_string_to_list(move))
move = ":4::A+B:"
print(command_string_to_list(move))
move = ":8::A+B:"
print(command_string_to_list(move))
move = ":2::3::6::A+B:"
print(command_string_to_list(move))
move = ":B+K:"
print(command_string_to_list(move))
move = ":6::B+K:"
print(command_string_to_list(move))
move = ":2::B+K:"
print(command_string_to_list(move))
move = ":4::B+K: or alternate inputs"
print(command_string_to_list(move))
move = "BT :B+K:"
print(command_string_to_list(move))
move = ":K+G:"
print(command_string_to_list(move))
move = ":A+K:"
print(command_string_to_list(move))
move = ":4::A+K:"
print(command_string_to_list(move))
move = ":4::(4):*:1::(1):*:7::(7)::aG:"
print(command_string_to_list(move))
move = ":6::(6):*:3::(3):*:9::(9)::B+K:"
print(command_string_to_list(move))
move = ":2::(2):*:8::(8)::B+K:"
print(command_string_to_list(move))
move = ":2::(2):*:8::(8)::A+K:"
print(command_string_to_list(move))
move = ":4::(4):*:1::(1):*:7::(7)::B+K:"
print(command_string_to_list(move))
move = ":4::(4):*:1::(1):*:7::(7)::(B+K):"
print(command_string_to_list(move))
move = ":2::3::6::A+K:"
print(command_string_to_list(move))
move = "WF :B::A+K:"
print(command_string_to_list(move))
move = "BKN :B+K:"
print(command_string_to_list(move))
move = "When :B+K: (or alternate inputs) is blocked"
print(command_string_to_list(move))
move = "STG :2::3::6::A+B:"
print(command_string_to_list(move))
move = ":(A+G):"
print(command_string_to_list(move))
move = ":A+G:"
print(command_string_to_list(move))
move = ":B+G:"
print(command_string_to_list(move))
move = ":(B+G):"
print(command_string_to_list(move))
move = ":2::3::6::A+B+K:"
print(command_string_to_list(move))
move = ":3::4::1::2::3::6::4::2::1::B+K:"
print(command_string_to_list(move))
move = "RG :4::(A+B+K):"
print(command_string_to_list(move))

