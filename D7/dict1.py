"""定义和使用字典"""

def main():
    scores = {'罗浩':95, '白元芳':78, '狄仁杰':82}
    print(scores['罗浩'])
    print(scores['狄仁杰'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 75
    scores.update(冷面=67, 方启河 = 85)
    print(scores)

    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('罗浩'))
    print(scores)

    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()


