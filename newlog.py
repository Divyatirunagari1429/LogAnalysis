#!/usr/bin/env python3

import psycopg2


def connect():
    try:
        lgn_base = psycopg2.connect(dbname="news")
        lgn_key = lgn_base.cursor()
        return lgn_base, lgn_key
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def themes():
    lgn_base, lgn_key = connect()
    lgn_ans = """SELECT nov.title, tms.eyepoint
        FROM themes as tms, articles as nov
        WHERE replace(tms.path, '/article/', '') = nov.slug
        LIMIT 3"""
    lgn_key.execute(lgn_ans)
    if(lgn_ans):
        lgn_out = lgn_key.fetchall()
        lgn_base.commit()
        lgn_base.close()

    # print top three favorite articles
        for head, seen in lgn_out:
            print '"{}" --> "{} views"'.format(head, seen)
    else:
        print("error")


def wordsmith():
    lgn_base, lgn_key = connect()
    lgn_ans2 = """SELECT authors.name, SUM(themes.eyepoint) as toteyep
        FROM themes, articles, authors
        WHERE authors.id=articles.author
        and replace(themes.path, '/article/', '') = articles.slug
        GROUP BY authors.name
        ORDER BY toteyep desc"""
    lgn_key.execute(lgn_ans2)
    if(lgn_ans2):
        lgn_out = lgn_key.fetchall()
        lgn_base.commit()
        lgn_base.close()

    # print authors of most popular articles
        for smith, seen in lgn_out:
            print '"{}" --> "{} views"'.format(smith, seen)
    else:
        print("error")


def mistake():
    # Select which days had errors
    lgn_base, lgn_key = connect()
    lgn_ans3 = """SELECT to_char(date, 'YYYY FMMonth DD'),
    misscall
    FROM strengthcall
    WHERE misscall > 1.0"""
    lgn_key.execute(lgn_ans3)
    if(lgn_ans3):
        lgn_out = lgn_key.fetchall()
        lgn_base.commit()
        lgn_base.close()

    # print days with more than 1% error request rate
        for lgn_dt, mist in lgn_out:
            print '"{}" --> "{}% error"'.format(lgn_dt, mist)
    else:
        print("error")


if __name__ == '__main__':
    print ("\nTop three favorite articles:")
    themes()
    print ("\nMost popular article authors:")
    wordsmith()
    print ("\nDays where more than 1% of requests lead to errors:")
    mistake()
