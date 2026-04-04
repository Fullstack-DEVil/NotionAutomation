from enum import Enum

class Status(Enum):
    EXPIRES_30 = "Expires in 1 month"
    EXPIRES_15 = "Expires in 15 days"
    EXPIRES_10 = "Expires in 10 days"
    EXPIRES_5 = "Expires in 5 days"
    EXPIRES_3 = "Expires in 3 days"
    EXPIRES_2 = "Expires in 2 days"
    EXPIRES_1 = "Expires in 1 day"
    EXPIRED = "Expired"
    ACTIVE = "Active"
    OPEN = "Open"