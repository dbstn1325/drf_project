from rest_framework.throttling import UserRateThrottle


class ReviewListThrottle(UserRateThrottle):
    scope = 'review_list'
    
class ReviewDetailThrottle(UserRateThrottle):
    scope = 'review_detail'