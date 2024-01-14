#!/usr/bin/python3
'''Unlock lockboxes module.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes can be unlocked.

    Args:
        boxes (list of lists): A list of boxes where each box contains keys
                               (indices) to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    num_boxes = len(boxes)
    seen_boxes = set([0])
    unprocessed_boxes = set(boxes[0]).difference(set([0]))

    while unprocessed_boxes:
        current_box_idx = unprocessed_boxes.pop()

        # Skip invalid box indices
        if not (0 <= current_box_idx < num_boxes):
            continue

        # Check if the box has not been processed yet
        if current_box_idx not in seen_boxes:
            # Add keys from the current box to unprocessed boxes
            unprocessed_boxes = unprocessed_boxes.union(boxes[current_box_idx])

            # Mark the current box as seen
            seen_boxes.add(current_box_idx)

    # Check if all boxes have been seen
    return num_boxes == len(seen_boxes)
