class Bj:
    count = 0
    def __init__(self):
        self.person = int(50) # 초기값으로 기본칩을 사람과 컴퓨터에게 50개씩 배정을 해줍니다.
        self.ai = int(50)
        Bj.count += 1

# 랜덤으로 3장씩 주는 메소드
    def threecard(self) :
        import random
        n_list = [i for i in range(1, 22)] # 1부터 21까지의 숫자가 들어있는 카드라고 생각되는 리스트를 만듭니다.
        self.card_person = random.sample(n_list, 3) # .sampel을 이용해서 랜덤으로 3장의 카드를 뽑는다.
        print('사람 : ', self.card_person) # 본인의 카드 확인
        self.card_ai = random.sample(n_list, 3) # .sampel을 이용해서 랜덤으로 3장의 카드를 뽑는다.
        # print('컴터 : ', self.card_ai)
        return self.card_person, self.card_ai


# 베팅을 할지 말지 결정하는 메소드
    def pos_bet(self) :
        self.dec = str(input('베팅을 할시에 y, 안하면 n :')) # 베팅을 할지 말지 결정
        if self.dec == 'y' :
            self.bet = int(input('베팅을 걸 갯수를 적으세요.')) # 베팅을 할 칩의 갯수 결정
            self.total_person = 0 # 카드의 총합을 구하기 위한 기본 세팅
            self.total_ai = 0 # 카드의 총합을 구하기 위한 기본 세팅
            # print(self.card_person)
            # print(self.card_ai)
            # print(self.bet)
            for i in self.card_person : # 사람 카드의 총합 구하기
                self.total_person += i
            for i in self.card_ai : # 컴퓨터 카드의 총합 구하기
                self.total_ai += i

            print('사람 :', self.card_person, '총합 :',self.total_person)
            print('컴퓨터 :', self.card_ai, '총합 :', self.total_ai)

            if int(self.total_person) > int(self.total_ai) : # 총합이 사람이 더 크면
                self.person += self.bet # 베팅을 한 만큼의 칩을 사람이 얻게된다.
                self.ai -= self.bet # 베팅을 한 만큼의 칩을 컴퓨터가 뻇긴다.
                print('사람이 이겼습니다')
                print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))

            elif int(self.total_person) == int(self.total_ai) : # 총합이 같다면
                print('무승부')
                print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))
                
            else : # 총합이 사람이 더 작으면
                self.person -= self.bet # 베팅을 한 만큼의 칩을 사람이 뺏긴다.
                self.ai += self.bet # 베팅을 한 만큼의 칩을 컴퓨터가 얻게긴다.
                print('사람이 졌습니다')
                print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))

        else : # 베팅을 안할시에는 그냥 넘어감
            pass

            
# 게임의 횟수를 알려주는는 메소드
    @classmethod
    def game_count(cls) :
        print('{}번째 게임입니다'.format(cls.count))

# 게임 종료시 승패를 구분하는 메소드
    def finalchip(self) :
        print('---게임 종료---')
        if self.person > self.ai : # 총 칩의 갯수가 사람이 더 많으면
            print('사람이 이겼습니다.')
            print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))

        elif self.person == self.ai : # 총 칩의 갯수가 같으면
            print('무승부')
            print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))

        else : # 총 칩의 갯수가 사람이 더 적으면
            print('사람이 졌습니다.')
            print('사람 : {}, 컴퓨터 : {}'.format(self.person, self.ai))

#게임을 하는 메소드
    def play_game(self) :
        game = 1
        print('기본 칩 사람람 50개, 컴퓨터 50개')
        while game <= 5 : # 5판까지 반복
            Bj.game_count()
            play.threecard()
            play.pos_bet()
            print('')
            print('')
            print('')
            game += 1
            Bj.count += 1
        play.finalchip()

play = Bj()
play.play_game()
