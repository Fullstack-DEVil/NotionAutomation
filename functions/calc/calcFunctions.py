from datetime import datetime

class CalcFunction:
    def getDiffFromNow(date):

        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        
        diff = (given_date - current_date).days

        return diff
