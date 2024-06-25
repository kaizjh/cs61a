# 这是一个模型，是在我第一次看过三体之后就有的一个想法，它模拟的是三体这本小说中的一个概念————黑暗森林
# 宇宙社会学的两大公理：第一，生存是文明的第一需要；第二，文明不断增长和扩张，但宇宙中的物质总量保持不变。
# 要想从这两条公理推论出宇宙社会学的基本图景，还有两个重要概念：猜疑链和技术爆炸。

# 简化模型：假设宇宙中有1000个恒星，且这些恒星的距离都足够远，远到足够忽略一些细节问题；
#          在这些恒星中随机诞生文明，并假定一个恒星只能有一个文明，但是一个文明可以拥有多个恒星（发展到一定程度）

import random

CIVIS = 10
LEVEL = 10
POSSIBILITY = 10
# STARS 必须是 LEVEL 的十倍或更大
STARS = 100
TIMES = 100

def main():
    # 初始化
    stars = generate_stars()
    civilizations = generate_civilizations(stars)
    # 开始模拟    
    for i in range(TIMES):
        print("__________________________________________________")
        print(f"第{i}轮模拟：")
        for s in stars:
            s.check_id_and_owner()

        for c in civilizations:
            if c.found != 0:
                c.found -= 1
                continue
            else:
                c.update_level()
                c.check_level_and_stars(civilizations)
                if c.level < LEVEL // 10:
                    # 阶段0，慢慢成长，不进行探索
                    continue
                elif c.level < LEVEL // 5:
                    # 阶段1，凭着好奇心和探索欲，它开始探索宇宙，并且探索到的恒星会有助于自己的成长
                    c.explore(stars)
                elif c.level < LEVEL // 2:
                    # 阶段2，它知道了黑暗森林理论，开始变得小心谨慎，尽全力不暴露自己，并且慢慢发展
                    c.explore(stars)
                elif c.level < LEVEL:
                    # 阶段4，搜索更大的范围
                    c.explore(stars, STARS // 5)
                else:
                    # 最后阶段，搜索全范围
                    c.explore(stars, STARS)
                        
class Civilization:
    def __init__(self, i):
        self.found = 0
        self.id = i
        self.level = 0
        self.stars = {}
        
    def update_level(self):
        if self.found == 0:
            self.level += 1 + len(self.stars)

    def check_level_and_stars(self,civilizations):
        if len(self.stars) <= 0:
            print(f"{self.id} has been destroyed")
            civilizations.remove(self)
        print(f"文明编号：{self.id}，等级：{self.level}，恒星数量：{len(self.stars)}")
    
    def explore(self, stars, limit=STARS//10):
        # 文明只在一定范围内进行探索，根据等级增加范围
        # 防止范围溢出
        if self.id - limit < 0:
            start = 0
        else:
            start = self.id - limit
        if self.id + limit > STARS:
            end = STARS
        else:
            end = self.id + limit
        # 正式开始探索
        for i in range(start, end):
            # 一轮模拟只能执行一次探索，无论是发现文明还是发现无主恒星都会break
            if stars[i].owner == None:
                set_ownership(self, stars[i])
                print(f"{self.id} has found a new star")
                break
            else:
                found_possibility = self.level - stars[i].owner.level
                if random.randint(0, 100) < found_possibility:
                    # 保证传入found函数的参数1一定是高等级的文明（或者两者相等）
                    if self.level >= stars[i].owner.level:
                        found(self, stars[i].owner)
                    else:
                        found(stars[i].owner, self)
                    break
                   

class Stars:
    def __init__(self, i):
        self.id = i
        self.owner = None
    def check_id_and_owner(self):
        print(f"恒星编号：{self.id}，拥有者编号：{self.owner and self.owner.id}")
        
# 生成STARS个恒星
def generate_stars():
    stars = []
    for i in range(STARS):
        stars.append(Stars(i))
    return stars

# 设置恒星与文明间的关系
def set_ownership(civilization, star):
    star.owner = civilization
    num = len(civilization.stars)
    civilization.stars[num + 1] = star

# 在已经生成好的恒星上随机生成文明
def generate_civilizations(stars):
    civilizations = []
    for i in range(0, CIVIS):
        j = random.randint(10, STARS - 10)
        for k in range(j - 10, j + 10):
            if stars[k].owner == None:
                a = Civilization(i)
                a.level = random.randint(0, 10)
                set_ownership(a, stars[k])
                civilizations.append(a)
                break
    return civilizations

# 在一个文明发现另一个文明之后，由于猜疑链，两个文明可能会对峙、僵持，期间可能触发技术爆炸，但是结局只有一死一生
def found(civ1, civ2):
    level1 = civ1.level
    level2 = civ2.level
    # 由前面传参步骤可知，level1 >= level2, gap >= 0
    gap = level1 - level2
    if level1 < LEVEL // 5:
        # 此时两个文明都不清楚黑暗森林，由于猜疑链两者对峙
        civ1.found = civ2.found = gap // 2
        # 用等级的随机提升来模拟技术爆炸
        civ1.level += random.randint(1, civ1.level * 2)
        civ2.level += random.randint(1, civ2.level * 2)
    elif level1 < LEVEL // 2 and gap < 19:
        # 此时高等级文明已经知道黑暗森林,但等级差距不太大，所以会产生技术爆炸
        civ1.found = civ2.found = 1
        civ1.level += random.randint(1, civ1.level // 2)
        civ2.level += random.randint(1, civ2.level // 2)
    elif level1 < LEVEL // 2 and gap > 19:
        # 差距太大，还没产生技术爆炸，高等文明就发动攻击了
        civ1.found = civ2.found = 1
    else:
        # 其他情况，全部开战
        civ1.found = civ2.found = 1
    
    # 根据技术爆炸后的情况决定战斗结果，只能有一个文明活下来！
    new_gap = civ1.level - civ2.level
    if new_gap < 0:
        # 根据概率解决战斗，领先越多，赢的概率越大，如果new_gap < -LEVEL // 2，那么civ2胜利的概率为100%
        if random.randint(0, LEVEL) < LEVEL // 2 + new_gap:
            win(civ1, civ2)
            set_ownership(civ1, )
        else:
            win(civ2, civ1)
    else:
        # 如果new_gap > LEVEL // 2，那么civ1胜利的概率为100%
        if random.randint(0, LEVEL) < LEVEL // 2 - new_gap:
            win(civ2, civ1)
        else:
            win(civ1, civ2)

# 一次战斗只解决一颗恒星的问题，失败文明还有东山再起的机会
# 这个函数出了问题，我需要确定civ1 的恒星信息，这样他输掉了战争之后就可以确定叫他交出恒星
# 这样应该需要civilization和star建立双向关系才好
def win(winner, loser):
    set_ownership(winner, loser.stars.pop(len(loser.stars)))
    
main()