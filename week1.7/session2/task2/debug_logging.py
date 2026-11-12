# Week 1.7, Session 2: Task 2 - logging

import logging


def calculate_average(scores):
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)

    logger = logging.getLogger()
    logger.info("calculate_average(): started")

    total_score = sum(scores)
    total_assignments = len(scores)

    # add debug logging here:
    logger.debug(f"Total score: {total_score}, total assignments: {total_assignments}")

    average = total_score / total_assignments
    
    # add debug logging here: 
    logger.debug(f"Calculated average: {average}")

    return round(average, 2)


print(calculate_average([85, 90, 88]))
# Expected Output: 87.67
# Actual Output:   87.0