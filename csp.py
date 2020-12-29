# From: https://github.com/davecom/ClassicComputerScienceProblemsInPython. Chapter 3 on CSP.

from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def is_satisfied(self, assignment):
        ...


class CSP:
    def __init__(self, variables, domains):
        self.variables = variables # variables to be constrained
        self.domains = domains # domain of each variable
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

                
    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

                
    def is_consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    
    def backtracking_search_unique_assignment(self, assignment = {}):
        visited_domains = assignment.values()
        
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first = unassigned[0]
        for value in self.domains[first]:
            if value in visited_domains:
                continue
            else:
                local_assignment = assignment.copy()
                local_assignment[first] = value
                # if we're still consistent, we recurse (continue)
                if self.is_consistent(first, local_assignment):
                    result = self.backtracking_search_unique_assignment(local_assignment)
                    # if we didn't find the result, we will end up backtracking
                    if result is not None:
                        return result
        return None
    
    
    def backtracking_search(self, assignment = {}):
        visited_domains = assignment.values()
        
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if we're still consistent, we recurse (continue)
            if self.is_consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None