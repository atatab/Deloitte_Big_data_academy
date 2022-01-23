from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from siteDataApi.serializers import ServiceSerializer, TeamMemberSerializer, BlogPostSerializer
from siteDataApi.models import Service, TeamMember, BlogPost

#Service CRUD
class ListServiceAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CreateServiceAPIView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DestroyServiceAPIView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UpdateServiceAPIView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

#TeamMember CRUD
class ListTeamMemberAPIView(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class CreateTeamMemberAPIView(CreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class DestroyTeamMemberAPIView(DestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class UpdateTeamMemberAPIView(UpdateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

#BlogPost CRUD
class ListBlogPostAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CreateBlogPostAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class DestroyBlogPostAPIView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class UpdateBlogPostAPIView(UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

