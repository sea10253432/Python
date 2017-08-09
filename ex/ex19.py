def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses! " % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

    
print "We can just give the function numbers directly:"
# 调用cheese_and_crackers，打印拥有的 cheese 和 cracker 数量
cheese_and_crackers(20, 30)


print "OR, we can use variable from our script:"
# amount_of_cheese 变量赋值，代表拥有的 cheeses 数量
amount_of_cheese = 10
# amount_of_crackers 变量赋值，代表拥有的 crackers 盒数
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 调用cheese_and_crackers函数，打印拥有的 cheeses 数量和 crackers 盒数
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
