from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.views.generic import date_based, list_detail
from blog.models import *

import datetime
import re

def post_list(request, page=0, paginate_by=5, **kwargs):
	page_size = paginate_by
	return list_detail.object_list(
		request,
		queryset=Post.objects.published(),
		template_name='blog/post_archive.django.html',
		paginate_by=page_size,
		page=page,
		**kwargs
	)

def post_detail(request, slug, year, month, day, **kwargs):
	posts = None
	
	# Allow super user to view any post
	if request.user.is_superuser:
		posts = Post.objects.all()
	else:
		posts = Post.objects.published()
	
	return date_based.object_detail(
		request,
		year=year,
		month=month,
		day=day,
		date_field='publish',
		slug=slug,
		queryset=posts,
		month_format='%m',
		extra_context = {'is_detail': True},
		allow_future = True,
		**kwargs
	)
	
def category_list(request, template_name='blog/category_list.django.html', **kwargs):
	return list_detail.object_list(
		request,
		queryset=Category.objects.all(),
		template_name=template_name,
		**kwargs
	)
	
def category_detail(request, slug, template_name='blog/category_detail.django.html', **kwargs):
	category = get_object_or_404(Category, slug=slug)
	
	return list_detail.object_list(
		request,
		queryset=category.post_set.published(),
		extra_context={'category': category},
		template_name=template_name,
		**kwargs
	)
	
def post_archive_year(request, year, **kwargs):
	return date_based.archive_year(
		request,
		year=year,
		date_field='publish',
		queryset=Post.objects.published(),
		make_object_list=True,
		template_name='blog/post_archive.django.html',
		**kwargs
	) 

def post_archive_month(request, year, month, **kwargs):
	return date_based.archive_month(
		request,
		year=year,
		month=month,
		date_field='publish',
		month_format='%m',
		queryset=Post.objects.published(),
		template_name='blog/post_archive.django.html',
		**kwargs
	) 

def post_archive_day(request, year, month, day, **kwargs):
	return date_based.archive_day(
		request,
		year=year,
		month=month,
		day=day,
		date_field='publish',
		month_format='%m',
		queryset=Post.objects.published(),
		template_name='blog/post_archive.django.html',
		**kwargs
	)