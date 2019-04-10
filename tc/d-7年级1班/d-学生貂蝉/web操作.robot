*** Settings ***
Library    pylib.WebOpLib
Library    pylib.TeacherLib
Variables  cfg.py

Suite Setup  open browser
Suite Teardown  close browser

*** Test Cases ***
老师登陆2 - tc005002
    ${addret}=  add teacher    kongzi2019111   孔子
            ...  ${g_subject_math_id}
            ...  ${suite_g7c1_classid}
            ...  139111666333  1302333@g.com  32052000233244
    should be true  $addret['retcode']==0

    teacher login  kongzi2019111   888888
    ${teachret}=   get teacher homepage info
    should be true  $teachret==['松勤学院0001', '孔子', '初中数学', '0', '0', '0']

    ${sturet}=  get teacher class students info

    should be true  $sturet=={'七年级1班': ['貂蝉']}

    [Teardown]  delete teacher  &{addret}[id]