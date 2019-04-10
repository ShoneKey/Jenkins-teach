from pprint import pprint

from selenium import webdriver
from cfg import *
import time


class WebOpLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def open_browser(self):
        self.wd = webdriver.Chrome(g_chrome_driver_path)
        self.wd.implicitly_wait(10)

    def close_browser(self):
        self.wd.quit()

    def teacher_login(self, username, password):
        self.wd.get(g_teacher_login_url)
        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        self.wd.find_element_by_id('home_div')

    def get_teacher_homepage_info(self):
        self.wd.find_element_by_css_selector('a[href="#/home"]>li').click()
        # 确保首页打开
        self.wd.find_element_by_id('home_div')
        eles = self.wd.find_elements_by_css_selector('.row .ng-binding')
        pprint([ele.text for ele in eles])
        return [ele.text for ele in eles]

    def get_teacher_class_students_info(self):
        self.wd.find_element_by_css_selector('.main-menu ul>li:nth-of-type(4)').click()
        self.wd.find_element_by_css_selector('a[href="#/student_group"] span').click()
        time.sleep(2)

        classeles = self.wd.find_elements_by_css_selector('a[ng-click*="showClassStudent"]')
        classStudentTab = {}
        self.wd.implicitly_wait(0)
        for ele in classeles:
            grade_info = ele.text.replace(' ', '')
            ele.click()
            time.sleep(3)
            stu_eles = self.wd.find_elements_by_css_selector('tbody span.ng-binding')
            stu_names = [ele.text for ele in stu_eles]

            classStudentTab[grade_info] = stu_names
        self.wd.implicitly_wait(10)
        pprint(classStudentTab)
        return classStudentTab

    # 老师布置作业
    def teacher_deliver_task(self, examname):
        # 点击作业
        self.wd.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(2)').click()
        # 点击创建作业
        self.wd.find_element_by_css_selector('a[ng-click="show_page_addexam()"] span').click()
        # 输入作业名称
        self.wd.find_element_by_id('exam_name_text').send_keys(examname)
        time.sleep(1)
        # 从题库选择题目
        self.wd.find_element_by_id('btn_pick_question').click()
        time.sleep(2)

        self.wd.switch_to.frame('pick_questions_frame')
        # 勾选习题，只要选3个
        for i in range(3):
            select_btns = self.wd.find_elements_by_class_name('btn_pick_question')
            select_btns[i].click()
            time.sleep(0.5)
        # 点击确认
        self.wd.find_element_by_css_selector('div[onclick*="_pickQuestionOK"]').click()
        # 切回主HTML
        self.wd.switch_to.default_content()
        # 页面发生变动，给页面加载时间
        time.sleep(1)
        # 点击确认添加
        self.wd.find_element_by_id('btn_submit').click()

        # 选择发布给学生
        self.wd.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button:nth-child(2)').click()
        # 页面加载
        time.sleep(2)

        # 保留当前窗口handle，后面要切回来
        mainWindow = self.wd.current_window_handle

        # 切换到下发学习任务窗口
        for handle in self.wd.window_handles:
            self.wd.switch_to.window(handle)
            if '下发学习任务' == self.wd.title:
                print('成功进入下发学习任务窗口')
                break

        time.sleep(1)

        # 勾选学生
        select_stu_btns = self.wd.find_elements_by_css_selector('a[ng-click*="selectAll"]')
        select_stu_btns[0].click()

        # 确定下发
        self.wd.find_element_by_class_name('btn-outlined').click()
        time.sleep(1)

        # 点击确定
        self.wd.find_element_by_css_selector('button[ng-click="dispatchIt()"]').click()
        time.sleep(1)

        # 任务编号
        task_msg = self.wd.find_element_by_class_name('bootstrap-dialog-message').text
        task_id = task_msg[-4:]
        # 再点击确定
        self.wd.find_element_by_class_name('btn-default').click()
        # 窗口自动关闭，回到主窗口
        self.wd.switch_to.window(mainWindow)

        return task_id

    # 学生登陆
    def student_login(self, username, password):
        self.wd.get(g_student_login_url)
        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()
        self.wd.find_element_by_css_selector('a[href="#/home"]')

    # 学生做作业
    def student_do_job(self):
        # 点击我的任务
        self.wd.find_element_by_css_selector('a[href="#/task_manage"]>li').click()
        time.sleep(1)
        # 点击第一个任务
        self.wd.find_element_by_css_selector('tr:nth-child(1) button[ng-click*="viewTask"]').click()
        # 全部选A
        firstAnwsers = self.wd.find_elements_by_css_selector('.btn-group>button:nth-child(1)')
        for one in firstAnwsers:
            one.click()
            time.sleep(1)
        # 点击提交
        self.wd.find_element_by_css_selector('button[ng-click*="saveMyResult"]').click()
        # 等待确认提示框弹出
        time.sleep(1)
        # 确认提交
        self.wd.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button:nth-child(2)').click()
        # 等待结尾动画弹出
        time.sleep(2)

    # 老师检查作业
    def teacher_check_last_student_task(self):
        # 登陆后进入已发布作业
        self.wd.get('http://ci.ytesting.com/teacher/index.html#/task_manage?tt=1')
        time.sleep(1)
        # 查看第一个结果
        self.wd.find_element_by_css_selector('tbody>tr:nth-child(1) a[ng-click="trackTask(task)"]').click()
        time.sleep(1)
        # 点击第一个学生
        self.wd.find_element_by_css_selector('button[ng-click*="viewTaskTrack"]').click()
        main_window = self.wd.current_window_handle
        for handle in self.wd.window_handles:
            self.wd.switch_to.window(handle)
            if '查看作业' == self.wd.title:
                print('成功进入查看作业页面')
                #给页面加载时间
                time.sleep(1)
                break
        eles = self.wd.find_elements_by_css_selector('.myCheckbox input:checked + span')
        anwsers = [ele.find_element_by_xpath('./ ..').text.replace(' ', '') for ele in eles]
        print(anwsers)
        self.wd.switch_to.window(main_window)
        return anwsers


if __name__ == '__main__':
    webop = WebOpLib()
    webop.open_browser()
    webop.teacher_login('jcyrss', 'sdfsdf5%')
    webop.teacher_deliver_task('作业2222')
    webop.student_login('ycg', 'sdfsdf5%')
    webop.student_do_job()
    webop.teacher_login('jcyrss', 'sdfsdf5%')
    webop.teacher_check_last_student_task()
    webop.close_browser()
