from enum import Enum

class o_Type(Enum):
    BUY_ORDER = 1
    LIMIT_ORDER = 2
    STOP_LOSS_ORDER = 3
    STOP_LIMIT_ORDER = 4
    TRAILING_STOP_ORDER = 5
    RECURRING_INVESTMENT = 6
    CLOSE_ORDER = 7

class TraderClient:
    def __init__(self):
        pass

class Order:
    def __init__(self,order_type, buy_in, amount):
        """Initializes an Order object.

        :param order_type: Must be of type `o_Type`. Type of order to be placed (e.g., "market", "limit").
        :rtype: None 
        """
        self.order_type
        self.buy_in
        self.amount
