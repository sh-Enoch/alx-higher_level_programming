Use the try statement to handle exception.
Place only minimal code that you want to protect from potential exceptions in the try clause.
Handle exceptions from most specific to least specific in terms of exception types. The order of except clauses is important.
The finally always executes whether the exceptions occurred or not.
The else clause only executes when the try clause terminates normally. The else clause is valid only if the try statement has at least one except clause.
Avoid using bare exception handlers.
