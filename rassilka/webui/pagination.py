from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_items(items, page, items_per_page = 10):

    paginator = Paginator(items, items_per_page)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    return {
        'items': result, 
        'pages': paginator.num_pages
    }