from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Art, Comment
from .forms import ArtForm, CommentForm


def main(request):
    arts = Art.objects.order_by('pk')

    context = {
        'arts': arts
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