from ib.opt import Connection, message,ibConnection
from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import ibConnection


def make_contract(symbol, sec_type, exch, prim_exch, curr):
    Contract.m_symbol =symbol
    Contract.m_secType = sec_type
    Contract.m_exchange=exch
    Contract.m_primaryExch=prim_exch
    Contract.m_currency=curr
    return Contract

def make_order(action, quantity, price=None):
    if price is not None:
        order =Order()
        order.m_orderType='LMT'
        order.m_totalQuantity=quantity
        order.m_action=action
        order.m_lmtPrice=price

    else:
        order =Order()
        order.m_orderType='MKT'
        order.m_totalQuantity=quantity
        order.m_action=action

    return Order

def main():
    con=Connection.create(port=7497, clientId=999)
    conn =ibConnection(port=7497, clientId=999)
    conn.connect()
    con.connect()

    oid=500
    cont = make_contract('TSLA', 'STK', 'SMART', 'SMART', 'USD')
    print 'make contract'
    offer = make_order ('BUY', 1, 200)
    print 'make order'




main()