# 这是一个模型，是在我第一次看过三体之后就有的一个想法，它模拟的是三体这本小说中的一个概念————黑暗森林
# 宇宙社会学的两大公理：第一，生存是文明的第一需要；第二，文明不断增长和扩张，但宇宙中的物质总量保持不变。
# 要想从这两条公理推论出宇宙社会学的基本图景，还有两个重要概念：猜疑链和技术爆炸。

# 简化模型：假设宇宙中有1000个恒星，且这些恒星的距离都足够远，远到足够忽略一些细节问题；
#          在这些恒星中随机诞生文明，并假定一个恒星只能有一个文明，但是一个文明可以拥有多个恒星（发展到一定程度）

import random

CIVIS = 10
POSSIBILITY = 10
STARS = 1000
TIMES = 50

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
            c.update_level()
            c.check_level_and_stars(civilizations)
            if c.level < 9:
                # 阶段0，慢慢成长，不进行探索
                continue
            elif c.level < 19:
                # 阶段1，凭着好奇心和探索欲，它开始探索宇宙，并且探索到的恒星会有助于自己的成长
                c.state = 1
                c.explore(stars)
            elif c.level < 29:
                # 阶段2，它知道了黑暗森林理论，开始变得小心谨慎，尽全力不暴露自己，并且慢慢发展
                continue
            elif c.level < 39:
                # 阶段3，它成为了宇宙中的强者，深谙宇黑暗森林法则，开始有意地清除被发现的文明，为自己的生存获取更大的空间
                c.explore(stars, 20)
            elif c.level < 99:
                # 阶段4，搜索更大的范围
                c.explore(stars, 50)
            else:
                # 最后阶段，搜索全范围
                c.explore(stars, STARS)
                        
class Civilization:
    def __init__(self, i):
        self.level = 0
        self.stars = 0
        self.id = i

    def update_level(self):
        self.level += 1
        self.level += self.stars

    def check_level_and_stars(self,civilizations):
        if self.stars == 0:
            print(f"{self.id} has been destroyed")
            civilizations.remove(self)
        print(f"文明编号：{self.id}，等级：{self.level}，恒星数量：{self.stars}")
    
    def explore(self, stars, limit=10):
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
            if stars[i].owner == None:
                self.stars += 1
                stars[i].owner = self
                print(f"{self.id} has found a new star")
            else:
                found_possibility = self.level - stars[i].owner.level
                if random.randint(0, 100) < found_possibility:
                    # 发现了一个文明，恒星易主，如果一个文明连最后一颗恒星都没有了，那么该文明消失
                    stars[i].owner.stars -= 1
                    set_ownership(self, stars[i])

        return None

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
    civilization.stars += 1

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

main()