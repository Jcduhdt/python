class Song(object):

    def __init__(self,lyrics):
         # 为什么必须是 __init__  不能是 _init_   后者会报错
         # 必须加变量 self 是为了不产生歧义
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
