
import re,traceback
from functools import partial
class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc())
    return f


# @O.k
# def testingFailure():
#   """this one must fail.. just to
#   test if the  unit test system is working"""
#   assert 1==2

@O.k
def testingSuccess():
  '''if this one fails, we have a problem!'''
  assert 1==1

@O.k
def pg5():
    """Multiline statements"""
    two_plus_three = 2 + \
        3
    assert two_plus_three == 2+ 3

@O.k
def pg6(my_reg_exp = "IHaveNumber0"):
    """Importing Modules"""
    # Using re module already imported above
    regex = re.compile("[0-9]")
    assert bool(regex.search(my_reg_exp)) == True

@O.k
def pg7():
    """Arithmetic - python division"""
    # Result without importing division from __future__
    assert bool(5 / 2 == 2.5) == False
    assert bool(5//2 == 2) == True

@O.k
def pg8():
    """Python functions are first-class"""
    def add (a, b):
        return a+b

    def fibo(c):
        if c<=1:
            return c
        # Functions can be passed as arguments to another function
        return add(fibo(c-1), fibo(c-2))

    assert fibo(6) == 8

@O.k
def pg9():
    """Python uses single backlashes to encode special char"""
    double_back_slash = "\\t"
    assert len(double_back_slash) == 2

@O.k
def pg10():
    """Using exceptions for Error handling"""
    try:
        print 0/0
    except ZeroDivisionError:
        assert True

@O.k
def pg11():
    """Checking 'in' operator"""
    list = [1,"Hi", [1,2,3]]
    assert (2 in list) == False

@O.k
def pg12():
    """Unpacking list"""
    _,y = [1,2]
    assert _ == 1

@O.k
def pg13():
    """Tuples are immutable"""
    my_tuple = (1,2, [1,2])
    second_tuple = (11,12)
    new_tuple = my_tuple.__add__(second_tuple)
    assert my_tuple != new_tuple

@O.k
def pg14():
    """Dictionaries"""
    grades = {"Dyuti": "A", "Xin": "A+"}
    assert len(grades.values())==2

@O.k
def pg15():
    """defaultdict usage"""
    from collections import defaultdict
    word_count = defaultdict(int)
    for word in ["this", "is", "a" "great", "idea", "but", "this", "is", "too", "long"]:
        word_count[word] += 1
    assert word_count["this"] == 2

@O.k
def pg16():
    """Counter"""
    from collections import Counter
    c = Counter("this is a great idea but this is too long".split())
    assert c["this"] == 2

@O.k
def pg17():
    """Sets for finding distinct elements"""
    list = [1,2,3,2,2]
    assert len(set(list)) == 3

@O.k
def pg18():
    """Testing python loops"""
    num = 0
    while num>0 :
        num -= 1
    assert num==0

@O.k
def pg19():
    """Boolean check"""
    assert bool(set()) == False
    assert bool({}) == False
    assert bool(3) == True
    assert 1 == True
    assert 0.0 == False

@O.k
def pg20():
    """All function test"""
    assert all([True, 0.1, {3}]) == True


@O.k
def pg22():
    """Sorting check and also the sequence matters in list unlike sets"""
    list_one = [2,3,1,4]
    list_two = [4,3,2,1]
    assert list_one != list_two
    assert list_one.sort() == list_two.sort()

@O.k
def pg23():
    """Pythonic way of transforming lists: List Comprehensions"""
    # to check growth of functions
    square_cube_pair = [(x*x,x*x*x)
                   for x in range(10)
                   ]
    assert square_cube_pair[3][1] == 27

@O.k
def pg24():
    """Lazy Dictionary access using Iterators"""
    # @Todo: Look if we can make dict with something similar to list comprehension
    my_dict = {1:2, 2:4, 3:6, 4:8}
    for key, val in my_dict.iteritems():
        assert val == 2*key

@O.k
def pg25():
    """Randomness"""
    import random
    x = random.randrange(1,3)
    y = random.randrange(4,7)
    assert x!=y

@O.k
def pg26():
    """Regular Expressions"""
    assert len(re.split("[a]", "banana")) == 4

@O.k
def pg27():
    """OOP: Asserting that each object has separate init called"""
    import random
    class Test:
        def __init__(self):
            # random.seed(5)
            self.val = {random.random()}
    obj1_Test = Test()
    obj2_Test = Test()
    assert obj1_Test.val != obj2_Test.val, "Will fail when random generates same number but should be rare"

@O.k
def pg28():
    """Partial and map function"""

    def filter(str):
        num_list = [int(num) for num in str.split() if num.isdigit()]
        return num_list
    list_filter = partial(map, filter)

    assert len(list_filter(["1 2 3 peter poll and marry", "3 2 1 go", "This is cool 2"])[2]) == 1

@O.k
def pg29():
    """Reduce implementation?"""
    my_list = [1,2,3,4]
    def multiply(x,y): return x*y
    my_reduced_list = reduce( multiply, my_list)
    def reduceFunc(func,list):
        a = 1
        for key in (list):
            a = func(a,key)
        return  a
    assert my_reduced_list == reduceFunc(multiply, my_list)

@O.k
def pg30():
    """Enumerate"""
    import copy

    my_list = [1,2,3,4]
    my_original_list = copy.deepcopy(my_list)
    for key, index in enumerate(my_list):
        if index%2 == 0:
            my_list.pop(key)
    assert len(my_original_list) == 2*len(my_list)

@O.k
def pg31():
    """Zip"""
    list_one = ['a','b','c']
    list_two= ['apple','banana']
    zip_list = zip(list_one, list_two)
    assert zip_list[0][1] == 'apple'

@O.k
def pg32():
    """Testing agrs"""
    def testArgs(*args):
        return len(args)
    assert testArgs(1,2,3,4) == 4
    return "Hello pg33"

@O.k
def pg33():
    """Arbitrary arguments to higher order function"""
    def higherOrderFunc(highArgs):
        def lowerOrderFunc(*args):
            print highArgs
        return lowerOrderFunc
    higherOrderFunc(1)

if __name__== "__main__":
  O.report()


