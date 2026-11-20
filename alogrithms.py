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

def main():
    movie_base = MovieBase()
    movie_base.add_movies_from_csv_file('movies.csv')
    # movie_base.print_base()
    # print('-------------------------------------------------------------')
    movie_base.sort_base()
    movie_base.print_base()


if __name__ == '__main__':
    main()
