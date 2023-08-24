comensal ="Santiago"

def burguer(bread, meat, cheese):
    return comensal + " wants a burguer with " + bread + " bun " + meat + " and " +cheese + " cheese " 


combo1 = burguer("wheat",  "bacon", "feta")
combo2 = burguer("corn","ground beef","blue")

if comensal == "Santiago":
    print(combo2)
else:
    print(combo1)




