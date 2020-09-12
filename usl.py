from bll import StudentManagerController
from model import *


class StudentManagerView:
    """
            学生管理视图：主要负责界面逻辑
    """
    def __init__(self):
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("1) 添加学生信息" + "\n" +
              "2) 显示学生信息" + "\n" +
              "3) 删除学生信息" + "\n" +
              "4) 修改学生信息" + "\n" +
              "5) 根据成绩升序排列" + "\n" +
              "6) 结束所有操作并清除数据"
              )

    def __select_menu(self):
        """
            用户选择界面
        :return: True表示结束所有操作并清除数据。
        """
        order_index = input("请输入您的指令选项: ")
        if order_index == "1":
            self.__input_students()
            return False
        elif order_index == "2":
            self.__output_students(self.__controller.stu_list)
            return False
        elif order_index == "3":
            self.__delete_student()
            return False
        elif order_index == "4":
            self.__modify_student()
            return False
        elif order_index == "5":
            self.__output_students_order_by_score()
            return False
        elif order_index == "6":
            print("感谢您的使用！")
            return True
        else:
            print("指令错误！请重新输入指令！")
            self.__select_menu()
            return False

    def __input_students(self):
        """
            添加新学生信息
        """
        name = input("请输入学生的姓名，输入\"end\"结束添加过程：")
        if name == "end":
            print("添加完成！")
            return
        age = self.__input_integer("请输入学生的年龄：")
        score = self.__input_integer("请输入学生的成绩：")
        new_stu = StudentModel(name, age, score)
        self.__controller.add_student(new_stu)
        self.__input_students()

    def __input_integer(self,message):
        while True:
            try:
                return int(input(message))
            except:
                print("输入有误")

    def __output_students(self,stu_list):
        """
            显示已存学生信息。
        """
        if self.__controller.check_empty():
            print("列表中无学生信息。")
        else:
            for student in stu_list:
                print("学生id：%d, 姓名：%s, 年龄：%d, 成绩：%d" %(student.id,student.name,student.age,student.score))

    def __delete_student(self):
        """
            根据学生姓名删除学生信息。
        """
        stu_name = input("请输入需要删除学生的姓名：")
        stu_id = self.__controller.search_student_id(stu_name)
        if self.__controller.remove_student(stu_id) == True:
            print("成功删除%s的信息" % (stu_name))

    def __modify_student(self):
        """
            根据学生id更新学生信息。
        """
        new_stu = StudentModel()
        new_stu.id = self.__input_integer("请输入学生的id：")
        new_stu.name = input("请输入学生的姓名：")
        new_stu.age = self.__input_integer("请输入学生的年龄：")
        new_stu.score = self.__input_integer("请输入学生的成绩：")

        if self.__controller.update_student(new_stu):
            print("修改成功！")
        else:
            print("修改失败！")

    def __output_students_order_by_score(self):
        """
            将学生成绩升序排序后显示所有学生信息。
        """
        temp_student_list = self.__controller.order_by_score()
        self.__output_students(temp_student_list)

    def main(self):
        while True:
            self.__display_menu()
            if self.__select_menu():
                break
