from doopl.factory import *

def solveWithCplex(box_size,object_list,numobj):
    # Generation des donnees :
    pb = [(numobj,box_size)]
    listobjects = [(1,object_list[0])]
    for i in range (numobj-1):
        listobjects.append((i+2,object_list[i+1]))

    # Creation du modele OPL a partir du fichier .mod
    with create_opl_model(model="bin-packing-model.mod") as opl:
        opl.apply_ops_file("bin-packing.ops")
        opl.set_input("pb", pb)
        opl.set_input("listobjects",listobjects)

        # Solve
        opl.mute()
        opl.run()
        results = opl.get_table('results')
        print(results)