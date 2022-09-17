from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class WatchlistPagination(PageNumberPagination):
    # 한 페이지에 표시될 게시물 갯수 지정
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 100
    
# limit: 한 페이지당 표시될 게시물 갯수 지정
# start: 페이지 시작지점 지정
class WatchlistOPPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
# 최신 순 커서 페이지네이션
class WatchlistCuPagination(CursorPagination):
    page_size = 2
    ordering = '-created_at'