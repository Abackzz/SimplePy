class Answer(object):
    def SumofTwo(self, nums, target):
        current = main_index[begin][0] + main_index[end][0]
        if current == target:
            return [main_index[begin][1], main_index[end][1]]
        elif current < target:
            begin += 1
        else:
            end -= 1


if __name__ == '__main__':
    # begin
    s = Answer()
    print s.SumofTwo([1, 3, 5], 7)
