####################################################################################

def first_fit(box_size,object_list):
    box_list=[0]
    for object_it in object_list:
        j=0
        while j<len(box_list) and object_it > box_size-box_list[j]:
            j+=1
        if j==len(box_list):
            box_list.append(object_it)
        else:
            box_list[j]+=object_it
    return len(box_list)

def first_fit_dec(box_size,object_list):
    object_list.sort()
    object_list.reverse()
    return first_fit(box_size,object_list)

####################################################################################

def next_fit(box_size,object_list):
    box_list=[0]
    for object_it in object_list:
        if object_it < box_size-box_list[-1]:
            box_list[-1]+=object_it
        else:
            box_list.append(object_it)
    return len(box_list)

def next_fit_dec(box_size,object_list):
    object_list.sort()
    object_list.reverse()
    return next_fit(box_size,object_list)

####################################################################################

def best_box(single_object,box_size,box_list_state):
    best_box = [-1,box_size]
    for i in range(len(box_list_state)):
        gap = box_size-box_list_state[i]
        if gap >= single_object:
            if gap-single_object < best_box[1]:
                best_box = [i,gap-single_object]
    return best_box[0]

def best_fit(box_size,object_list):
    box_list=[0]
    for object_it in object_list:
        chosen_box = best_box(object_it,box_size,box_list)
        if chosen_box==-1:
            box_list.append(object_it)
        else:
            box_list[chosen_box]+=object_it
    return len(box_list)

def best_fit_dec(box_size,object_list):
    object_list.sort()
    object_list.reverse()
    return best_fit(box_size,object_list)

####################################################################################
