def test_function(name, lastname, status = False):
    print(name, lastname, status)

test_function('michal', 'kruczkowski')
test_function(lastname='kruczkowski', name='michal')
test_function(status=True, lastname='kruczkowski', name='michal')

def lab_results(*grades):
    for grade in grades:
        print(grade, end=" ")
    print()
def lab_named_results(**named_grades):
    print(named_grades)

lab_results(5)
lab_named_results(lab1  = 5, lab3 = 3)

