import pyodbc

class Demo:
    l = []
    def __init__(self, Name="", Mark=0):
        self.conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230303-1197\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes')
        self.cursor = self.conn.cursor()
        self.Name = Name
        self.Mark = Mark
        self.Course_Code = "PY21"
        self.Grade = self.gradescore()
        self.emp_status = self.status()
    
    def create_table(self):
        self.cursor.execute('CREATE TABLE Training.dbo.StudentData(Student_id INT IDENTITY(1,1) PRIMARY KEY, Name VARCHAR(40) NOT NULL, Course_Code VARCHAR(5), Mark INT NOT NULL, Grade VARCHAR(1) NOT NULL, employment_status VARCHAR(20))')
        self.conn.commit()
        print("Table created successfully")
        self.close()

    def gradescore(self):
        if self.Mark >= 75:
            return "A"
        elif self.Mark >= 65 and self.Mark < 75:
            return "B"
        elif self.Mark >= 55 and self.Mark < 65:
            return "C"
        else:
            return "F"
        
    def status(self):
        if self.gradescore() == "A":
            return "Automatic employment"
        elif self.gradescore() == "B" or self.gradescore()== "C":
            return "Open to work"
        else:
            return "Probation"
    def collector(self):
        self.l.append((self.Name,self.Mark,self.Course_Code,self.Grade,self.emp_status))
        print("Successful")

    def insertion(self):
        self.cursor.executemany("insert into Training.dbo.StudentData(Name,Mark,Course_Code,Grade,employment_status) values(?,?,?,?,?)",self.l)
        self.conn.commit()
        print("Insert successful")
        self.close()

    def d(self,value):
        self.value= int(value)
        self.cursor.execute("Delete from Training.dbo.StudentData where (Student_id)=(?)", self.value)
        self.conn.commit()
        print("Deletion successful")

    def updation(self,id):
        self.id = int(id)
        self.cursor.execute("update Training.dbo.StudentData set Name=?,Mark=?,Grade=?,employment_status=?  where Student_id=?",(self.Name,self.Mark,self.Grade,self.emp_status,self.id))
        self.conn.commit()
        print("Update successful")

    def selection(self,sel_id):
        self.sel_id = int(sel_id)
        self.cursor.execute("select * from Training.dbo.StudentData where (Student_id) = (?)",self.sel_id)
        for names in self.cursor:
            return names
        
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Connection Closed")
        
