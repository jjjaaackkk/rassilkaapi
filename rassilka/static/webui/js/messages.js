function getCookie(val)
{
    if (document.cookie.length > 0)
    {
        var c_start = document.cookie.indexOf(val + "=");
        if (c_start != -1)
        {
            c_start = c_start + val.length + 1;
            var c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

async function remove_message(id)
{
    var response;
    var cookies = getCookie('csrftoken');

    console.log(cookies);

    $.ajaxSetup({
        headers: { 
            'X-CSRFToken': cookies
        }
    });

    await $.ajax({
        type: "DELETE",
        url: `/api/v1/messages/${id}`,
        contentType: "application/json",
        async: true,
        success: function (r)
        {
            response = r;
        },
        failure: function () {
            response = 'error';
        },
    });

    if ('undefined' != response.result && response.result == 'succeed')
    {
        document.getElementById(`msg${id}`).remove();
    }

    return;
}


document.addEventListener('DOMContentLoaded', function()
{
    // add trash
    elements = document.getElementsByClassName("fa-trash");

    var trash_handle = function() 
    {
        var id = this.getAttribute("id");
        if (!id.includes('trash')) return;
        id = id.split('trash')[1];
        remove_message(id);
    };

    for (var el of elements) 
    {
        el.addEventListener('click', trash_handle, false);
    }
});