today = datetime.now()

employee = Employee(emp_num=168, emp_lname="Doe", emp_fname="John", emp_initial="JD", job_code=500 emp_hiredate=today)
session.add(employee)
session.commit()
