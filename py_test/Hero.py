class Hero:             # 定义英雄父类
    hp = 0
    power = 0
    name = ""
    def fight(self, enemy_hp, enemy_power):
        my_pk_hp = self.hp - enemy_power        # 我PK后的血量
        enemy_pk_ph = enemy_hp - self.power     # 敌人PK后的血量
        if my_pk_hp > enemy_hp:
            print(f"{self.name}赢了")
        elif my_pk_hp == enemy_hp:
            print("打平了")
        else:
            print("敌人赢了")


class Jinx(Hero):       # 继承父类，编写具体英雄
    hp = 2000
    power = 210
    name = "Jinx"


class EZ(Hero):          # 继承父类，编写具体英雄
    hp = 1100
    power = 190
    name = "EZ"

jinx = Jinx() # 调用Jinx类
ez = EZ()   # 调用EZ类

jinx.fight(ez.hp, ez.power)     # 使用Jinx的fight方法
ez.fight(jinx.hp, jinx.power)   # 使用Jinx的fight方法