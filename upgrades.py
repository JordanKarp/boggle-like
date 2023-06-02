# from collections import namedtuple
import csv
from dataclasses import dataclass
from tools import clear, inputNumber
from colored_terminal import returnBold, returnStrike


@dataclass
class Upgrade:
    id: str
    name: str
    price: int
    unlocked: bool
    remove_after: bool


class UpgradeSystem:
    def __init__(self, player):
        self.player = player
        self.consumables = {}
        self.perks = {}

    def load_upgrades(self, upgrade_file):
        with open(upgrade_file, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            for id, name, price, unlocked, remove in csv_reader:
                u = unlocked == "True"
                r = remove == "True"
                if u and not r:
                    self.consumables[id] = Upgrade(id, name, int(price), u, r)
                elif r:
                    self.perks[id] = Upgrade(id, name, int(price), u, r)
                else:
                    print("import didnt work")
                    print(Upgrade(id, name, int(price), u, r))

    def buy(self, upgrade_id):
        clear()
        self.player.show_player_header()
        proceed = False
        if self.player.score >= self.consumables[upgrade_id].price:
            self.player.score -= self.consumables[upgrade_id].price
            print(f"{self.consumables[upgrade_id].name} purchased!")
            proceed = True
        else:
            print(f"Not enough points to buy {self.consumables[upgrade_id].name}.")
        if proceed:
            match upgrade_id:
                case "1_free":
                    self.player.freebies += 1
                case "5_sec":
                    self.player.level_time += 5
                case "inc_score":
                    choice = inputNumber("Which word length? ", [2, 10])
                    self.player.score_mult[choice] += 0.1
                case "red_win":
                    self.player.win_percent -= 0.01
                case "1_el":
                    self.player.extra_life += 1
                # case 'rem_two':
                #     self.player.min_length = 3

        self.buy_again()

    def buy_again(self):
        print("Buy something else?")
        print("1. Yes, go back to upgrades.")
        print("2. No, go to next round.")
        choice = inputNumber("> ", [1, 2])
        match choice:
            case 1:
                self.show()
                self.purchase_prompt()

    def unlock(self, upgrade_id):
        self.perks[upgrade_id].unlocked = True
        self.buy_again()

    def purchase_prompt(self):
        print("What would you like to purchase?")
        choice = inputNumber("> ", [1, 9])
        match choice:
            case 1:
                self.buy("1_free")
            case 2:
                self.buy("5_sec")
            case 3:
                self.buy("inc_score")
            case 4:
                self.buy("red_win")
            case 5:
                self.buy("1_el")
            case 6:
                self.unlock("rem_two")
            case 7:
                self.unlock("add_time")
            case 8:
                self.unlock("order_ans")
            case 9:
                self.unlock("un_5")

    def show(self):
        clear()
        self.player.show_player_header()
        # Print Consumables
        print("#   ", returnBold("Consumable Name".ljust(30)), returnBold("Prices"))
        for num, u in enumerate(self.consumables.values(), 1):
            n = f"{str(num)}."
            name_price = f"{u.name.ljust(30)} {u.price}"
            print(f"{n.ljust(4)} {name_price}")
        print()

        # Print Perks
        print("#   ", returnBold("Perk Name".ljust(30)), returnBold("Prices"))
        for num, u in enumerate(self.perks.values(), len(self.consumables) + 1):
            n = f"{str(num)}."
            name_price = f"{u.name.ljust(30)} {u.price}"
            if u.unlocked:
                print(f"{n.ljust(4)} {returnStrike(name_price)}")
            else:
                print(f"{n.ljust(4)} {name_price}")
        self.purchase_prompt()


# u = UpgradeSystem()
# u.load_upgrades('data/upgrades.csv')
# for key, value in u.consumables.items():
#     print(key, '->', value)

# print('-----')
# for key, value in u.perks.items():
#     print(key, '->', value)

# u.buy()
