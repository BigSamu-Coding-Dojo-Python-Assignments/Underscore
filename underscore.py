class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i])==True:
                return iterable[i]
    def filter(self, iterable, callback):
        output = []
        for i in range(len(iterable)):
            if callback(iterable[i])==True:
                output.append(iterable[i])
        return output
    def reject(self, iterable, callback):
        output = []
        for i in range(len(iterable)):
            if callback(iterable[i])==False:
                output.append(iterable[i])
        return output
# you just created a library with 4 methods!

# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
areEvens = _.map([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(areEvens) # should return [False, True, False, True, False, True]
firstEven = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(firstEven) # should return 2
filterEven = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(filterEven) # should return [2,4,6]
rejectEven = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(rejectEven) # should return [1,3,5]

multiplyByTwo=_.map([1,2,3], lambda x: x*2) 
print(multiplyByTwo)# should return [2,4,6]
greaterThanFour = _.find([1,2,3,4,5,6], lambda x: x > 4)
print(greaterThanFour) # should return the first value that is greater than 4, which is in this case 5


