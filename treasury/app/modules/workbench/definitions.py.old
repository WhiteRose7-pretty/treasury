# type enums
class Types:
    TYPE_NUMBER = 'TYPE_NUMBER'
    TYPE_STRING = 'TYPE_STRING'
    TYPE_DATE = 'TYPE_DATE'
    TYPE_BOOLEAN = 'TYPE_BOOLEAN'
    TYPE_MARKET_DATES = 'TYPE_MARKET_DATES'
    TYPE_BUSINESS_CENTRE = 'TYPE_BUSINESS_CENTRE'
    TYPE_DISCOUNT_CURVE = 'TYPE_DISCOUNT_CURVE'
    TYPE_LIBOR_CURVE = 'TYPE_LIBOR_CURVE'
    TYPE_CURRENCY = 'TYPE_CURRENCY'
    TYPE_ELEMENT_DESCRIBE = 'TYPE_ELEMENT_DISCRIBE'
    TYPE_ELEMENT_SHOW_AVAILABLE = 'TYPE_ELEMENT_SHOW_AVAILABLE'
    TYPE_TRADE_LIST = 'TYPE_TRADE_LIST'


data_type_spec = [
    {'TYPE_NUMBER': {'type': 'number', 'width': '10', 'init_values': []}}
    , {'TYPE_STRING': {'type': 'string', 'width': '10', 'init_values': []}}
    , {'TYPE_DATE': {'type': 'date', 'width': '10', 'init_values': []}}
    , {'TYPE_BOOLEAN': {'type': 'combo', 'width': '10', 'init_values': ['true', 'false']}}
    , {'TYPE_BUSINESS_CENTRE': {'type': 'combo', 'width': '10',
                                'init_values': ['none', 'frankfort', 'london', 'milan', 'newyork', 'paris', 'target',
                                                'tokyo', 'zurich']}}
    , {'TYPE_DISCOUNT_CURVE': {'type': 'combo', 'width': '10',
                               'init_values': ['chf.ois', 'eur.ois', 'gbp.ois', 'jpy.ois', 'usd.ois']}}
    , {'TYPE_LIBOR_CURVE': {'type': 'combo', 'width': '10',
                            'init_values': ['chf.libor3m', 'chf.libor6m', 'eur.libor3m', 'eur.libor6m', 'gbp.libor3m',
                                            'gbp.libor6m', 'jpy.libor3m', 'jpy.libor6m', 'usd.libor3m', 'usd.libor6m']}}
    , {'TYPE_CURRENCY': {'type': 'combo', 'width': '10', 'init_values': ['usd', 'gbp', 'eur', 'chf', 'jpy']}}
    , {'TYPE_ELEMENT_DESCRIBE': {'type': 'combo', 'width': '10',
                                 'init_values': [' ','book', 'describe', 'formatted_grid_swap_rates', 'market_fx_rates',
                                                 'market_swap_rates', 'pnl_attribute', 'pnl_predict', 'price',
                                                 'price_fx_forward', 'price_vanilla_swap', 'risk_ladder',
                                                 'show_available', 'workspace']}}
    , {'TYPE_ELEMENT_SHOW_AVAILABLE': {'type': 'combo', 'width': '10',
                                       'init_values': [' ','asof_dates', 'daycounts', 'calendar', 'business_day_rule',
                                                       'libor_curves', 'discount_curves']}}
    ]


_show_available={
'name':'show_available'
,'arguments': ['element']
,'argument_labels': ['element']
,'argument_optionals': [1]
,'argument_types': ['TYPE_ELEMENT_SHOW_AVAILABLE']
}

_describe={
'name':'describe'
,'arguments': ['element']
,'argument_labels': ['element']
,'argument_optionals': [1]
,'argument_types': ['TYPE_ELEMENT_DESCRIBE']
}

_market_swap_rates={
'name':'market_swap_rates'
,'arguments': ['asof', 'currency']
,'argument_labels': ['As of', 'Currency']
,'argument_optionals': [0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_CURRENCY']
}


_market_fx_rates={
'name':'market_fx_rates'
,'arguments': ['asof', 'to_date', 'base_currency']
,'argument_labels': ['As of', 'Date(to)','Base Currency']
,'argument_optionals': [0,0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_MARKET_DATES','TYPE_CURRENCY']
}


_price_fx_forward={
'name':'price_fx_forward'
,'arguments': ['type','asof',  'trade_date', 'trade_expiry', 'pay_amount', 'pay_currency',
                       'receive_amount', 'receive_currency','save_as' ]
,'argument_labels': ['Type', 'As of','Trade Date', 'Expiry', 'Pay Amount', 'Pay Currency',
                       'Receive Amount', 'Receive Currency','Save as']
,'argument_optionals': [-1,0,0,0,0,0,0,0,1]
,'argument_types': ['TYPE_STRING','TYPE_MARKET_DATES','TYPE_MARKET_DATES','TYPE_NUMBER','TYPE_CURRENCY','TYPE_NUMBER','TYPE_CURRENCY','TYPE_STRING']
}

_price_vanilla_swap={
'name':'price_vanilla_swap'
,'arguments': ['type','asof', 'notional', 'trade_date', 'trade_maturity', 'index_id',
                         'discount_id', 'floating_leg_period', 'fixed_leg_period', 'floating_leg_daycount',
                         'fixed_leg_daycount', 'spread', 'fixed_rate', 'is_payer', 'business_day_rule',
                         'business_centres', 'spot_lag_days','save_as' ]
,'argument_labels': ['Type', 'As of', 'Notional', 'Trade Date', 'Trade Maturity', 'Index Id',
                         'Discount Curve', 'Floating Leg Period', 'Fixed Leg Period', 'Floating Leg Daycount',
                         'Fised Leg Daycount', 'Spread', 'Fixed Rate', 'Is Payer', 'Business Day Rule',
                         'Business Centre', 'Spot Lag(days)','Save as']
,'argument_optionals': [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
,'argument_types': ['TYPE_STRING','TYPE_MARKET_DATES','TYPE_MARKET_DATES','TYPE_NUMBER','TYPE_CURRENCY','TYPE_NUMBER','TYPE_CURRENCY','TYPE_STRING']
}


_price={
'name':'price'
,'arguments': ['asof', 'load_as']
,'argument_labels': ['As of', 'Load as']
,'argument_optionals': [0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_TRADE_LIST']
}


_risk_ladder={
'name':'risk_ladder'
,'arguments': ['asof', 'load_as']
,'argument_labels': ['As of', 'Load as']
,'argument_optionals': [0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_TRADE_LIST']


}



_pnl_predict={
'name':'pnl_predict'
,'arguments': ['from_date', 'to_date', 'load_as']
,'argument_labels': ['As of', 'Load as']
,'argument_optionals': [0,0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_MARKET_DATES','TYPE_TRADE_LIST']
}


_pnl_attribute={
'name':'pnl_attribute'
,'arguments': ['from_date', 'to_date', 'load_as']
,'argument_labels': ['As of', 'Load as']
,'argument_optionals': [0,0,0]
,'argument_types': ['TYPE_MARKET_DATES','TYPE_MARKET_DATES','TYPE_TRADE_LIST']
}


api_specs={'pnl_attribute':_pnl_attribute,
           'pnl_predict':_pnl_predict,
           'risk_ladder':_risk_ladder,
           'price':_price,
           'price_vanilla_swap':_price_vanilla_swap,
           'price_fx_forward':_price_fx_forward,
           'market_fx_rates':_market_fx_rates,
           'market_swap_rates':_market_swap_rates,
           'describe':_describe,
           'show_available':_show_available
           }