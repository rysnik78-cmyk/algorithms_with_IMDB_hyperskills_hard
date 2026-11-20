# write your code here
from scipy.constants import value


class MovieBase:
    def __init__(self):
        self.movie_base = []

    def add_movies_from_csv_file(self, path):
        with open(path, 'r', encoding="utf-8") as csv_file:
            data_read = csv_file.read().splitlines()
            # print(len(data_read))
            for line in data_read:

                title = ','.join(line.split(',')[0:-1]).strip('"')

                rating = float(line.split(',')[-1])
                # if rating == 6:
                #     print(title, '-', rating)
                # if title in self.movie_base:
                #     print(len(line.split(',')))
                #     print(line)
                #     print(title)
                #     print(rating)

                self.movie_base.append([title, rating])
        # print(len(self.movie_base))


    def print_base(self):
        for title, rating in self.movie_base:
            print(title,'-', rating)


    def sort_base(self, ascending = True):
        swapped = True
        base_len = len(self.movie_base)
        while swapped:
            swapped = False
            for i in range(base_len - 1):
                # print('swapping', self.movie_base[i], 'with', self.movie_base[i + 1])
                if self.movie_base[i][1] > self.movie_base[i+1][1]:
                    # print('swapping', self.movie_base[i], 'with', self.movie_base[i+1])
                    temp = self.movie_base[i]
                    self.movie_base[i] = self.movie_base[i+1]
                    self.movie_base[i+1] = temp
                    swapped = True

    def merge_sort_base(self, base_to_sort, ascending = True):

        # return when 1 element
        if len(base_to_sort) == 1:
            return base_to_sort

        # merging two elements
        elif len(base_to_sort) == 2:
            # print('base_init', base_to_sort)
            if (base_to_sort[0][1] <= base_to_sort[1][1]) and ascending:
                # print(base_to_sort)
                return base_to_sort
            elif (base_to_sort[0][1] >= base_to_sort[1][1]) and not ascending:
                # print(base_to_sort)
                return base_to_sort
            else:
                # print([base_to_sort[1], base_to_sort[0]])
                return [base_to_sort[1], base_to_sort[0]]

        # merging more then 2 elements
        # TODO?
        elif len(base_to_sort) > 2:
            # if len(base_to_sort) == 3:
            #     print('input_base',base_to_sort)
            mid = len(base_to_sort) // 2
            left_list = self.merge_sort_base(base_to_sort[:mid])
            # print('left_list',left_list)
            right_list = self.merge_sort_base(base_to_sort[mid:])
            # print('right_list',right_list)

            return_base = []
            left_index = 0
            right_index = 0
            while left_index < mid and right_index < len(base_to_sort) - mid:
                # print(right_index)
                if left_list[left_index][1] <= right_list[right_index][1] and ascending:
                    return_base.append(left_list[left_index])
                    left_index += 1

                elif left_list[left_index][1] >= right_list[right_index][1] and not ascending:
                    return_base.append(left_list[left_index])
                    left_index += 1
                else:
                    return_base.append(right_list[right_index])
                    right_index += 1

            if left_index < mid:
                return_base.extend(left_list[left_index:mid])
            elif right_index < len(base_to_sort) - mid:
                return_base.extend(right_list[right_index:])
            # if len(base_to_sort) == 3:
            #     # print('out_put_base', return_base)
            return return_base


    def binary_search(self, value, low, high):
        if low == high:
            if self.movie_base[low][1] == value:
                return self.movie_base[low][0] + ' - ' + str(self.movie_base[low][1]) + '\n'
            else:
                return ''
        else:
            mid = (low + high) // 2
            if self.movie_base[mid][1] == value:
                if low == mid:
                    return self.movie_base[mid][0] + ' - ' + str(self.movie_base[mid][1]) + '\n' + self.binary_search(value, mid + 1, high)
                elif mid > low:
                    return self.binary_search(value, low, mid - 1) + self.movie_base[mid][0] + ' - ' + str(self.movie_base[mid][1]) + '\n' + self.binary_search(value, mid + 1, high)
            elif self.movie_base[mid][1] > value:
                return self.binary_search(value, low, mid - 1)
            else:
                return self.binary_search(value, mid + 1, high)


def main():
    movie_base = MovieBase()
    movie_base.add_movies_from_csv_file('movies.csv')
    # movie_base.print_base()
    # print('-------------------------------------------------------------')
    movie_base.movie_base = movie_base.merge_sort_base(movie_base.movie_base)
    # movie_base.print_base()
    print(movie_base.binary_search(6, 0, len(movie_base.movie_base)))

if __name__ == '__main__':
    main()
