'use strict';

var Cookies = (function () {

    // Variables

    var $modal = $("#modal-cookies");

    // Methods

    function show($this) {
        var cookies = localStorage.getItem('modal_cookies');
        if (!cookies) {
            $this.modal({backdrop: 'static', keyboard: false})
        }
    }

    // Events

    if ($modal.length) {
        show($modal);
        $modal.on('hidden.bs.modal', function (e) {
            localStorage.setItem('modal_cookies', 1);
        })
    }

})();

function call_account_api(token, function_name, argument, success_callback) {
    $.ajax({
        headers: {
            "X-CSRFToken": token
        },
        type: 'post',
        url: call_api_url,
        data: JSON.stringify({
            'function_name': function_name,
            'arguments': argument,
            'source_caller': document.location.href,
        }),
        success: success_callback,
        error: function (jqXhr, textStatus, errorMessage) {
            msg_show(ele_msg, "Error: " + errorMessage);
            ele_loading_icon.css('display', 'none');
            post_message(function_name, errorMessage);
        },
    });
}

function clear_msg_loading(){
    ele_msg.html('');
    ele_loading_icon.css('display', 'none');
}
