/******************************** Data and API specifications *********************************/

/*
    Notes
    =====
    This page is meant to be a simple workbench exposing our apis to the user.
    Like any function, our apis will have different number of input arguments as well as output results.
    Furthermore, each argument and each result will have different types: some numbers, some strings, list, etc.
    The objective of the design is to introduce these apis in a cohesive and intuitive manner
    The design is simple. User selects an api name (function name) from the main combo list from the top.
    A dynamic Form is then created based on the chosen api's specification. Once the final submission
    button is clicked, there will be a validation, request creation and an api call over http. The results
    are then parsed and placed in various locations on the screen. So the key to the design is the api specifications.

    API Specification
    =================
    Each api specification provides the arguments, argument_labels, argument_types and argument_optionals.
    - arguments are used when building the api request
    - argument_labels are used to print the argument names in a more user friendly manner
    - argument_types are used to create the appropriate input fields as well as validating the input values
    - argument_optionals are used for validating the input and accepting empty values.
    - argument_values are the initial values to be set at. When it is set at "last" we will set the last entry as selected .When it is set at "previous" we will set the one before the last entry as selected.

    Data Type Specification
    =======================
    Data types used for argument_type processing cover a range of types from number to various combo lists.

    Each type covers type, width and init_values .
    - type is the type name that is used to distinguish this type from others.
    - width is the width of the input filed that is meant to be the same for each type all its instantiations.
    - init_values are used for combo list.
    * note: there are two types that are dynamic: 1) TYPE_MARKET_DATES and 2) TYPE_TRADE_LIST. TYPE_MARKET_DATES should be populated only once and only when the page is loaded. TYPE_TRADE_LIST is populated at the beginning and at each time a trade is saved.


    Steps of adding a new api
    =========================
    1) create a new api specification
    'name': 'api name'
    , 'arguments': [arg1, arg2, ...] #the are the actual aruments of the api
    , 'argument_labels': [label1, label2, ...]
    , 'argument_optionals': ['0','0','0',...]
    , 'argument_types': ['TYPE_STRING'. 'TYPE_MARKET_DATES', ...]
    , 'argument_values': ['def value', '0',...]
    , 'callback_name': callback_nothing


    */
    /******************************** End *********************************/


//
// declaring  the data type specifications
//
var data_type_spec = {
    'TYPE_NUMBER': {'type': 'number', 'width': '10', 'init_values': []}
    , 'TYPE_STRING': {'type': 'string', 'width': '10', 'init_values': []}
    , 'TYPE_DATE': {'type': 'date', 'width': '8', 'init_values': []}
    , 'TYPE_BOOLEAN': {'type': 'combo', 'width': '10', 'init_values': ['true', 'false']}
    , 'TYPE_BUSINESS_CENTRE': {
        'type': 'combo', 'width': '10',
        'init_values': ['none', 'frankfort', 'london', 'milan', 'newyork', 'paris', 'target',
            'tokyo', 'zurich']
    }
    , 'TYPE_DISCOUNT_CURVE': {
        'type': 'combo', 'width': '10',
        'init_values': ['usd.ois', 'eur.ois', 'gbp.ois', 'chf.ois', 'jpy.ois']
    }
    , 'TYPE_LIBOR_CURVE': {
        'type': 'combo', 'width': '10',
        'init_values': ['usd.libor3m', 'usd.libor6m', 'eur.libor3m', 'eur.libor6m', 'gbp.libor3m',
            'gbp.libor6m', 'chf.libor3m', 'chf.libor6m', 'jpy.libor3m', 'jpy.libor6m']
    }
    , 'TYPE_CURRENCY': {'type': 'combo', 'width': '10', 'init_values': ['usd', 'gbp', 'eur', 'chf', 'jpy']}
    , 'TYPE_ELEMENT_DESCRIBE': {
        'type': 'combo', 'width': '10',
        'init_values': ['', 'book', 'describe', 'formatted_grid_swap_rates', 'market_fx_rates',
            'market_swap_rates', 'pnl_attribute', 'pnl_predict', 'price',
            'price_fx_forward', 'price_vanilla_swap', 'risk_ladder',
            'show_available', 'workspace']
    }
    , 'TYPE_ELEMENT_SHOW_AVAILABLE': {
        'type': 'combo', 'width': '10',
        'init_values': ['', 'asof_dates', 'daycounts', 'calendar', 'business_day_rule',
            'libor_curves', 'discount_curves']
    }
    , 'TYPE_MARKET_DATES': {
        'type': 'combo', 'width': '10',
        'init_values': []
    }
    , 'TYPE_TRADE_LIST': {
        'type': 'combo', 'width': '10',
        'init_values': []
    }
    , 'TYPE_SWAP_TYPES': {
        'type': 'combo', 'width': '10',
        'init_values': ['ir_vanilla_swap']
    }
    , 'TYPE_FXFWD_TYPES': {
        'type': 'combo', 'width': '10',
        'init_values': ['fx_forward']
    }
    , 'TYPE_PERIOD': {
        'type': 'combo', 'width': '10',
        'init_values': ['3m', '6m', '1y']
    }
    , 'TYPE_DAYCOUNT': {
        'type': 'combo', 'width': '10',
        'init_values': ['act/360', 'act/365', '30/360', 'act/act', '30/360eu', '30/360_us', '30/360_isda']
    }
    , 'TYPE_BUSINESS_DAY_RULE': {
        'type': 'combo', 'width': '10',
        'init_values': ['none', 'modified_following', 'modified_precedent', 'following', 'precedent']
    }
    , 'TYPE_SPOT_LAG_DAYS': {
        'type': 'combo', 'width': '10',
        'init_values': ['0', '1', '2']
    }
};


