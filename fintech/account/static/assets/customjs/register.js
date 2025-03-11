$(document).ready(function () {
    $('#personal_form').on('submit', function (form) {
        form.preventDefault(); // Prevents default form submission
        
        // Your form handling logic here
        console.log(form);

        // const $btn_text = $('#btn_text')
        // const $spinner = $('.spinner-border')
        // const $btnpersonal = $('#btnpersonal')
        // $btn_text.text('Loading')
        // $spinner.show();
        // $btnpersonal.prop('disabled', true)
        
    });
});

