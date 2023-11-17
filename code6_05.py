class Hero:

    #コンストラクタの作り方
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def sleep(self,hours):
        print("{}は{}時間寝た!".format(self.name,hours))
        self.hp += hours

#ゲーム開始
print("スッキリファンタジーXII ～金色の理想郷～")
h = Hero("松田",100)
h.sleep(3)
print("{}のHPは現在{}です".format(h.name,h.hp))