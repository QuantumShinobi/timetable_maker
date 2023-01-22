class S:
    def __init__(self):
        for i in range(10):
            # globals()[f'{self}.class_{i}'] = [i, (i*2)]
            exec("self.{} = '{}'".format(f"grade_{i}", [i, 2j]))
            print(self.grade_2)

    def test(self):
        for i in range(10):
            print(exec(f"self.grade_{i} "))


a = S()
a.test()

# Create your tests here.
