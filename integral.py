"""
以下sympyでの積分計算
#sin、log、exp等はsympyに入っている。
"""

from sympy import *

#inputで積分
def integral():
    #関数入力
    print("関数を入力してください")
    function=input()

    #xについて積分する
    x = Symbol('x')

    #積分実行
    result = integrate(function,x)
    print(result)
    plot(result)



#引数で積分
def integral2(function):
    #xについて積分する
    x = Symbol('x')

    #積分実行
    result = integrate(function,x)
    print(result)
    plot(result)



#定積分
def constegral():
    #関数入力
    print("関数を入力してください")
    function=input()

    #範囲指定
    print("下端、上端の順に入力")
    down,up = map(float,input().split())

    #xについて積分する
    x = Symbol('x')

    #積分実行
    result = integrate(function,(x,down,up))
    print(result)
    return result



#重積分
def double():
    #関数入力
    print("関数を入力してください")
    function=input()

    #xとyについて積分する
    x=Symbol('x')
    y=Symbol('y')

    print("xの下端、上端とyの下端、上端")
    down1,up1,down2,up2 = map(float,input().split())

    #積分実行
    result=integrate(function,(x,down1,up1),(y,down2,up2))
    print(result)
    return result



#ガウス積分
def gauss():
    x=Symbol('x')
    a=Symbol('a')

    function=exp(-a*x**2)

    #積分実行
    result=integrate(function,(x,-oo,oo))
    print(result)
