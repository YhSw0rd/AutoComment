# import uiautomator2 as u2
# import time
# import random

# if __name__ == '__main__':
#     d = u2.connect()
#     d.set_fastinput_ime(True)
#     f = open("comment.txt",encoding = "utf-8")
#     comment = f.readline()
#     commentLen = len(comment)
#     # comments = ['高端','给力','不错','支持','放心使用','爱了','喜欢']
#     for x in range(10000):
#         # time.sleep(random.randint(1,1))
#         time.sleep(1)
#         start = random.randint(1,commentLen)
#         subLen = random.randint(2,4)
#         result = comment[start: start+subLen if start+subLen < commentLen else commentLen ]
#         d(resourceId="com.ss.android.ugc.aweme:id/cqn").wait(timeout=60.0) 
#         d(resourceId="com.ss.android.ugc.aweme:id/cqn").click()
#         time.sleep(.1)
#         d.clear_text()
#         d.send_keys(result)
#         # d.send_keys(comments[random.randint(0,len(comments)-1)]*random.randint(2,4))
#         time.sleep(.3)
#         d(resourceId="com.ss.android.ugc.aweme:id/jnt").wait(timeout=60.0) 
#         d(resourceId="com.ss.android.ugc.aweme:id/jnt").click()
        
import uiautomator2 as u2
import time
import random

if __name__ == '__main__':
    d = u2.connect()
    d.set_fastinput_ime(True)
    f = open("comment.txt",encoding = "utf-8")
    comment = f.readline()
    commentLen = len(comment)
    realComment = ['女生支持',
                '女生喜欢',
                '女生爱了',
                '女生买了',
                '女友支持',
                '女友爱了',
                '女友买了',
                '女友喜欢',
                '宝贝划算',
                '宝贝实惠',
                '宝贝精美',
                '宝贝低调',
                '精美实惠',
                '精美划算',
                '颜色精美',
                '颜色艳丽',
                '颜色低调',
                '包装低调',
                '质量不错',
                '质量很好',
                '宝贝不错',
                '宝贝很好',
                '支持',
                '爱了',
                '喜欢',
                '赞赞赞',
                '经济',
                '实惠',
                '优惠多多',
                '价格实惠',
                '价格公道',
                '包装不错',
                '包装美丽',
                '做工很好',
                '做工精美',
                '做工新颖',
                '组合实惠',
                '组合经济',
                '组合优惠',
                '组合划算',
                '划算',
                '物超所值',
                '质量好',
                '绝对支持',
                '物美价廉',
                '商品很棒',
                '价格很棒',
                '颜色喜欢',
                '颜色爱了爱了',
                '颜色爱了',
                '形状喜欢',
                '形状新颖',
                '形状创新',
                '料子不错',
                '做工不错',
                '收藏了',
                '准备下单了',
                '小巧精致',
                '精致小巧',
                '方便',
                '方便使用',
                '使用方便',
                '试用很好',
                '试用爱了',
                '准备再买俩',
                '给家人买俩',
                '多买划算',
                '多买实惠']

    maxPercent = 0
    for x in range(10000):
        # 如果于5等于0，检查有效率
        if (x+1) % 5 == 0:
            d(resourceId="com.ss.android.ugc.aweme:id/g3").click()
            d(textContains="有效评论率").wait(10.0)
            resultPercent = d(textContains="有效评论率").get_text()
            resultPercent = int(resultPercent[-3:-1])
            if resultPercent < maxPercent:
                time.sleep(90)
            maxPercent = resultPercent
            d.click(0.509, 0.231)
        print("有效率"+str(maxPercent)+"%")
        start = random.randint(1,commentLen)
        subLen = random.randint(2,4)
        result = realComment[x%len(realComment)]+comment[start: start+subLen if start+subLen < commentLen else commentLen ]
        d(resourceId="com.ss.android.ugc.aweme:id/cqn").wait(timeout=60.0) 
        d(resourceId="com.ss.android.ugc.aweme:id/cqn").click()
        time.sleep(.1)
        d.clear_text()
        time.sleep(.1)
        d.send_keys(result)
        time.sleep(.2)
        d(resourceId="com.ss.android.ugc.aweme:id/jnt").wait(timeout=60.0) 
        d(resourceId="com.ss.android.ugc.aweme:id/jnt").click()
        
