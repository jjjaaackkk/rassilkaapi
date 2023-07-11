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

async function remove_customer(id)
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
        url: `/api/v1/customers/${id}`,
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
        document.getElementById(`customer${id}`).remove();
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
        url: `/api/v1/customers/${id}`,
        data: {
            tag: data[1], 
            tel: data[2],
            tmz: data[3]
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

function save_data(id) 
{
    var names = ['id', 'tag', 'tel', 'tmz'];
    var values = [];
    
    var tr = $(`#customer${id}`);
    tr.children().each(function (i)
    {
        var inputId = `#${names[i]}_${id}`;
        
        if (i < 3) 
        {
            var value = $(inputId).val();
            $(this).html(value);
            values.push(value);
        }
        else if (i == 3) 
        {
            var value = $(inputId).find('option:selected').val();
            $(this).html(value);
            values.push(value);
        }
    });

    send_row_data(id, values);
}

function get_tmz_opts(type)
{
    var tmz = 'Asia/Anadyr,Asia/Barnaul,Asia/Chita,Asia/Irkutsk,Asia/Kamchatka,Asia/Khandyga,Asia/Krasnoyarsk,Asia/Magadan,Asia/Novokuznetsk,Asia/Novosibirsk,Asia/Omsk,Asia/Sakhalin,Asia/Srednekolymsk,Asia/Tomsk,Asia/Ust-Nera,Asia/Vladivostok,Asia/Yakutsk,Asia/Yekaterinburg,Europe/Astrakhan,Europe/Kaliningrad,Europe/Kirov,Europe/Moscow,Europe/Samara,Europe/Saratov,Europe/Simferopol,Europe/Ulyanovsk,Europe/Volgograd'.split(',');

    if (type == 1)
    {
        var opts = ''
        for (var t of tmz) opts += `<option value="${t}">${t}</option>`;
        return opts
    }

    return tmz;
}

function row_to_form(id)
{
    var names = ['id', 'tag', 'tel', 'tmz'];

    var tr = $(`#customer${id}`);

    var edit_data_not_exists = $(`#message_${id}`).length == 0;

    edit_data_not_exists && tr.children().each(function (i)
    {
        var sizes = [8, 10, 20, 8];
        var data = $(this).html();
        var size = sizes[i];
        var name = names[i];

        if (i == 0)
        {
            $(this).html(`<input type="text" size="${size}" id="${name}_${id}" value="${data}" style="text-align:center;" disabled>`);
        }
        else if (i < 3)
        {
            $(this).html(`<input type="text" size="${size}" id="${name}_${id}" value="${data}" style="text-align:center;">`);
        }
        else if (i == 3)
        {
            var cb = `${name}_${id}`;
            var opts = get_tmz_opts(1);
            $(this).html(`<select id="${cb}">${opts}</select>`);
            $(`#${cb} option[value="${data}"]`).prop('selected', true);
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
        url: `/api/v1/customers`,
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
        remove_customer(id);
    };

    for (var el of elements) 
    {
        el.addEventListener('click', trash_handle, false);
    }

    // Create new campaign
    $('#new_form').on('submit', function(event) 
    {
        event.preventDefault();

        var tel = $('#tel').val();
        var is_num = /^\d+$/.test(tel);

        if (tel.length != 11)
        {
            $('#new_form_result')
            .toggleClass('alert alert-danger')
            .html('Ошибка: формат телефона неверный!')
            .toggle()
            .fadeOut(5000);
            return;
        }
        else if (tel[0] != '7')
        {
            $('#new_form_result')
            .toggleClass('alert alert-danger')
            .html('Ошибка: телефон должен начинаться на 7!')
            .toggle()
            .fadeOut(5000);
            return;
        }
        else if (!is_num)
        {
            $('#new_form_result')
            .toggleClass('alert alert-danger')
            .html('Ошибка: телефон должен содержать только цифры!')
            .toggle()
            .fadeOut(5000);
            return;
        }

        var data = $(this).serialize();
        send_new_form(data);
    });

    // add tmz
    var tmz_values = get_tmz_opts(0);
    $.each(tmz_values, function (i, item) 
    {
        $('#tmz').append($('<option>', 
        { 
            value: tmz_values[i],
            text : tmz_values[i]
        }));
    });
});