*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py


*** Test Cases ***
添加老师1 - tc001001
# 添加 老师
    ${addRet}=    add teacher    tuobahong1   拓跋宏1
                ...  ${g_subject_math_id}
                ...  ${suite_g7c1_classid}
                ...  13000000321  130133@g.com  320520001

    should be true     $addRet['retcode']==0

#列出老师，检验一下
    ${listRet}=    list teacher

    teacherlist should contain   &{listRet}[retlist]
                 ...  tuobahong1   拓跋宏1   &{addRet}[id]
                 ...   ${suite_g7c1_classid}
                 ...  13000000321  130133@g.com  320520001

    [Teardown]    delete teacher   &{addRet}[id]
