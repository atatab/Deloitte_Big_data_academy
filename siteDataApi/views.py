from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from siteDataApi.serializers import ServiceSerializer, TeamMemberSerializer, BlogPostSerializer
from siteDataApi.models import Service, TeamMember, BlogPost

#Service CRUD
class ListServiceAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CreateServiceAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DestroyServiceAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UpdateServiceAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

#TeamMember CRUD
class ListTeamMemberAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class CreateTeamMemberAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class DestroyTeamMemberAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class UpdateTeamMemberAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

#BlogPost CRUD
class ListBlogPostAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CreateBlogPostAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class DestroyBlogPostAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class UpdateBlogPostAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

