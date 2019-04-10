*** Settings ***
Library    pylib.TeacherLib
Library    pylib.SchoolClassLib
Variables   cfg.py


*** Test Cases ***
添加老师2 - tc001002
# 添加一个 老师 教7年级1班 科学

    ${addRet}=    add teacher    kongzi2019   孔子
            ...  ${g_subject_science_id}
            ...  ${suite_g7c1_classid}
            ...  139111222333  1302333@g.com  32052000233244

    should be true     $addRet['retcode']==0

#列出老师，检验一下
    ${listRet}=    list teacher

    teacherlist should contain   &{listRet}[retlist]
            ...  kongzi2019   孔子   &{addRet}[id]
            ...  ${suite_g7c1_classid}
            ...  139111222333  1302333@g.com  32052000233244

    [Teardown]    delete teacher   &{addRet}[id]



添加老师3 - tc001003


#列出老师
    ${listRet1}=    list teacher


# 添加 老师 教7年级1班 科学
    ${addRet}=    add teacher    haiwen   海文2
           ...  ${g_subject_science_id}
           ...  ${suite_g7c1_classid}
           ...  139000222333  1302333@g.com  32052000233244

    should be true     $addRet['retcode']==1
    should be true     $addRet['reason']=="登录名 haiwen 已经存在"

#列出老师，检验一下
    ${listRet2}=    list teacher

    should be equal   ${listRet1}    ${listRet2}



删除老师1 - tc001081


#列出老师
    ${listRet1}=    list teacher


#删除老师，不存在的ID
    ${delRet}=   delete teacher   99999999
    should be true     $delRet['retcode']==404
    should be true     $delRet['reason']==u"id 为`99999999`的老师不存在"

#列出老师，检验一下
    ${listRet2}=    list teacher

    should be equal   ${listRet1}    ${listRet2}



删除老师2 - tc001082
#列出老师
    ${listRet1}=    list teacher
# 添加 老师 教7年级1班 科学
    ${addRet}=    add teacher    kongzi2019   孔子
            ...  ${g_subject_science_id}
            ...  ${suite_g7c1_classid}
            ...  139111222333  1302333@g.com  32052000233244

    should be true     $addRet['retcode']==0
#删除老师
    delete teacher   &{addRet}[id]
#列出老师，检验一下
    ${listRet2}=    list teacher

    should be equal   ${listRet1}    ${listRet2}


修改老师1 - tc001051
    ${delRet}=   modify teacher   99999999
    should be true     $delRet['retcode']==1
    should be true     $delRet['reason']=="id 为`99999999`的老师不存在"

修改老师2 - tc001052
#添加科学老师
    ${addRet}=    add teacher    kongzi2019   孔子
            ...  ${g_subject_science_id}
            ...  ${suite_g7c1_classid}
            ...  139111222333  1302333@g.com  32052000233244
    should be true     $addRet['retcode']==0

#添加七年级二班
    ${classret}=   add school class   ${g_grade_7_id}   2班    60
    should be true     $classret['retcode']==0

#修改老师，真实姓名和授课班级，改为两个班
    ${modifyret}=   modify teacher  &{addRet}[id]
            ...   孔丘   ${g_subject_science_id}
            ...   ${suite_g7c1_classid},&{classret}[id]

    should be true  $modifyret['retcode']==0
#检查修改结果
    ${listRet2}=  list teacher
    teacherlist should contain   &{listRet2}[retlist]
            ...  kongzi2019   孔丘   &{addRet}[id]
            ...  ${suite_g7c1_classid},&{classret}[id]
            ...  139111222333  1302333@g.com  32052000233244

    [Teardown]  run keywords  delete teacher  &{addRet}[id]  AND
                ...   delete school class  &{classret}[id]