class Hangman:
    """
    this is a object of hangman game that save list and score
    """
    def __init__(self,number_list):
        self.number_list = number_list 
        self.score = 0
        self.num_lost = []
        self.num_play = []

    def create_field(self):
        for i in self.number_list:
            if i in self.num_play:
                print(f"{i}", end=" ")
            else:
                print("_", end=" ")

        for i in self.num_lost:
            print(i, end=" ")
        print()

    def count_score(self, num_guest):
        if num_guest in self.number_list:
            if num_guest not in self.num_play:
                self.num_play.append(num_guest)
                self.score += self.number_list.count(num_guest)
        elif num_guest not in self.number_list:
            if num_guest not in self.num_lost:
                self.num_lost.append(num_guest)

    def play(self):
        self.create_field
        for i in range(5):
            num = int(input())
            self.count_score(num)
            self.create_field()

            