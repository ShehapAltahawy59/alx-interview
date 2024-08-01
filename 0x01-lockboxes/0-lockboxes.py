#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    if(boxes and type(boxes) is list):
        n = len(boxes)
        keys = {x for x in boxes[0]}
        keys.add(0)
        opened_boxes = [0]
        for i in opened_boxes:
            for x in boxes[i]:
                if x < n:
                    keys.add(x)
                    if (x not in opened_boxes):
                        opened_boxes.append(x)
        return len(keys) == len(boxes)
    else:
        return False
