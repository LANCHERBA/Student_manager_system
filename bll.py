
class StudentManagerController:
    """
        学生管理控制器：主要负责业务逻辑处理
    """
    init_id = 1

    @classmethod
    def __generate_id(cls, stu):
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def check_empty(self):
        """
            测试学生列表是否存有信息
        :return: True代表无信息，False代表有信息。
        """
        if len(self.__stu_list) == 0:
            return True
        else:
            return False

    def search_student_pos(self, stu_id):
        """
            在学生信息列表中以学生id查找学生位置
        :param stu_id:需要查找的学生的id
        :return: 学生在列表中的位置
        """
        for studentindex in range(len(self.__stu_list)):
            if self.__stu_list[studentindex].id == stu_id:
                return studentindex
        raise Exception("查无此人")

    def search_student_id(self, stu_name):
        """
            在学生信息列表中以学生姓名查找学生id
        :param stu_name:需要查找的学生的姓名
        :return: 学生的id
        """
        for studentindex in range(len(self.__stu_list)):
            if self.__stu_list[studentindex].name == stu_name:
                return self.__stu_list[studentindex].id
        raise Exception("查无此人")

    def add_student(self, stu):
        """
            添加学生信息
        :param stu: 需要添加的学生对象
        """
        StudentManagerController.__generate_id(stu)
        self.__stu_list.append(stu)

    def remove_student(self, stu_id):
        """
            根据学生id从列表中清除学生信息。
        :param stu_id: 需要删除的学生的id
        :return: true代表删除成功。
        """
        del self.__stu_list[self.search_student_pos(stu_id)]
        return True

    def update_student(self, updated_stu):
        """
            根据更新后的学生信息更新列表中的旧学生信息。
        :param updated_stu: 更新后的学生信息
        :return: true代表信息更改成功。
        """
        self.__stu_list[self.search_student_pos(updated_stu.id)] = updated_stu
        return True

    def order_by_score(self):
        """
            根据学生成绩进行升序排序。
        :return:　true代表排序成功。
        """
        if len(self.__stu_list) == 0:
            raise Exception("无学生信息")
        ordered_list = self.__stu_list[::]
        for first_index in range(len(ordered_list) - 1):
            for second_index in range(first_index, len(ordered_list)):
                if ordered_list[first_index].score > ordered_list[second_index].score:
                    ordered_list[first_index], ordered_list[second_index] = ordered_list[second_index], \
                                                                                  ordered_list[first_index]
        return ordered_list