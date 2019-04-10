*** Settings ***
Library    pylib.StudentLib
Variables   cfg.py

Suite Setup    add student   diaochan   貂蝉
        ...  ${g_grade_7_id}
        ...  ${suite_g7c1_classid}    132006789000
        ...  suite_student_id

Suite Teardown    delete student   ${suite_student_id}
