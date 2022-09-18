from urllib import request
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from watchlist_app.api import serializers
from watchlist_app import models
from rest_framework_simplejwt.tokens import RefreshToken


# Login Logout Test
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="wjddbstn023", password="1234")
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))
    
        self.stream = models.StreamPlatform.objects.create(name="netflix", about="넷플릭스입니다", website="http://www.netflix.com")
    def test_streamplaform_create(self):
        data = {
            "name": "tvN",
            "about": "신서유기가 방송하는 곳",
            "website": "http://www.tvN.com",
        }
        # 기존 basename 의 streamplatform 중 list 기능(READ, CREATE) 를 쓰겠다.
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_streamplatform_detail(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="wjddbstn023", password="1234")
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))

        self.stream = models.StreamPlatform.objects.create(name="netflix", about="넷 플리스입니다", website="http://www.netflix.com")
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
                                                         title="신서유기3", storyline="강호동과 이수근의 미친조합",
                                                         active=True)
        
    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "신서유기3",
            "stroyline": "이수근 강호동 등등",
            "active": True
        }
        
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_detail(self):
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, '신서유기3')

class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="wjddbstn023", password="1234")
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))

        self.stream = models.StreamPlatform.objects.create(name="netflix", about="넷 플리스입니다", website="http://www.netflix.com")
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
                                                         title="신서유기3", storyline="강호동과 이수근의 미친조합",
                                                         active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream,
                                                         title="신서유기3", storyline="강호동과 이수근의 미친조합",
                                                         active=True)
        
        self.review = models.Review.objects.create(review_user=self.user, watchlist=self.watchlist2, rating=5, description="이 영화 개꿀잼", active=True)
    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "이 영화 너무꿀잼",
            "active": True,
        }
        
        response = self.client.post(reverse('movie_review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        # self.assertEqual(models.Review.objects.get().rating, 5)
        
        # 특정 watchlist에 리뷰남길시
        response = self.client.post(reverse('movie_review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "watchlist": self.watchlist,
            "rating": 5,
            "description": "이 영화 너무꿀잼",
            "active": True,
        }
        
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('movie_review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_update(self):
        
        
        data = {
            "review_user": self.user,
            "watchlist": self.watchlist,
            "rating": 5,
            "description": "이 영화 너무꿀잼",
            "active": False,
        }
        
        response = self.client.put(reverse('movie_review_detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # 특정 watchlist의 리뷰 확인
    def test_review_list(self):
        response = self.client.get(reverse('movie_review_list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # 특정 리뷰 확인
    def test_review_detail(self):
        response = self.client.get(reverse('movie_review_detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # 특정 유저의 리뷰들 확인
    def test_review_user(self):
        response = self.client.get('/api/watch/user-reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
         