//
// declaring each api specification separately (rather than all of the together for readability)
//

//
// api:show_available
//
var _show_available = {
    'name': 'show_available'
    , 'arguments': ['element']
    , 'argument_labels': ['element']
    , 'argument_optionals': [1]
    , 'argument_types': ['TYPE_ELEMENT_SHOW_AVAILABLE']
    , 'argument_values': ['']
    , 'callback_name': callback_nothing
}

//
// api:describe
//
var _describe = {
    'name': 'describe'
    , 'arguments': ['element']
    , 'argument_labels': ['element']
    , 'argument_optionals': [1]
    , 'argument_types': ['TYPE_ELEMENT_DESCRIBE']
    , 'argument_values': ['']
    , 'callback_name': callback_nothing
}

//
// api:market_swap_rates
//
var _market_swap_rates = {
    'name': 'market_swap_rates'
    , 'arguments': ['asof', 'currency']
    , 'argument_labels': ['As of', 'Currency']
    , 'argument_optionals': [0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_CURRENCY']
    , 'argument_values': ['last', '0']
    , 'callback_name': callback_nothing
}
//
// api:market_fx_rates
//
var _market_fx_rates = {
    'name': 'market_fx_rates'
    , 'arguments': ['asof', 'to_date', 'base_currency']
    , 'argument_labels': ['As of', 'To Date', 'Base Currency']
    , 'argument_optionals': [0, 0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_DATE', 'TYPE_CURRENCY']
    , 'argument_values': ['last', '', '0']
    , 'callback_name': callback_nothing
}


//
// api:price_fx_forward
//
var _price_fx_forward = {
    'name': 'price_fx_forward'
    ,
    'arguments': ['type', 'asof', 'trade_date', 'trade_expiry', 'pay_amount', 'pay_currency',
        'receive_amount', 'receive_currency', 'save_as']
    ,
    'argument_labels': ['Type', 'As of', 'Trade Date', 'Expiry', 'Pay Amount', 'Pay Currency',
        'Receive Amount', 'Receive Currency', 'Save as']
    ,
    'argument_optionals': [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,
    'argument_types': ['TYPE_FXFWD_TYPES', 'TYPE_MARKET_DATES', 'TYPE_DATE', 'TYPE_DATE', 'TYPE_NUMBER', 'TYPE_CURRENCY', 'TYPE_NUMBER', 'TYPE_CURRENCY', 'TYPE_STRING']
    ,
    'argument_values': ['0', 'last', '', '', '1000000', '0', '1000000', '1', '']
    ,
    'callback_name': callback_price_fx_forward
}

//
// api:price_vanilla_swap
//
var _price_vanilla_swap = {
    'name': 'price_vanilla_swap'
    ,
    'arguments': ['type', 'asof', 'notional', 'trade_date', 'trade_maturity', 'index_id',
        'discount_id', 'floating_leg_period', 'fixed_leg_period', 'floating_leg_daycount',
        'fixed_leg_daycount', 'spread', 'fixed_rate', 'is_payer', 'business_day_rule',
        'business_centres', 'spot_lag_days', 'save_as']
    ,
    'argument_labels': ['Type', 'As of', 'Notional', 'Trade Date', 'Trade Maturity', 'Index Id',
        'Discount Curve', 'Floating Leg Period', 'Fixed Leg Period', 'Floating Leg Daycount',
        'Fixed Leg Daycount', 'Spread', 'Fixed Rate', 'Is Payer', 'Business Day Rule',
        'Business Centre', 'Spot Lag(days)', 'Save as']
    ,
    'argument_optionals': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,
    'argument_types': [
        'TYPE_SWAP_TYPES',
        'TYPE_MARKET_DATES',
        'TYPE_NUMBER',
        'TYPE_DATE',
        'TYPE_STRING',
        'TYPE_LIBOR_CURVE',
        'TYPE_DISCOUNT_CURVE',
        'TYPE_PERIOD',
        'TYPE_PERIOD',
        'TYPE_DAYCOUNT',
        'TYPE_DAYCOUNT',
        'TYPE_NUMBER',
        'TYPE_NUMBER',
        'TYPE_BOOLEAN',
        'TYPE_BUSINESS_DAY_RULE',
        'TYPE_BUSINESS_CENTRE',
        'TYPE_SPOT_LAG_DAYS',
        'TYPE_STRING']
    ,
    'argument_values': ['0', 'last', '100000000', '', '30y', '0', '0', '0', '0', '0', '0', '0', '0.01', '0', '0', '0', '0', '']
    , 'callback_name': callback_price_vanilla_swap
}

//
// api:price
//
var _price = {
    'name': 'price'
    , 'arguments': ['asof', 'load_as']
    , 'argument_labels': ['As of', 'Load as']
    , 'argument_optionals': [0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_TRADE_LIST']
    , 'argument_values': ['last', '0']
    , 'callback_name': callback_nothing
}


//
// api:risk_ladder
//
var _risk_ladder = {
    'name': 'risk_ladder'
    , 'arguments': ['asof', 'load_as']
    , 'argument_labels': ['As of', 'Load as']
    , 'argument_optionals': [0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_TRADE_LIST']
    , 'argument_values': ['last', '0']
    , 'callback_name': callback_nothing
}
//
// api:pnl_predict
//
var _pnl_predict = {
    'name': 'pnl_predict'
    , 'arguments': ['from_date', 'to_date', 'load_as']
    , 'argument_labels': ['Date(from)', 'Date (to)', 'Load as']
    , 'argument_optionals': [0, 0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_MARKET_DATES', 'TYPE_TRADE_LIST']
    , 'argument_values': ['previous', 'last', '0']
    , 'callback_name': callback_nothing
}

//
// api:pnl_attribute
//
var _pnl_attribute = {
    'name': 'pnl_attribute'
    , 'arguments': ['from_date', 'to_date', 'load_as']
    , 'argument_labels': ['Date(from)', 'Date (to)', 'Load as']
    , 'argument_optionals': [0, 0, 0]
    , 'argument_types': ['TYPE_MARKET_DATES', 'TYPE_MARKET_DATES', 'TYPE_TRADE_LIST']
    , 'argument_values': ['previous', 'last', '0']
    , 'callback_name': callback_nothing
}

//
// api:workspace_list
//
var _workspace_list = {
    'name': 'workspace_list'
    , 'arguments': []
    , 'argument_labels': []
    , 'argument_optionals': []
    , 'argument_types': []
    , 'argument_values': []
    , 'callback_name': callback_nothing
}
//
// api:workspace_read
//
var _workspace_list = {
    'name': 'workspace_read'
    , 'arguments': ['file_id']
    , 'argument_labels': ['File Id']
    , 'argument_optionals': ['0']
    , 'argument_types': ['TYPE_TRADE_LIST']
    , 'argument_values': ['0']
    , 'callback_name': callback_nothing
}
//
// api:workspace_delete
//
var _workspace_delete = {
    'name': 'workspace_delete'
    , 'arguments': ['file_id']
    , 'argument_labels': ['File Id']
    , 'argument_optionals': ['0']
    , 'argument_types': ['TYPE_STRING']
    , 'argument_values': ['']
    , 'callback_name': callback_nothing
}


//
// create a dictionary of all api specification
//
var api_specs = {
    'price_fx_forward': _price_fx_forward,
    'price_vanilla_swap': _price_vanilla_swap,
    'price': _price,
    'risk_ladder': _risk_ladder,
    'pnl_attribute': _pnl_attribute,
    'pnl_predict': _pnl_predict,
    'market_swap_rates': _market_swap_rates,
    'market_fx_rates': _market_fx_rates,
    'describe': _describe,
    'show_available': _show_available
}


//
// create a dictionary of all api text description
//
var api_descriptions = {
    'price_fx_forward': '',
    'price_vanilla_swap': '',
    'price': '',
    'risk_ladder': '',
    'pnl_attribute': '',
    'pnl_predict': '',
    'workspace_list',
    'workspace_read',
    'workspace_delete',
    'market_swap_rates': '',
    'market_fx_rates': '',
    'describe': '',
    'show_available': '',
}

/******************************** Form Creation *********************************/


//
// Populates the list for any type that contains a selection

function get_api_list() {
    let content = "<option value=\"x\">Select API</option>";
    for (let key in api_specs) {
        if (api_specs.hasOwnProperty(key)) {
            content += "<option value=\"" + key + "\">" + key + "</option>";
        }
    }
    return content;
}

function get_list(id, list, default_value) {
    var content = "<div class=\"col-6\"><select class=\"form-control\"  id=\"" + id + "\" name=\"" + id + "\">";
    for (j = 0; j < list.length; ++j) {

        content += "<option value=\"" + list[j] + "\"";
        if (default_value == 'last' && j == list.length - 1) {
            content += " selected ";
        }
        if (default_value == 'previous' && j == list.length - 2) {
            content += " selected ";
        } else if (default_value == j) {
            content += " selected ";
        }
        content += ">" + list[j] + "</option>";
    }
    content += "</select></div>";

    return content;
}


function build_input_text_box(argument, type_attribute = 'text', value = '', placeholder = '', size = '', maxlength = '') {

    var style_attrib = ''
    var placeholder_attrib = " placeholder=" + " \"" + placeholder + "\" ";
    var size_attrib = " size=" + "\"" + size + "\"  ";
    var maxlength_attrib = " maxlength=" + " \"" + maxlength + "\" ";
    var value_attrib = " value=" + " \"" + value + "\" ";

    var content = "<div class=\"col-6\"><input class=\"form-control\" id=\"" + argument + "\" name=\"" + argument + " type=\"" + type_attribute + "\"";

    if (value != '') {
        content += value_attrib;
    }
    if (placeholder != '') {
        content += placeholder_attrib;
    }
    if (size != '') {
        content += size_attrib;
    }
    if (maxlength != '') {
        content += maxlength_attrib;
    }
    content += style_attrib + " ></div>";
    return content;
}

//
// Provides an input object such as a text box or a list, etc. depending on the type of the input (see data_type_spec)
//
function get_input_object(argument, argument_text, argument_optional, argument_type, argument_default) {
    var simple_type_content = "<input ";
    simple_type_content += "   class=\"form-control\" id=\"" + argument + "\" name=\"" + argument + "\"";
    simple_type_content += " type=\"email\"";
    simple_type_content += " >";


    var content = "";
    var place_holder = "";
    switch (argument_type) {
        case 'TYPE_DATE':
            place_holder = "YYYYMMDD";
            var argument_width = data_type_spec['TYPE_DATE']['width'];
            content = build_input_text_box(argument, 'number', argument_default, place_holder, argument_width, argument_width);
            break;

        case 'TYPE_NUMBER':
            place_holder = "";
            var argument_width = data_type_spec['TYPE_NUMBER']['width'];
            content = build_input_text_box(argument, 'number', argument_default, place_holder, argument_width, '');
            break;

        case 'TYPE_STRING':
            place_holder = "";
            var argument_width = data_type_spec['TYPE_STRING']['width'];
            content = build_input_text_box(argument, 'number', argument_default, place_holder, argument_width, '');
            break;

        case 'TYPE_BOOLEAN':
            content = get_list(argument, data_type_spec['TYPE_BOOLEAN']['init_values'], argument_default);
            break;
        case 'TYPE_BUSINESS_CENTRE':
            content = get_list(argument, data_type_spec['TYPE_BUSINESS_CENTRE']['init_values'], argument_default);
            break;
        case 'TYPE_DISCOUNT_CURVE':
            content = get_list(argument, data_type_spec['TYPE_DISCOUNT_CURVE']['init_values'], argument_default);
            break;
        case 'TYPE_LIBOR_CURVE':
            content = get_list(argument, data_type_spec['TYPE_LIBOR_CURVE']['init_values'], argument_default);
            break;
        case 'TYPE_CURRENCY':
            content = get_list(argument, data_type_spec['TYPE_CURRENCY']['init_values'], argument_default);
            break;
        case 'TYPE_TRADE_LIST':
            content = get_list(argument, data_type_spec['TYPE_TRADE_LIST']['init_values'], argument_default);
            break;
        case 'TYPE_ELEMENT_DESCRIBE':
            content = get_list(argument, data_type_spec['TYPE_ELEMENT_DESCRIBE']['init_values'], argument_default);
            break;
        case 'TYPE_MARKET_DATES':
            content = get_list(argument, data_type_spec['TYPE_MARKET_DATES']['init_values'], argument_default);
            break;
        case 'TYPE_ELEMENT_SHOW_AVAILABLE':
            content = get_list(argument, data_type_spec['TYPE_ELEMENT_SHOW_AVAILABLE']['init_values'], argument_default);
            break;
        case 'TYPE_SWAP_TYPES':
            content = get_list(argument, data_type_spec['TYPE_SWAP_TYPES']['init_values'], argument_default);
            break;
        case 'TYPE_FXFWD_TYPES':
            content = get_list(argument, data_type_spec['TYPE_FXFWD_TYPES']['init_values'], argument_default);
            break;
        case 'TYPE_PERIOD':
            content = get_list(argument, data_type_spec['TYPE_PERIOD']['init_values'], argument_default);
            break;
        case 'TYPE_DAYCOUNT':
            content = get_list(argument, data_type_spec['TYPE_DAYCOUNT']['init_values'], argument_default);
            break;
        case 'TYPE_BUSINESS_DAY_RULE':
            content = get_list(argument, data_type_spec['TYPE_BUSINESS_DAY_RULE']['init_values'], argument_default);
            break;
        case 'TYPE_SPOT_LAG_DAYS':
            content = get_list(argument, data_type_spec['TYPE_SPOT_LAG_DAYS']['init_values'], argument_default);
            break;
        default:
            content = "<input class=\"form-control\" id=\"" + argument + "\" name=\"" + argument + "\" type=\"text\">";
    }

    return content;
}

function print_form(choice) {
    clear_output()

    var chosen_function_name = choice;

    var function_spec = api_specs[chosen_function_name];
    if (function_spec == undefined) {
        return;
    }
    var name = function_spec['name'];
    var arguments = function_spec['arguments'];
    var argument_labels = function_spec['argument_labels'];
    var argument_optionals = function_spec['argument_optionals'];
    var argument_types = function_spec['argument_types'];
    var argument_values = function_spec['argument_values'];


    var form_content = "";
    for (i = 0; i < arguments.length; i++) {

        var argument = arguments[i];
        var argument_label = argument_labels[i];
        var argument_optional = argument_optionals[i];
        var argument_type = argument_types[i];


        let default_value = argument_values[i];


        form_content += "<div class=\"form-group row\"><label class=\"col-6 col-form-label font-weight-bold\">" + argument_label + ":" + "</label>";
        form_content += get_input_object(argument, argument_label, argument_optional, argument_type, default_value);
        form_content += "</div>";


    }

    //  finished building the form for this given api. Expose it in the page.
    document.getElementById("api-entries").innerHTML = form_content;


    // place the description

    document.getElementById("description").innerHTML = api_descriptions[name];

}


//
// A general function to clear the output once an api is
// selected to ensure all previous messages are reset.
//
function clear_output() {
    $('#output').text('');
    document.getElementById("api-entries").innerHTML = ''
    document.getElementById("description").innerHTML = ''

}


//function clear_form() {
//    document.getElementById("api-entries").innerHTML = ''
//}


/******************************** Calculate Form *********************************/

//
// Performs the validation and processes the form. starts by validating the each field,
// building a request, sending it and treat the output results
//
function calculate() {

    var function_name = $('#api-list').val();
    var function_spec = api_specs[function_name];

    if (function_spec == undefined) {
        return;
    }
    var name = function_spec['name'];
    var arguments = function_spec['arguments'];
    var argument_labels = function_spec['argument_labels'];
    var argument_optionals = function_spec['argument_optionals'];
    var argument_types = function_spec['argument_types'];


    //
    //  validation section
    //

    if (function_name.trim() == '') {
        return;
    }

    var argument_values = [];

    var i = 0;

    var arguments_dictionary = {};

    var is_error = false;

    for (i = 0; i < arguments.length; ++i) {
        var argument = arguments[i];
        var argument_value = $('#' + argument).val();


        //
        //     validate argument_value by type and optional
        //
        var value = ''
        if (argument_value != null) {
            value = argument_value.trim();
        }

        if (argument_optionals[i] != 1 && value == '') {
            is_error = true;
            print_output({'Error': "'" + argument_labels[i] + "' cannot be empty."});
            break;
        }

        if (argument_types[i] == 'TYPE_NUMBER' && !is_valid_number(value)) {
            is_error = true;
            print_output({'Error': "'" + argument_labels[i] + "' should be numeric."});
            break;
        }


        if (argument_types[i] == 'TYPE_DATE' && (value == '' || !is_valid_date(value))) {
            is_error = true;
            print_output({'Error': argument_labels[i] + " should be a valid date in the following format: yyyymmdd."});
            break;
        }

        argument_values.push(argument_value);
        arguments_dictionary[arguments[i]] = argument_value;
    }

    //
    //  If no error, we call the api with the corresponding callback function to consume the results
    //

    if (!is_error) {
        $('#loading-icon-calculate').css('display', 'inline-block');
        api_call(function_name, arguments_dictionary, function_spec['callback_name']);
    }

}

/******************************** callback functions *********************************/
//
// Market dates callback function to treat the response
//
function callback_fill_market_dates(data, request) {
    results = data['Response']['Results'];
    keys = Object.keys(results);
    data_type_spec['TYPE_MARKET_DATES']['init_values'] = keys;
}

//
// Trade id's callback function to treat the response
//
function callback_fill_trade_ids(data, request) {
    results = data['Response']['Results'];
    keys = Object.keys(results);
    data_type_spec['TYPE_TRADE_LIST']['init_values'] = keys;
}


//
// General callback function to treat the response
//

function callback_nothing(data, request) {
    var results = {};
    if (data['Response']['focus'] == 'errors') {
        results = data['Response']['Errors'];
    } else {
        results = data['Response']['Results'];
    }

    print_output(results);
    print_summary(data, request);
    $('#loading-icon-calculate').css('display', 'none');
    return;
}

//
// General callback function to price_fx_forward api
//
function callback_price_fx_forward(data,request){
    callback_nothing(data, request);
    if($('#save_as').val()){
        load_trade_ids();
    }
    return;
}

//
// General callback function to price_vanilla_swap
//

function callback_price_vanilla_swap(data, request){
    callback_nothing(data, request);
    if($('#save_as').val()){
        load_trade_ids();
    }
    return;
}

//
// Token Create callback function to treat the response
//
function callback_account_token_create(data, request) {
    if (data['Response']['focus'] == 'errors') {
        callback_nothing(data, request);
        return;
    }
    var token = data['Response']['Results']['account_token_create'];
    $('#token').text(token);
    var expiry_in_minutes = data['Response']['expiry_minutes'];
    expiry_in_minutes = Math.floor(expiry_in_minutes);
    var now = new Date();
    now.setMinutes(now.getMinutes() + expiry_in_minutes); //  timestamp
    now = new Date(now); //  Date object
    $('#token_expiry').text(now.toISOString());
    print_summary(data, request);

}

/******************************** screen functions *********************************/

// prints the result to the output window
//
function print_output(results) {

    var cntr = 0;
    var output_content = "";
    var keys = Object.keys(results);

    for (cntr = 0; cntr < keys.length; ++cntr) {
        output_content += "<div class=\"form-group row\" >";
        output_content += "<label class=\"col-6 col-form-label font-weight-bold\">" + keys[cntr] + ":</label>";
        output_content += "<label class=\"col-6 col-form-label \">" + results[keys[cntr]] + "</label>";
        output_content += "</div>";
    }

    document.getElementById('output').innerHTML = output_content;
    return;

}

// updates the summary of balance, token, expiry, etc.

function print_summary(data, request) {
    document.getElementById('balance').innerHTML = data['Response']['balance'];
    document.getElementById('client_id').innerHTML = data['client_id'];
    document.getElementById('ip').innerHTML = data['source_id'];
    var request_id = data['id'];
    var request_text = "<b>Request:" + request_id + "</b><br>";
    request_text += "<b>URL:</b>" + url + "<br>";
    request_text += "<b>Method:</b> POST" + "<br>";
    request_text += "<em>" + request + "</em>";

    var response_text = "<br><b>Response:" + request_id + "</b><br><em>" + JSON.stringify(data) + "</em>";

    document.getElementById('log').innerHTML = request_text + request + response_text + "<hr>" + document.getElementById('log').innerHTML;
    return;
}

/******************************** internal api calls  *********************************/

function load_asof_dates() {
    var function_name = 'show_available';
    arguments = {'element': 'asof_dates'};
    api_call(function_name, arguments, callback_fill_market_dates);

}

function load_trade_ids() {
    var function_name = 'workspace';
    arguments = {'list': 'all'};
    api_call(function_name, arguments, callback_fill_trade_ids);
}

//this function should be run with setInterval


async function obtain_or_refresh_token() {

    let email = $('#email').text();
    if ($('#token').text().trim() == '') {
        var arguments = {'email': email};
        await api_call('account_token_create', arguments, callback_account_token_create);
        return $('#token').text();
    }

    var expiry = Date.parse($('#token_expiry').text());
    var diff_second = (expiry - new Date()) / 1000;
    var diff_minutes = Math.round(diff_second / 60);
    if ($('#token').text().trim() == '' || diff_minutes < 2) {
        var arguments = {'email': email};
        api_call('account_token_create', arguments, callback_account_token_create);
    }

//     var email_div = document.getElementById('email');
//     email_div.innerHTML=email;


    return $('#token').text();
}


function is_valid_number(value) {
    return !isNaN(value * 1);
}

function is_valid_date(str) {
    // str is assumed to be YYYYMMDD

    str = str.toString();

    try {
        var year = str.substring(0, 4);
        var month = str.substring(4, 6);
        var day = str.substring(6, 8);
        var str_reformatted = year + "-" + month + "-" + day + " 00:00";
        var date = new Date(str_reformatted);
        return is_valid_number(date.getTime());
    } catch (err) {
        return false;
    }
}


function argument_make_string(function_name, arguments) {
    arguments['function_name'] = function_name;
    var i = 0;
    var argument_string = '';
    length = Object.keys(arguments).length;
    for (var key in arguments) {
        if (arguments.hasOwnProperty(key)) {
            argument_string += key + '=' + arguments[key];
        }
        if (i < length - 1) {
            argument_string += '&';
        }
        i++;
    }
    return argument_string;
}

function format_date(date) {
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var year = date.getFullYear();
    if (day < 10)
        day = "0" + day;

    if (month < 10)
        month = "0" + month;

    var today_date_formatted = year.toString() + month + day;
    return today_date_formatted;
}

function hex2ascii(hexx) {
    var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

/******************************** API gateway *********************************/

async function asyncFetch(url, requestOptions, callback_function) {
    console.log("fetch", requestOptions);
    let response = await fetch(url, requestOptions);
    let data = await response.json();
    await callback_function(data, requestOptions.body);
}


async function api_call(function_name, arguments, callback_function) {

    arguments['function_name'] = function_name;
    if (function_name != 'account_token_create') {
        await obtain_or_refresh_token();
        arguments['token'] = $('#token').text();
    }

    var arguments_string = argument_make_string(function_name, arguments);

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: arguments_string
    };

    await asyncFetchWrapper(url, requestOptions, callback_function);

}

function asyncFetchWrapper(url, requestOptions, callback_function) {
    return new Promise((resolve, reject) => {
        asyncFetch(url, requestOptions, (data, response) => {
            callback_function(data, response);
            resolve();
        });
    });
}

/******************************** initialization segment *********************************/


function initialize_page() {
    // set the default for the trade date
    var date = new Date();
    var today_date_formatted = format_date(date);
    date.setMonth(date.getMonth() + 3);
    var three_month_date_formatted = format_date(date);

    // trade date for vanilla swap
    api_specs['price_vanilla_swap']['argument_values'][3] = today_date_formatted;

    // trade date for FX swap
    api_specs['market_fx_rates']['argument_values'][1] = three_month_date_formatted;
    // expiry date for market FX rate
    api_specs['price_fx_forward']['argument_values'][2] = today_date_formatted;
    api_specs['price_fx_forward']['argument_values'][3] = three_month_date_formatted;
}

//
// load the description text from the session
//
function load_descriptions(descriptions) {

    if (descriptions.length == 0) {
        return;
    }

    var i = 0;
    var api_names = Object.keys(descriptions);
    for (i = 0; i < api_names.length; ++i) {
        descriptions[api_names[i]] = hex2ascii(descriptions[api_names[i]]);
    }
    api_descriptions = descriptions;

}

async function initial_load(email,descriptions) {
    if (email != '' && email != null) {
        print_output({'Connecting to Server': 'Please wait...'});

        load_descriptions(descriptions);
        await obtain_or_refresh_token();

        load_asof_dates();
        load_trade_ids();
        initialize_page();

        setTimeout(function () {
            document.getElementById("api-list").innerHTML = get_api_list();
            clear_output();
        }, 2000);

    } else {
        print_output({'Error': 'Please login first.'});
        document.getElementById("calculate-button").disabled = true
        document.getElementById("api-list").disabled = true
        document.getElementById("send-feedback");
        $('#send-feedback').addClass('disabled');
    }
}


$('#send-feedback').on('click', function () {
    if ($('#send-feedback').hasClass('disabled')) {
        return false;
    }
    $('#feedback-modal').modal('show');
    $('#feedback-content').val('');
    ele_msg.html('');

})

