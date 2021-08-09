import pandas as pd
import sys

class EmployeePerformance:
    '''Generates the classification comparison of Supervisor-Assesment and Desired Competencies'''
    
    def __init__(self):
        self.classif = pd.read_csv('../data/processed/classification.csv', index_col=[0])
    
    def main(self):
        '''Main function.'''
        emp = str((sys.argv)[1])
        r = self.classif[self.classif['Employee ID'] == f'Employee {emp}']
        r.to_csv(f'../data/processed/report for Employee {emp}')

if __name__ == '__main__':
    employee = EmployeePerformance()
    employee.main()
