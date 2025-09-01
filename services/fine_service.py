
from datetime import datetime
from ..db.database import DB

class FineService:
    FINE_PER_DAY = 1.0  # 1 dollar per day

    def calculate_fine(self, user_id: str) -> float:
        total_fine = 0.0
        for loan_data in DB["loans"].values():
            if loan_data["user_id"] == user_id and loan_data["return_date"] is None:
                due_date = loan_data["due_date"]
                if isinstance(due_date, str):
                    due_date = datetime.fromisoformat(due_date)
                
                if datetime.utcnow() > due_date:
                    overdue_days = (datetime.utcnow() - due_date).days
                    total_fine += overdue_days * self.FINE_PER_DAY
        
        user_fines = DB["fines"].get(user_id, {"amount": 0.0})
        user_fines["amount"] += total_fine
        DB["fines"][user_id] = user_fines
        return user_fines["amount"]

    def get_user_fine(self, user_id: str) -> float:
        return DB["fines"].get(user_id, {}).get("amount", 0.0)
