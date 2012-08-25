from itertools import chain
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from portfolio.models import Project, Video

def index(request):
	all_projects = Project.objects.all().filter(published=True).order_by('category', '-start_date')
	return render_to_response('portfolio/index.django.html', locals(), context_instance=RequestContext(request))
	
def detail(request, slug):
	project = get_object_or_404(Project, slug=slug, published=True)
	return render_to_response('portfolio/detail.django.html', locals(), context_instance=RequestContext(request))
	
def video(request, project_slug, video_slug):
	project = get_object_or_404(Project, slug=project_slug, published=True)
	video = get_object_or_404(Video, project=project, slug=video_slug)
	return render_to_response('portfolio/video.django.html', locals(), context_instance=RequestContext(request))