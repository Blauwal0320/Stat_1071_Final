import random
import math

p = 0.558304495
var_p = p * (1-p)
pi = 0
var_pi = 0

count = 0

class Couple():
    def __init__(self, id, edu_h, edu_w):
        self.id = id
        self.edu_husband = edu_h
        self.edu_wife = edu_w

def main():
    couples_list = create_105_list()
    n = input("民國 105 年總共有 145348 對新人搭上幸福列車 \n請輸入欲抽樣對數：")
    x = input("請輸入欲抽樣次數：")

    for i in range( int(x) ):
        pi = sampling( int(n), couples_list )
        var_pi = var_p / int(n)
        μ = [ pi-1.96 * math.sqrt(var_pi) , pi+1.96 * math.sqrt(var_pi) ]

        print("-" * 80)
        print("π：",pi,"(樣本夫妻學歷相等之比率)") 
        print("var(π)：",var_pi)
        print("在 95% 信心水準之下，抽樣誤差為正負", 1.96 * math.sqrt(var_pi) * 100 , "個百分點")
        print("信賴區間為：", μ)
        print("母體平均數 p 是否落在此信賴區間中？", μ[0] <= p and μ[-1] >= p)

        if μ[0] <= p and μ[-1] >= p :
            global count
            count += 1

    print("=" * 80)
    print("在", x ,"次抽樣中，母體平均數（夫妻同學歷比率） p 落在此信賴區間中的次數為：", count)



def sampling(n, List):
    success = 0
    for i in range(n):
        couple = List[random.randint(0,145348)]
        if couple.edu_husband == couple.edu_wife:
            success += 1

    pi = success / n
    return pi  

def create_105_list():
    couples = []
    for i in range (55289): 
        couples.append( Couple(i, "大學以上", "大學以上") )
    for i in range (5412):
        couples.append( Couple(i, "大學以上", "專科學校") )
    for i in range (9391):
        couples.append( Couple(i, "大學以上", "高　　中") )
    for i in range (1941):
        couples.append( Couple(i, "大學以上", "國　　中") )
    for i in range (414):
        couples.append( Couple(i, "大學以上", "國小以下") )

    for i in range (3244): 
        couples.append( Couple(i, "專科學校", "大學以上") )
    for i in range (2245):
        couples.append( Couple(i, "專科學校", "專科學校") )
    for i in range (3821):
        couples.append( Couple(i, "專科學校", "高　　中") )
    for i in range (1172):
        couples.append( Couple(i, "專科學校", "國　　中") )
    for i in range (329):
        couples.append( Couple(i, "專科學校", "國小以下") )

    for i in range (12731): 
        couples.append( Couple(i, "高　　中", "大學以上") )
    for i in range (4257):
        couples.append( Couple(i, "高　　中", "專科學校") )
    for i in range (17668):
        couples.append( Couple(i, "高　　中", "高　　中") )
    for i in range (6952):
        couples.append( Couple(i, "高　　中", "國　　中") )
    for i in range (1332):
        couples.append( Couple(i, "高　　中", "國小以下") )

    for i in range (2461): 
        couples.append( Couple(i, "國　　中", "大學以上") )
    for i in range (1143):
        couples.append( Couple(i, "國　　中", "專科學校") )
    for i in range (6905):
        couples.append( Couple(i, "國　　中", "高　　中") )
    for i in range (5428):
        couples.append( Couple(i, "國　　中", "國　　中") )
    for i in range (1073):
        couples.append( Couple(i, "國　　中", "國小以下") )
    
    for i in range (219): 
        couples.append( Couple(i, "國小以下", "大學以上") )
    for i in range (108):
        couples.append( Couple(i, "國小以下", "專科學校") )
    for i in range (649):
        couples.append( Couple(i, "國小以下", "高　　中") )
    for i in range (646):
        couples.append( Couple(i, "國小以下", "國　　中") )
    for i in range (519):
        couples.append( Couple(i, "國小以下", "國小以下") )
    return couples

main()