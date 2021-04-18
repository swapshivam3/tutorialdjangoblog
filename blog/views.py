from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Post,Comment
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import xlwt


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    paginate_by=5
    ordering=['-date_posted']


class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    ordering=['-date_posted']  #- for descending
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)                       #super is to access methods of super class

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)           

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if (self.request.user)==post.author:
            return True
        return False
        
class CommentCreateView(LoginRequiredMixin,CreateView):
    model=Comment
    template_name='blog/comment_form.html'
    fields=['content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) 



def verification_smtp(request):
    return render(request,'blog/b0d5ca0798bf6a4356b249b97a35ab2d.html')

def about(request):
    return render(request,'blog/about.html')

def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Database')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Post Title','Post Content','Date Posted','Author','Email','Likes']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    font_style.font.bold = False
    rows = Post.objects.all()
    arr=[0,0,0,0,0,0]
    arr_c=[0,0,0,0]
    for row in rows:
        row_num+=1
        arr[0]=row.title
        arr[1]=row.content
        arr[2]=row.date_posted.strftime("%Y-%m-%d %H:%M:%S")
        arr[3]=row.author.username
        arr[4]=row.author.email
        arr[5]=row.likes
        for col_num in range(6):
            ws.write(row_num, col_num, arr[col_num], font_style)
        row_num+=2

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        ws.write(row_num, 1,"Comments", font_style)
        
        font_style = xlwt.XFStyle()
        font_style.font.bold = False

        comments=Comment.objects.filter(post=row)
        for comment in comments:
            arr_c[0]=comment.text
            arr_c[1]=comment.created_date.strftime("%Y-%m-%d %H:%M:%S")
            arr_c[2]=comment.author.username
            arr_c[3]=comment.author.email
            row_num += 1
            for col_num in range(4):
                ws.write(row_num, col_num+1, arr_c[col_num], font_style)
        row_num+=2
    
    wb.save(response)
    return response


def like_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.likes+=1
    post.save()
    return redirect('post-detail',pk=post.pk)


@login_required
def add_comment_to_post(request, pk):
        
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.author=request.user
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})