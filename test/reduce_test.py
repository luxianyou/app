from functools import reduce
'''
用法：只能处理一个iter,init为初始化值，执行顺序为：先将iter的第一个值和init进行func处理，
处理结果在与iter的第二个值进行func处理，直到结束
reduce(func,iter,init)
'''
r  = reduce(lambda x,y: x + y, [2,3,4,5,6],1)
print(r)