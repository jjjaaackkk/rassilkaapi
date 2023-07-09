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

async function remove_campaign(id)
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
        url: `/api/v1/campaigns/${id}`,
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
        document.getElementById(`camp${id}`).remove();
    }

    return;
}

async function send_row_data(id, data)
{
    var response;
    var cookies = getCookie('csrftoken');

    $.ajaxSetup({
        headers: { 
            'X-CSRFToken': cookies
        }
    });

    await $.ajax({
        type: "PUT",
        url: `/api/v1/campaigns/${id}`,
        data: {
            message: data[1], 
            filter: data[2],
            start: data[3],
            stop: data[4], 
            status: data[5]
        },
        async: true,
        success: function (r)
        {
            response = r;
        },
        failure: function () {
            response = 'error';
        },
    });

    return;
}

function get_status(value, type)
{
    if (type == 's')
    {
        if (value == 1) value = 'Новый';
        else if (value == 2) value = 'Запущен';
        else if (value == 3) value = 'Завершен';
        else value = 'ошибка';
    }
    else
    {
        if (value == 'Новый') value = 1;
        else if (value == 'Запущен') value = 2;
        else if (value == 'Завершен') value = 'Завершен';
        else value = 0;
    }
    return value;
}

function save_data(id) 
{
    var names = ['id', 'message', 'filter', 'start', 'stop', 'status'];
    var values = [];
    
    var tr = $(`#camp${id}`);
    tr.children().each(function (i)
    {
        var inputId = `#${names[i]}_${id}`;
        
        if (i < 5) 
        {
            var value = $(inputId).val();
            $(this).html(value);
            values.push(value);
        }
        else if (i == 5) 
        {
            var  value = $(inputId).find('option:selected').val();
            var status = get_status(value, 's');
            $(this).html(status);
            values.push(value);
        }
    });

    send_row_data(id, values);
}

function row_to_form(id)
{
    var names = ['id', 'message', 'filter', 'start', 'stop', 'status'];

    var tr = $(`#camp${id}`);

    var edit_data_not_exists = $(`#message_${id}`).length == 0;

    edit_data_not_exists && tr.children().each(function (i)
    {
        var sizes = [8, 20, 20, 17, 17, 8];
        var data = $(this).html();
        var size = sizes[i];
        var name = names[i];

        if (i == 0)
        {
            $(this).html(`<input type="text" size="${size}" id="${name}_${id}" value="${data}" style="text-align:center;" disabled>`);
        }
        else if (i == 3 || i == 4)
        {
            $(this).html(`<input class="calendar" type="text" size="${size}" id="${name}_${id}" value="${data}" style="text-align:center;">`);

            $(".calendar").flatpickr({
                enableTime: true,
                altFormat: "F j, Y",
                dateFormat: "Y-m-d H:i:ss",
                pick12HourFormat: false 
            });
        }
        else if (i < 5)
        {
            $(this).html(`<input type="text" size="${size}" id="${name}_${id}" value="${data}" style="text-align:center;">`);
        }
        else if (i == 5)
        {
            var cb = `${name}_${id}`;
            $(this).html(`<select id="${cb}"><option value=1>Новый</option><option value=2>Запущен</option><option value=3>Завершен</option></select>`);

            if (data == 'Новый') data = 1;
            else if (data == 'Запущен') data = 2;
            else if (data == 'Завершен') data = 3;
            else data = 0;

            var status = get_status(data, 's')

            $(`#${cb} option[value=${status}]`).prop('selected', true);
        }
    });
    
    var save = `#save${id}`;
    $(save).show();
    $(save).attr('onclick', `save_data(${id});`)
}

async function send_new_form(data)
{
    var response;
    var cookies = getCookie('csrftoken');

    $.ajaxSetup({
        headers: { 
            'X-CSRFToken': cookies
        }
    });

    await $.ajax({
        type: "POST",
        url: `/api/v1/campaigns`,
        data: data,
        async: true,
        success: function (r)
        {
            response = r;
        },
        failure: function () {
            response = 'error';
        },
    });

    var r = response;

    if (r.result == 'succeed') 
    {
        $('#new_form_result')
        .toggleClass('alert alert-success')
        .html('Успех!')
        .toggle()
        .fadeOut(5000);
    }
    else if (r.result == 'failed') 
    {
        $('#new_form_result')
        .toggleClass('alert alert-danger')
        .html(`Ошибка: ${r.error}`)
        .toggle()
        .fadeOut(5000);
    }
    else
    {
        $('#new_form_result')
        .toggleClass('alert alert-danger')
        .html('Ошибка системы!')
        .toggle()
        .fadeOut(5000);
    };
}

document.addEventListener('DOMContentLoaded', function()
{
    // add edit
    var elements = document.getElementsByClassName("fa-edit");

    var edit_handle = function() 
    {
        var id = this.getAttribute("id");
        if (!id.includes('edit')) return;
        var id = id.split('edit')[1];
        row_to_form(id);
    };

    for (var el of elements) 
    {
        el.addEventListener('click', edit_handle, false);
    }


    // add trash
    elements = document.getElementsByClassName("fa-trash");

    var trash_handle = function() 
    {
        var id = this.getAttribute("id");
        if (!id.includes('trash')) return;
        id = id.split('trash')[1];
        remove_campaign(id);
    };

    for (var el of elements) 
    {
        el.addEventListener('click', trash_handle, false);
    }

    // check operator enabled
    $('#op_filter').change(function() 
    {
        if(this.checked) $("#operator").prop('disabled', false); 
        else $("#operator").prop('disabled', true);   
    });

    // check tag enabled
    $('#tag_filter').change(function() 
    {
        if(this.checked) $("#tag").prop('disabled', false); 
        else $("#tag").prop('disabled', true);   
    });

    // Create new campaign
    $('#new_form').on('submit', function(event) 
    {
        event.preventDefault();

        var data = $(this).serialize();

        var filter = {
            operator: '',
            tag: ''
        }

        if (!data.includes('operator')) filter.operator = $('#operator').val();
        if (data.includes('tag')) filter.tag = $('#tag').val();

        data += `&filter=${JSON.stringify(filter)}`.replaceAll('"', "'");

        alert(data);

        send_new_form(data);
    });

    // add datepicker
    $(".calendar").flatpickr({
        enableTime: true,
        altFormat: "F j, Y",
        dateFormat: "Y-m-d H:i:ss",
        pick12HourFormat: false 
    });
});