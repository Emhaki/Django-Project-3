from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Art, Comment
from .forms import ArtForm, CommentForm
from django.core.paginator import Paginator
import re
from django.views.generic import ListView
from django.db.models import Q
from django.http import JsonResponse
from accounts.decorators import artist_required


def index(request):

    return render(request, "articles/index.html")


def loading(request):

    return render(request, "articles/loading.html")

def ticket_machine(request):

    return render(request, "articles/ticket_machine.html")

def main(request):
    arts = Art.objects.order_by("pk")

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
            "arts": arts,
            "name": name,
            "page_obj": page_obj,
            "category": category,
            "art_type_all": art_type_all,
        }
        return render(request, "articles/main.html", context)

    else:
        context = {
            "arts": arts,
            "category": category,
            "art_type_all": art_type_all,
        }
    return render(request, "articles/main.html", context)


@artist_required
# 작가만 작품 등록할 수 있도록
def create(request):
    if request.method == "POST":
        art_form = ArtForm(request.POST, request.FILES)
        if art_form.is_valid():
            art = art_form.save(commit=False)
            art.artist = request.user
            art.save()
            return redirect("articles:main")

    else:
        art_form = ArtForm()

    context = {
        "art_form": art_form,
    }
    return render(request, "articles/create.html", context=context)


def detail(request, pk):
    art = Art.objects.get(pk=pk)
    if request.user.is_authenticated:
        user = get_user_model().objects.get(pk=request.user.pk)

        user_recently_view = user.recently_view
        target = str(art.pk)

        # 번호 추가
        if f"_{target}_" in user_recently_view:
            user_recently_view = user_recently_view.replace(f"_{target}_", "")
            user_recently_view += f"_{target}_"
        else:
            user_recently_view += f"_{target}_"

        # 최근 본 작품 개수제한
        if len(user_recently_view.replace("_", "")) > 6:
            i = 1
            while user_recently_view[i] != "_":
                i += 1
            else:
                user_recently_view = user_recently_view[i + 1 :]

        # 최근 본 작품 꺼내 쓸 때는 replace("__", ",").replace("_", "") 한 다음에 리스트로 바꿔서 꺼내 쓰면 될 것 같음
        # 스택 자료구조
        user.recently_view = user_recently_view
        user.save()

    comment_form = CommentForm()
    context = {
        "art": art,
        "comments": art.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


# @artist_required
def update(request, pk):
    art = Art.objects.get(pk=pk)
    if request.user == art.artist:
        if request.method == "POST":
            article_form = ArtForm(request.POST, request.FILES, instance=art)
            if article_form.is_valid():
                article_form.save()
                return redirect("articles:detail", art.pk)

        else:
            art_form = ArtForm(instance=art)

        context = {"art": art, "art_form": art_form}
        return render(request, "articles/update.html", context)
    else:
        return redirect("articles:detail", art.pk)


# @artist_required
def delete(request, pk):
    if request.user.is_authenticated:
        target_art = Art.objects.get(pk=pk)
        if request.user == target_art.artist:
            target_art.delete()
    return redirect("articles:main")


# @artist_required
def comment_create(request, pk):
    if request.user.is_authenticated:
        art = Art.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.art = art
            comment.user = request.user
            comment.save()
        comments = art.comment_set.all()
        comment_dict = {}
        i = 0
        for one_comment in comments:
            if one_comment.user.test:
                name = one_comment.user.creater_name
            elif one_comment.user.creater_name:
                name = one_comment.user.creater_name
            elif one_comment.user.username:
                name = one_comment.user.username
            comment_dict[f"comment_set{i}"] = {
                "commentPk": one_comment.pk,
                "commentUser": name,
                "commentContent": one_comment.content,
            }
            i += 1
        context = {
            "commentSet": comment_dict,
        }
        return JsonResponse(context)
    else:
        print("로그인 해주세요!")
        context = {
            "errorMsg": "로그인 해주세요!",
        }
        return JsonResponse(context)


# @artist_required
def comment_delete(request, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
        context = {
            "commentPk": comment_pk,
        }
        return JsonResponse(context)
    else:
        context = {
            "errorMsg": "로그인 해주세요!",
        }
        return JsonResponse(context)


# @login_required
def like(request, pk):
    if request.user.is_authenticated:
        art = Art.objects.get(pk=pk)

        if request.user in art.likes.all():
            art.likes.remove(request.user)
            is_liked = False
        else:
            art.likes.add(request.user)
            is_liked = True

        context = {"is_liked": is_liked, "like_cnt": art.likes.count()}
        return JsonResponse(context)

    return redirect("accounts:login")


def search(request):
    all_data = Art.objects.order_by("-pk")
    search = request.GET.get("search")
    paginator = Paginator(all_data, 6)
    page_obj = paginator.get_page(request.GET.get("page"))
    category = ["동양화", "서양화", "판화", "일러스트", "조각 및 조소", "설치미술", "사진"]

    if search:
        search_list = all_data.filter(
            Q(title__icontains=search)
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
        if search == None:
            search = ""

        context = {
            "search": search,
            "search_list": all_data,
            "question_list": page_obj,
            "category": category,
        }
    return render(request, "articles/search.html", context)

def about(request):
    return render(request, "articles/about.html")