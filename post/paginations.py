from rest_framework.pagination import PageNumberPagination


class DocumentPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'limit'
