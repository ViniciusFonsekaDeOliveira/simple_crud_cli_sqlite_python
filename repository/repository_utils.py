def get_where_clause_conditions(data_identifier: dict):
    clause_conditions = [f"{column}=?" for column in data_identifier.keys()]
    clause_values = tuple(data_identifier.values())
    clause_numbers = len(data_identifier.keys())
    if clause_numbers == 1:
        return clause_conditions[0], clause_values
    elif clause_numbers >= 2:
        conditions = ' AND '.join(clause_conditions)
        return conditions, clause_values
    else:
        print("Where-clause must be at least size 1, but nothing was provided.")
