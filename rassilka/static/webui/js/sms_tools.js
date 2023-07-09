document.addEventListener('DOMContentLoaded', function()
{
    $('#sms_txt_field').on('change keyup paste', function(event) 
    {
        var total = event.target.textLength;
        var estimated = 160 - total;

        if (estimated < 0 ) estimated = 'Слишком много текста для одного смс!'

        $('#sms_txt_counter').text(estimated);
    });
});