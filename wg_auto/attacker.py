# coding:utf-8

import sys
def test_a0():
    from wg_auto.a0_general_basic.http_basics import http_post1, http_post2
    print(http_post1().text)
    print(http_post2().text)


def test_a1(flag1=False):
    from wg_auto.a1_inject.sql_injection.intro import sql2_test, sql3_test, sql4_test, \
        sql5_test, sql9_test, sql10_test, sql11_test, sql12_test, sql13_test
    if flag1:
        print(sql2_test().text)
        print(sql3_test().text)
        print(sql4_test().text)
        print(sql5_test().text)
        print(sql9_test().text)
        print(sql10_test().text)
        print(sql11_test().text)
        print(sql12_test().text)
        print(sql13_test().text)

    from wg_auto.a1_inject.sql_injection.advanced import sql3a_test
    print(sql3a_test().text)


if __name__ == '__main__':
    # test_a0()
    test_a1()

