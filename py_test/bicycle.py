class Bicycle:
    def run(self, mile):
        # 自行车骑行里程
        print(f"自行车骑行了：{mile}km")

class EBicycle(Bicycle):
    def __init__(self, valume):
        # 电动车初始电量
        self.valume = valume
        print(f"电动车初始电量为：{self.valume}")

    def fill_charge(self, vol):
        # 充电电量
        self.valume = self.valume + vol
        print(f"电动车充电后电量为：{self.valume}")

    def elec_run(self, mile):
        """
        :param mile: 电动车骑行总路程
        :return:
        """
        elec_mile = self.valume * 10   # 所有电量总骑行路程
        rema_mile = mile - elec_mile    # 剩余电量路程
        if rema_mile > 0:
            vol = rema_mile / 10
            print(f"剩余电量{vol}")
            print(f"电动自行车骑行了:{elec_mile}km")

        else:
            self.run(elec_mile)     # 电使用完成后，脚踏骑行的里程


a = EBicycle(20)    # 原始电量20
a.fill_charge(5)    # 充电5
a.elec_run(678)     # 电动车总骑行路程