from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return the last page of results.
        items = paginator.page(paginator.num_pages)
    return items


def image_path(instance, filename):
    imagename, extension = filename.split(".")
    return f"category/{instance.id}.{extension}"


def is_valid_query_paramter(param):
    return param != '' and param is not None
