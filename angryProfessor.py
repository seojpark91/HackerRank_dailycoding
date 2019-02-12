def angryProfessor(k, a):
    students = len(list(filter(lambda x: x<=0, a)))
    if k <= students:
        return "NO"
    return "YES"