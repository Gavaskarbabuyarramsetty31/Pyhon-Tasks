#basic_salart=20000
#bonus-->20%
#incentive-->5%
#P.F-->2%
#Health_insurence-->1%


Basic_salary=20000
bonus=0.2*Basic_salary
incentive=0.05*Basic_salary
gross_salary=Basic_salary+bonus+incentive

Pf=0.02*20000
health_insurence=0.01*20000
cuttings=Pf+health_insurence

inhand_salary=gross_salary-cuttings
print("Gross_salary",gross_salary)
print("Cuttings:",cuttings)
print("Inhand Salary :₨",inhand_salary)