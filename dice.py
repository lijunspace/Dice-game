class Dice():
    def __init__(self,x,y):   # x:是求和 y:是分开
        self.x = x
        self.y = y


    def big_small(self):
        self.x = int(self.x)
        if (self.x >= 4) and (self.x <= 10):
            return 'small'
        elif (self.x >= 11 and self.x <= 17):
            return 'big'
        else:
            return 'none'

    def all_same_dice(self):
        self.y = str(self.y)
        if self.y.count(self.y[0]) == 3:
            return True #'1 wins 150'
        else:
            return False



    def two_same_dice(self):
        self.y = str(self.y)
        if (self.y.count(self.y[0]) == 2) or (self.y.count(self.y[1]) == 2):
            return True        #'1 wins 8'
        else:
            return False


    def dice_num(self):
        self.x = int(self.x)
        if (self.x == 17) or (self.x == 4):
            return '1 wins 50'
        elif (self.x == 16) or (self.x == 5):
            return '1 wins 18'
        elif (self.x == 15) or (self.x == 6):
            return '1 wins 14'
        elif (self.x == 14) or (self.x == 7):
            return '1 wins 12'
        elif (self.x == 13) or (self.x == 8):
            return '1 wins 8'
        else:
            return '1 wins 6'

    def specific_dice(self):
        self.y = str(self.y)
        if ('1' in self.y) and ('2' in self.y):
            return '1 wins 5'
        
        elif ('2' in self.y) and ('4' in self.y):
            return '1 wins 5'
        
        elif ('1' in self.y) and ('4' in self.y):
            return '1 wins 5'
        
        elif ('2' in self.y) and ('3' in self.y):
            return '1 wins 5'
        
        elif ('3' in self.y) and ('4' in self.y):
            return '1 wins 5'

        elif ('2' in self.y) and ('5' in self.y):
            return '1 wins 5'

        elif ('3' in self.y) and ('5' in self.y):
            return '1 wins 5'

        elif ('2' in self.y) and ('6' in self.y):
            return '1 wins 5'

        elif ('4' in self.y) and ('5' in self.y):
            return '1 wins 5'

        elif ('3' in self.y) and ('6' in self.y):
            return '1 wins 5'

        elif ('1' in self.y) and ('5' in self.y):
            return '1 wins 5'

        elif ('1' in self.y) and ('6' in self.y):
            return '1 wins 5'

        elif ('4' in self.y) and ('6' in self.y):
            return '1 wins 5'

        elif ('5' in self.y) and ('6' in self.y):
            return '1 wins 5'

        elif ('1' in self.y) and ('3' in self.y):
            return '1 wins 5'
        else:
            return 'none'











