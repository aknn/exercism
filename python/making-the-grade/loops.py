"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    return [round(num) for num in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grade_range = highest - 40
    base_interval = grade_range // 4
    remainder = grade_range % 4

    len_A = base_interval + (1 if remainder > 0 else 0)
    len_B = base_interval + (1 if remainder > 1 else 0)
    len_C = base_interval + (1 if remainder > 2 else 0)
    len_D = base_interval + (1 if remainder > 3 else 0)

    A_lower = highest - (len_A - 1)
    B_lower = A_lower - len_B
    C_lower = B_lower - len_C
    D_lower = C_lower - len_D

    return [D_lower, C_lower, B_lower, A_lower]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    order = sorted(zip(student_scores, student_names), key=lambda x: x[0], reverse=True)
    return [f"{rank}. {name}: {score}" for rank, (score, name) in enumerate(order, 1)]


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if student[1] == 100:
            return student
    return []
