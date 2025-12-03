class AttendanceSystem:
    def __init__(self, name, total_classes, present_classes):
        self.name = name
        self.total = total_classes
        self.present = present_classes

    def attendance_percentage(self):
        return (self.present / self.total) * 100

    def status(self):
        percentage = self.attendance_percentage()
        if percentage >= 75:
            return "Allowed to sit in exam"
        else:
            return "Not allowed (Short Attendance)"

    def show(self):
        print("Student Name:", self.name)
        print("Total Classes:", self.total)
        print("Present:", self.present)
        print("Attendance:", round(self.attendance_percentage(), 2), "%")
        print("Status:", self.status())


# Usage
student = AttendanceSystem("Musharib", 28, 22)
student.show()
