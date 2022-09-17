$(document).ready(function() {
    $('section').each(
        function (index) {
            let input = $(this);
            console.log(input);
            input.css('margin-bottom','0px');
        });
});
