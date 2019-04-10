*** Settings ***
Library    pylib.WebOpLib
Library    pylib.TeacherLib
Variables  cfg.py

Suite Setup  open browser
Suite Teardown  close browser

*** Test Cases ***
老师发布作业1 - tc005101
    teacher login   haiwen   888888
    teacher deliver task   松勤自动化作业001

    student login   diaochan   888888
    student do job

    teacher login   haiwen   888888
    ${taskret}=   teacher check last student task
    should be true  $taskret==['A', 'A', 'A']

