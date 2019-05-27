from django import template


register = template.Library()


PAGINATION_WINDOW = 10
HALF_PAGINATION_WINDOW = int(PAGINATION_WINDOW / 2)


@register.inclusion_tag('pagination/pagination_element.html')
def pagination_element(request, page_obj):
    all_pages = page_obj.paginator.page_range
    current_page = page_obj.number
    first_page = all_pages[0]
    last_page = all_pages[-1]

    page_numbers = all_pages
    if len(all_pages) <= PAGINATION_WINDOW:
        page_numbers = all_pages
    else:
        first_page_number = current_page - (HALF_PAGINATION_WINDOW + 1)
        if first_page_number < 0:
            first_page_number = 0
        page_numbers = all_pages[first_page_number:current_page + HALF_PAGINATION_WINDOW]

    return {'page_obj': page_obj,
            'page_numbers': page_numbers,
            'first_page': first_page,
            'last_page': last_page,
            'request': request }