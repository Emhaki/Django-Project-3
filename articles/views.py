from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Art, Comment
from .forms import ArtForm, CommentForm
from django.core.paginator import Paginator
import re
from django.views.generic import ListView
from django.db.models import Q

def main(request):
    
    arts = Art.objects.order_by('pk')
    # 작품 카테고리
    category = ["동양화", "서양화", "판화", "일러스트", "조각 및 조소", "설치미술", "사진"]
    art_type_all = "모든 작품"
    # art_type = re.sub(r"[0-9]", "", request.GET.get("type"))

    # 페이지네이션
    paginator = Paginator(arts, 8)
    page_number = request.GET.get("type")
    
    if request.GET.get("type"):
        name = re.sub(r"[0-9]", "", request.GET.get("type"))
        arts = Art.objects.filter(art_category__contains=name)
        paginator = Paginator(arts, 8)
        page_number = re.sub(r"[^0-9]", "", request.GET.get("type")) 
        page_obj = paginator.get_page(page_number)
        context = {
            'arts': arts,
            'name': name,
            'page_obj': page_obj,
            'category': category, 
            'art_type_all': art_type_all,
        }
        return render(request, "articles/main.html", context)
    
    else:
       context = {
        'arts': arts,
        'category': category,
        'art_type_all': art_type_all,
        }
    return render(request, "articles/main.html", context)

# @artist_required
# 작가만 작품 등록할 수 있도록
def create(request):
    if request.method == 'POST':
        art_form = ArtForm(request.POST, request.FILES)
        if art_form.is_valid():
            art = art_form.save(commit=False)
            art.artist = request.user 
            art.save()
            return redirect('articles:main')
    
    else:
        art_form = ArtForm()
    
    context = {
        'art_form': art_form,
    }
    return render(request, 'articles/forms.html', context=context)

def detail(request, pk):
    art = Art.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        'art': art,
        'comments': art.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

# @artist_required
def update(request, pk):
    art = Art.objects.get(pk=pk)
    if request.user == art.user: 
        if request.method == 'POST':
            article_form = ArtForm(request.POST, request.FILES, instance=art)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:detail', art.pk)

        else:
            art_form = ArtForm(instance=art)
        context = {
            'art_form': art_form
        }
        return render(request, 'articles/form.html', context)
    else:
        return redirect('articles:detail', art.pk)

# @artist_required
def delete(request, pk):
    Art.objects.get(pk=pk).delete()
    return redirect("articles:main", pk)

# @artist_required
def comment_create(request, pk):
    art = Art.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.art = art
        comment.user = request.user
        comment.save()

    return redirect('articles:detail', art.pk)

# @artist_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if comment.user == request.user:
        comment.delete()     
    return redirect('articles:detail', pk)

# @login_required
def like(request, pk):
    article = Art.objects.get(pk=pk)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
        
    return redirect('articles:detail', pk)

# class SearchView(ListView):
#     model = Art
#     context_object_name = "arts_list"
#     template_name = "articles/search.html"
#     paginate_by = 8
    
#     def get_queryset(self):
#         search_keyword = self.request.GET.get("q", "")
#         arts_list = Art.objects.order_by('-id')
#         return Art.objects.filter(
#             Q(title__icontains=search_keyword)
#             | Q(artist__icontains=search_keyword)
#         )
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         paginator = context["paginator"]
#         page_numbers_range = 5
#         max_index = len(paginator.page_range)
        
#         page = self.request.GET.get("page")
#         current_page = int(page) if page else 1
        
#         start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#         end_index = start_index + page_numbers_range
        
#         if end_index >= max_index:
#             end_index = max_index
        
#         page_range = paginator.page_range[start_index:end_index]
#         context["page_range"] = page_range
        
#         search_keyword = self.request.GET.get("q", "")
        
#         if len(search_keyword) > 1:
#             context["q"] = search_keyword

#         return context

def search(request):
    all_data = Art.objects.order_by("-pk")
    search = request.GET.get("search")
    paginator = Paginator(all_data, 6)
    page_obj = paginator.get_page(request.GET.get("page"))
    category = ["동양화", "서양화", "판화", "일러스트", "조각 및 조소", "설치미술", "사진"]

    if search:
        search_list = all_data.filter(
            Q(title__icontains=search)
            | Q(content__icontains=search) 
            | Q(artist__nickname__icontains=search) 
            )
        paginator = Paginator(search_list, 6)
        page_obj = paginator.get_page(request.GET.get("page"))
        context = {
            "search": search,
            "search_list": search_list,
            "question_list": page_obj,
            "category": category,
        }
    else:
        if search == None :
            search = ''
            
        context = {
            "search": search,
            "search_list": all_data,
            "question_list": page_obj,
            "category": category,
        }
    return render(request, "articles/search.html", context)