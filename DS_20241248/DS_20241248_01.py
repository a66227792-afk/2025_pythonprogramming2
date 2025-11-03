class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name
    def showinfo(self):
        print(f"학번 {self.stu_id}, 이름 : {self.name}")

a = DSstudent("20241248", "조민서")
a.showinfo()