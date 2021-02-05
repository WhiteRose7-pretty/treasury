'use strict';

var Cookies = (function() {

	// Variables

	var $modal = $("#modal-cookies");


	// Methods

	function show($this) {
        var cookies = localStorage.getItem('modal_cookies');

        if(! cookies) {
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