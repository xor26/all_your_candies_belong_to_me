class CandyStealer:

    def __init__(self):
        # erase prev output file
        open('out', 'w').close()

    @staticmethod
    def get_all_cases():
        with open("in", "r") as fp:
            in_data = fp.read()

            # get rid of excess data
            in_data = in_data.strip()
            in_data = in_data.split("\n")[1:]
            filtered_data = []
            for i in range(len(in_data)):
                if i % 2 != 0:
                    filtered_data.append(in_data[i])

            # convert strings to int lists
            test_cases = []
            for data_row in filtered_data:
                data_row = data_row.split(" ")
                test_cases.append(data_row)

            return test_cases

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

    def get_all_heaps_variants(self, t_case):
        combinations_count = (2 ** len(t_case)) - 1  # all possible combinations count
        default_mask = ["0" for x in range(len(t_case))]
        default_mask = "".join(default_mask)
        masks = []

        for i in range(1, combinations_count):
            mask = bin(i)
            mask_str = str(mask)[2:]
            mask_str = default_mask[:-len(mask_str)] + mask_str
            masks.append(mask_str)

        heaps_variants = []
        for mask in masks:
            heap1, heap2 = self.get_heaps_by_mask(t_case, mask)
            heaps_variants.append([heap1, heap2])

        return heaps_variants

    def sasha_add(self, n1, n2):
        n1 = bin(int(n1))[2:]
        n2 = bin(int(n2))[2:]
        return int(n1, 2) ^ int(n2, 2)

    def get_sasha_heap_sum(self, heap):
        sum = 0
        for num in heap:
            sum = self.sasha_add(sum, num)
        return sum

    @staticmethod
    def get_heap_sum(heap):
        sum = 0
        for num in heap:
            sum += int(num)
        return sum

    @staticmethod
    def write_result(max_sum, case_num):
        with open("out", "a") as fp:
            addition = "NO" if max_sum == -1 else str(max_sum)
            fp.write("Case #" + str(case_num) + ": " + addition + "\n")

    def run(self):
        t_cases = self.get_all_cases()
        case_num = 0
        for t_case in t_cases:
            case_num += 1
            max_sum = -1
            for heap1, heap2 in self.get_all_heaps_variants(t_case):
                heap1_sum_by_sasha_opinion = self.get_sasha_heap_sum(heap1)
                heap2_sum_by_sasha_opinion = self.get_sasha_heap_sum(heap2)
                if heap1_sum_by_sasha_opinion == heap2_sum_by_sasha_opinion:
                    variant_max_sum = max(sum(heap1), sum(heap2))
                    if variant_max_sum > max_sum:
                        max_sum = variant_max_sum
            self.write_result(max_sum, case_num)


if __name__ == "__main__":
    CandyStealer().run()
