let client = document.getElementById('clientName');

$(document).ready(() => { events($); });

function events($) {
    "use strict";
    $(function () {
        client.addEventListener("keyup", function (event) {
            var $this = $(this);
            var input = $this.val();
            client.value = input.replace(/^([a-zA-Z]{3,20}) {1,}([a-zA-Z]{3,20})/);
        });
    });
}
