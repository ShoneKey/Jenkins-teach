*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py

Suite Setup    add teacher    haiwen   海文
           ...  ${g_subject_math_id}
           ...  ${suite_g7c1_classid}
           ...  180111222333  1301@g.com  3205200019856565
           ...  suite_math_teacher_id

Suite Teardown    delete teacher   ${suite_math_teacher_id}
