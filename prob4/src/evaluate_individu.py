from haunted_field import Haunted_Field

class Evaluate_ind(object):
    def __init__(self, field):
        """
        this class is to test a set of directions ( the genom of the individu ) , in that field
        and calculate the final score and state that he can attempt
        :param field: the haunted field that we are gonna test
        :type field: Haunted_Field
        """
        self.field = field
        self.paths = "" # this variable should be set after
        self.position = ()
        self.states = {"_" : "life", "M" : "monster", "*":"blocked"}

    def set_path(self, paths):
        """
        update the set of directions to be tested in that field
        :param paths: the set of directions that we are gonna test
        :type paths: str
        """
        self.paths = paths # the genome of the individu
        self.position = (1, self.field.get_width()//2) # first position of the cell
        self.visited = 1
        self.used_s = {self.position}

    def get_border(self):
        """
        calculate the number that correspond to the motif of the player.
        :return: an integer from 0 to 243
        :rtype: int
        """
        l, c = self.position
        borders = [(l,c-1),(l+1,c-1),(l+1,c),(l+1, c+1),(l,c+1)]
        s_borders = [self.field.get_cell(x[0], x[1]) for x in borders]
        s_borders = ''.join(s_borders).replace("M","1").replace("_","0").replace("*","2")[::-1] # transform borders to a number in base 3

        return int(s_borders, 3)

    def next_pos(self):
        """
        get the next position of the player depending on its border
        """
        l, c = self.position
        borders_i = self.get_border()
        direction = self.paths[borders_i]
        if direction == "U":
            self.position = (l-1, c)
        elif direction == "D":
            self.position = (l+1, c)
        elif direction == "L":
            self.position = (l, c-1)
        else:
            self.position = (l, c+1)

    def state(self):
        """
        get the current state of the cell, monster, blocked or life
        :return: the current state
        :rtype: str
        """
        l, c = self.position
        w, h = self.field.get_width(), self.field.get_height()
        i_state = self.field.get_cell(l, c)
        c_s = self.states[i_state]
        if c_s == "life":
            self.visited += 1
            self.used_s.add((l,c))
        if c_s == "life" and l == h:
            c_s = "success"
        return c_s

    def score(self, i_state):
        """
        calculate the score of the player
        :param i_state: the current state of the player
        :type i_state: str

        :return: a integer that correspond to the score of the player
        :rtype: int
        """
        l, c = self.position
        w, h = self.field.get_width(), self.field.get_height()
        used = len(self.used_s)
        sc = used + l*w
        if i_state == "life" and self.visited >= w*h//2: # so if he visited w*h//2 it is gonna stop
            
            return sc
        elif i_state == "success":
            sc = sc + (w*h - used)*10
        elif i_state == "life" and l != h:
            return None # in that case the game didn't end yet
        elif i_state == "monster":
            sc = sc + (h - l) * 20
        else: # blocked
            sc = sc + (h - l) * 2
        return sc

    def complete_test(self):
        """
        this method will advance the player until he is blocked, monster, success or living but do many steps, and it will calculate the score and the state of the final result
        :return: a tuple that contains the final score and the final state of the player
        :rtype: tuple
        """
        self.next_pos()
        s = self.state()
        sc = self.score(s)
        if sc != None:
            return (sc, s)
        else:
            return self.complete_test()
