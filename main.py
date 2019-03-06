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
    def write_result(result, case_num):
        with open("out", "a") as fp:
            fp.write("Case #" + str(case_num) + ": " + result + "\n")

    @staticmethod
    def is_win_exist(candy_bag):
        heap_sum = 0
        for candy in candy_bag:
            heap_sum = bin(int(heap_sum))[2:]
            candy = bin(int(candy))[2:]
            heap_sum = int(heap_sum, 2) ^ int(candy, 2)

        if heap_sum == 0:
            return True
        return False

    def run(self):
        case_num = 0
        for t_case in self.get_next_case():
            result = "NO"
            if self.is_win_exist(t_case):
                case_num += 1
                min_candy = int(min(t_case))
                all_candy_sum = sum(t_case)
                result = str(all_candy_sum - min_candy)

            self.write_result(result, case_num)


if __name__ == "__main__":
    CandyStealer().run()
