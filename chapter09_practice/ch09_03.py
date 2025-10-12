class Student:
    def __init__(self, name):
        self.name= name
        self.score = []

    def add_score(self, score):
        self.score.append(score)
        print(f"{self.name}의 성적 {score}점이 추가되었습니다.")
        
    def cal_avg(self):
        if not self.score:
            return 0
        return sum(self.score) / len(self.score)

student = Student("Kim")
student.add_score(90)
student.add_score(85)
student.add_score(78)
avg_score = student.cal_avg()
print(f"{student.name}의 평균 성적 : {avg_score:.2f}")