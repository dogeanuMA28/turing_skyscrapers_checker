def create_final():
    transitions = []
    transitions.append("init: start\naccept: Y\n")
    # lista cu toate permutatrile posibile
    permutations = ["141232", "142132", # 1_2
                    "141323", "142313", "143123", # 1_3
                    "143214", # 1_4
                    "231241", "232141", # 2_1
                    "214232", "221432", "224132", "231422", "232412", "234122", # 2_2
                    "214323", "224313", "234213", # 2_3
                    "313241", "321341", "323141", # 3_1
                    "312432", "313422", "323412", # 3_2
                    "412341" # 4_1
                    ]
    # ca sa scapam de comenzile duplicate
    duplicates = []
    # starea de inceput
    for symb1 in "1234#":
        if symb1 == "#":
            transitions.append(f"start, {symb1}\ntwr_find_, {symb1}, >\n")
        else:
            transitions.append(f"start, {symb1}\nstart, {symb1}, >\n")
    # gaseste primul turn
    for symb1 in "1234":
        transitions.append(f"twr_find_, {symb1}\ntwr_find_{symb1}, {symb1}, >\n")
        transitions.append(f"twr_find_{symb1}, :\ntwr_find_{symb1}, :, >\n")
    # calculam fiecare varianta pana la atingerea caracterului ":"
    for s in permutations:
        for i in range(1, len(s) - 1):
            transitions.append(f"twr_find_{s[:i]}, {s[i]}\ntwr_find_{s[:(i+1)]}, {s[i]}, >\n")
    # calculam si pentru ultimul turn
    for s in permutations:
        transitions.append(f"twr_find_{s[:(len(s) - 1)]}, :\ntwr_find_{s[:(len(s) - 1)]}, :, >\n")
        transitions.append(f"twr_find_{s[:(len(s) - 1)]}, {s[len(s) - 1]}\ntwr_find_{s}, {s[len(s) - 1]}, >\n")
        transitions.append(f"twr_find_{s}, #\nskip, #, >\n")
    # pentru a verifica daca am terminat cu liniile
    for symb in "1234":
        transitions.append(f"skip, {symb}\nskip{symb}, {symb}, >\n")
        transitions.append(f"skip{symb}, :\ntwr_find_{symb}, :, >\n")
        for i in "1234":
            transitions.append(f"skip{symb}, {i}\nreset, {i}, <\n")
    # reset
    for symb in "1234#:_X":
        if symb == "_":
            transitions.append(f"reset, {symb}\nfind_twr_col_, {symb}, >\n")
        else:
            transitions.append(f"reset, {symb}\nreset, {symb}, <\n")

    # pentru coloane
    for symb in "1234#X":
        if symb == "#":
            transitions.append(f"find_twr_col_, {symb}\nY, {symb}, -\n")
        elif symb == "X":
            transitions.append(f"find_twr_col_, {symb}\nfind_twr_col_, X, >\n")
        else:
            transitions.append(f"find_twr_col_, {symb}\ngoto_line_{symb}, X, >\n")
    # pentru a merge pe prima linie
    for symb1 in "1234":
        for symb2 in "1234:#_X":
            if symb2 == ":":
                transitions.append(f"goto_line_{symb1}, {symb2}\nfind_twr_col_{symb1}, {symb2}, >\n")
            else:
                transitions.append(f"goto_line_{symb1}, {symb2}\ngoto_line_{symb1}, {symb2}, >\n")
    # merge la urmatorul element din coloana
    for s in permutations:
        for i in range(1, len(s) - 1):
            transitions.append(f"find_twr_col_{s[:i]}, {s[i]}\nskip_line_{s[:(i + 1)]}, X, >\n")
            transitions.append(f"find_twr_col_{s[:i]}, X\nfind_twr_col_{s[:i]}, X, >\n")
            for j in "1234":
                transitions.append(f"skip_line_{s[:i]}, {j}\nskip_line_{s[:i]}, {j}, >\n")
                transitions.append(f"new_line_{s[:i]}, {j}\nnew_line_{s[:i]}, {j}, >\n")
            transitions.append(f"skip_line_{s[:i]}, :\nnew_line_{s[:i]}, :, >\n")
            transitions.append(f"skip_line_{s[:i]}, #\nskip_line_{s[:i]}, #, >\n")
            transitions.append(f"new_line_{s[:i]}, :\nfind_twr_col_{s[:i]}, :, >\n")
            transitions.append(f"new_line_{s[:i]}, #\nnew_line_{s[:i]}, #, >\n")
    # pentru ultimele verificari
    for s in permutations:
        for j in "1234":
            transitions.append(f"skip_line_{s[:(len(s) - 1)]}, {j}\nskip_line_{s[:(len(s) - 1)]}, {j}, >\n")
            transitions.append(f"new_line_{s[:(len(s) - 1)]}, {j}\nnew_line_{s[:(len(s) - 1)]}, {j}, >\n")
        transitions.append(f"skip_line_{s[:(len(s) - 1)]}, :\nnew_line_{s[:(len(s) - 1)]}, :, >\n")
        transitions.append(f"new_line_{s[:(len(s) - 1)]}, #\nfind_twr_col_{s[:(len(s) - 1)]}, #, >\n")
        transitions.append(f"find_twr_col_{s[:(len(s) - 1)]}, {s[len(s) - 1]}\nreset, X, <\n")
        transitions.append(f"find_twr_col_{s[:(len(s) - 1)]}, X\nfind_twr_col_{s[:(len(s) - 1)]}, X, >\n")
    # filtram liniile duplicate
    for transition in transitions:
        if transition in duplicates:
            continue
        else:
            duplicates.append(transition)
    # cream comenzile
    with open("skyscrapers_final.tms", "w") as f:
        for transition in duplicates:
            f.write(transition + "\n")

create_final()