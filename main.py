class CandyStealer:

    def __init__(self):
        # erase prev output file
        open('out', 'w').close()

    @staticmethod
    def get_next_case():
        with open("in", "r") as fp:
            in_data = fp.read()
            # get rid of excess data
            in_data = in_data.strip()
            in_data = in_data.split("\n")[1:]
            for i in range(len(in_data)):
                if i % 2 != 0:
                    t_case = in_data[i].split(" ")
                    t_case = [int(x) for x in t_case]
                    yield t_case

    @staticmethod
    def sasha_add(n1, n2):
        n1 = bin(int(n1))[2:]
        n2 = bin(int(n2))[2:]
        return int(n1, 2) ^ int(n2, 2)

    def get_sasha_heap_sum(self, heap):
        heap_sum = 0
        for num in heap:
            heap_sum = self.sasha_add(heap_sum, num)
        return heap_sum

    @staticmethod
    def write_result(max_sum, case_num):
        with open("out", "a") as fp:
            addition = "NO" if max_sum == -1 else str(max_sum)
            fp.write("Case #" + str(case_num) + ": " + addition + "\n")

    @staticmethod
    def get_heaps_by_mask(t_case, mask):
        heap1 = []
        heap2 = []
        for i in range(len(mask)):
            if mask[i] == "0":
                heap1.append(int(t_case[i]))
            else:
                heap2.append(int(t_case[i]))
        return heap1, heap2

    def run(self):
        case_num = 0
        for t_case in self.get_next_case():
            case_num += 1
            combinations_count = (2 ** (len(t_case) - 1))  # all possible heaps
            default_mask = ["0" * len(t_case)]
            default_mask = "".join(default_mask)
            max_gain = -1
            for i in range(1, combinations_count):
                mask = bin(i)[2:]
                mask = default_mask[:-len(mask)] + mask
                heap1, heap2 = self.get_heaps_by_mask(t_case, mask)
                if self.get_sasha_heap_sum(heap1) == self.get_sasha_heap_sum(heap2):
                    current_gain = max(sum(heap1), sum(heap2))
                    if current_gain > max_gain:
                        max_gain = current_gain
            self.write_result(max_gain, case_num)


if __name__ == "__main__":
    CandyStealer().run()
