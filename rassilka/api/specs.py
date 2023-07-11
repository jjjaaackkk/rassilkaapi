from drf_yasg import openapi

# GET Responses
customer_get_response_all = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'customer': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID клиента', example=142),
                        'tag':openapi.Schema(type=openapi.TYPE_STRING, description="Тег", example='good'),
                        'tel':openapi.Schema(type=openapi.TYPE_STRING, description="Номер телефона", example='79093112029'),
                        'tmz':openapi.Schema(type=openapi.TYPE_STRING, description="Часовой пояс", example='Europe/Moscow'),
                    }
                    ),),})}

# GET Responses
customer_get_response = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'customer': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID клиента', example=142),
                    'tag':openapi.Schema(type=openapi.TYPE_STRING, description="Тег", example='good'),
                    'tel':openapi.Schema(type=openapi.TYPE_STRING, description="Номер телефона", example='79093112029'),
                    'tmz':openapi.Schema(type=openapi.TYPE_STRING, description="Часовой пояс", example='Europe/Moscow'),
                    }
                    )}),
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

campaign_get_response_all = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'campaigns': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID клиента', example=142),
                        'message': openapi.Schema(type=openapi.TYPE_STRING, max_length=160, description="Текст SMS сообщения", example="Поздравляем вас с Днем Рождения!"),
                        'filter': openapi.Schema(type=openapi.TYPE_STRING, max_length=255, description="Фильтр рассылки", example="{'operator':'933,909','tag':'good,new'}"),
                        'start': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время начала рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
                        'stop': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время завершения рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
                        'status': openapi.Schema(type=openapi.TYPE_INTEGER, description="Статус", example=1, enum=[
                            {1: 'новая'},
                            {2: 'в процессе'},
                            {3: 'завершена'},
                            ]),
                    }
                    ),),})}

campaign_get_response = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID клиента', example=142),
                        'message': openapi.Schema(type=openapi.TYPE_STRING, max_length=160, description="Текст SMS сообщения", example="Поздравляем вас с Днем Рождения!"),
                        'filter': openapi.Schema(type=openapi.TYPE_STRING, max_length=255, description="Фильтр рассылки", example="{'operator':'933,909','tag':'good,new'}"),
                        'start': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время начала рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
                        'stop': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время завершения рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
                        'status': openapi.Schema(type=openapi.TYPE_INTEGER, description="Статус", example=1, enum=[
                            {1: 'новая'},
                            {2: 'в процессе'},
                            {3: 'завершена'},
                            ]),
                    }),
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

stats_get_response_main = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'campaigns': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Всего', example=30),
                    'ready':openapi.Schema(type=openapi.TYPE_INTEGER, description="Новые", example=10),
                    'started':openapi.Schema(type=openapi.TYPE_INTEGER, description="Запущенные", example=10),
                    'finished':openapi.Schema(type=openapi.TYPE_INTEGER, description="Готовые", example=10),
                    }
                    ),
            'messages': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Всего', example=30),
                    'succeed':openapi.Schema(type=openapi.TYPE_INTEGER, description="Успешные", example=10),
                    'failed':openapi.Schema(type=openapi.TYPE_INTEGER, description="Неудачные", example=10),
                    'finished':openapi.Schema(type=openapi.TYPE_INTEGER, description="Готовые", example=10),
                    }
                    ),})}

stats_get_response = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'campaigns': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Всего', example=30),
                    'ready':openapi.Schema(type=openapi.TYPE_INTEGER, description="Новые", example=10),
                    'started':openapi.Schema(type=openapi.TYPE_INTEGER, description="Запущенные", example=10),
                    'finished':openapi.Schema(type=openapi.TYPE_INTEGER, description="Готовые", example=10),
                    }
                    ),
            'messages': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Всего', example=30),
                    'succeed':openapi.Schema(type=openapi.TYPE_INTEGER, description="Успешные", example=10),
                    'failed':openapi.Schema(type=openapi.TYPE_INTEGER, description="Неудачные", example=10),
                    'finished':openapi.Schema(type=openapi.TYPE_INTEGER, description="Готовые", example=10),
                    }
                    ),}),             
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}


# POST Request Bodies
customer_post_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['tag', 'tel', 'tmz'],
    properties={
        'tag':openapi.Schema(type=openapi.TYPE_STRING, description="Тег", example='good'),
        'tel':openapi.Schema(type=openapi.TYPE_STRING, description="Номер телефона", example='79093112029'),
        'tmz':openapi.Schema(type=openapi.TYPE_STRING, description="Часовой пояс", example='Europe/Moscow'),
        },
    )

campaign_post_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['message', 'filter', 'start', 'stop'],
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, max_length=160, description="Текст SMS сообщения", example="Поздравляем вас с Днем Рождения!"),
        'filter': openapi.Schema(type=openapi.TYPE_STRING, max_length=255, description="Фильтр рассылки", example="{'operator':'933,909','tag':'good,new'}"),
        'start': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время начала рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
        'stop': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время завершения рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
    }
    )

# POST Responses
campaign_post_responses = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'result': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

customer_post_responses = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'result': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

# PUT Requests
campaign_put_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, max_length=160, description="Текст SMS сообщения", example="Поздравляем вас с Днем Рождения!"),
        'filter': openapi.Schema(type=openapi.TYPE_STRING, max_length=255, description="Фильтр рассылки", example="{'operator':'933,909','tag':'good,new'}"),
        'start': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время начала рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
        'stop': openapi.Schema(type=openapi.TYPE_STRING, description="Дата и время завершения рассылки", example="2023-05-27T12:48:07", format="YYYY-MM-DD HH:MM:ss"),
        'status': openapi.Schema(type=openapi.TYPE_INTEGER, description="Статус", example=1, enum=[
            {1: 'новая'},
            {2: 'в процессе'},
            {3: 'завершена'},
            ]),
    }
)

# PUT Responses

campaign_put_responses = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'result': openapi.Schema(type=openapi.TYPE_STRING,),
                    }),
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

customer_put_responses = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'result': openapi.Schema(type=openapi.TYPE_STRING,),
                    }),
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}

# GET Parameters

campaign_par = openapi.Parameter(
    'id', openapi.IN_PATH,
    description="Id рассылки",
    type=openapi.TYPE_INTEGER
    )

customer_par = openapi.Parameter(
    'id', openapi.IN_PATH,
    description="Id клиента",
    type=openapi.TYPE_INTEGER
    )

msg_par = openapi.Parameter(
    'id', openapi.IN_PATH,
    description="Id сообщения",
    type=openapi.TYPE_INTEGER
    )

# DELETE responses
messages_delete_responses = {
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'result': openapi.Schema(type=openapi.TYPE_STRING,),
                    }),
    404: openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'error': openapi.Schema(type=openapi.TYPE_STRING,),
                    })}