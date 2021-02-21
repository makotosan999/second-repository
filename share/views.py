from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Image,Friend,Post     #imageちゃんとある
from .forms import ImageForm, HelloForm,TweetForm

def index(request):
    images = Image.objects.all()
    timeline = Post.objects.all()
    data = Friend.objects.all()
    params = {                    ##なぜparam?contextにするべき？
        'title':'Share/Index',
        'msg':'ホーム画面',
        'goto1':'post',
        'goto2':'mypage',
        'goto3':'create',
        'timeline': timeline,
        'images':images,
        'data': data,
    }
    return render(request, 'share/index.html', params)

def upload(request):               ##画像投稿用
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='/share')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'share/upload.html', context)

def post(request):
    params = {
        'title':'Share/Post',
        'msg':'投稿画面',
        'goto1':'index',
        'goto2':'mypage',
        'form': TweetForm(),
    }
    if (request.method == 'POST'):
        content = request.POST['content']

        post = Post(content=content)
        post.save()
        return redirect(to='/share')
    return render(request, 'share/post.html', params)

def mypage(request):
    params = {
        'title':'Share/Mypage',
        'msg':'マイページ',
        'goto1':'index',
        'goto2':'post',
    }    
    return render(request, 'share/mypage.html', params)

# create model
def create(request):
    params = {
        'title': 'Share/create',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,\
                age=age,birthday=birth)
        friend.save()
        return redirect(to='/share')
    return render(request, 'share/create.html', params)    


def edit(request, num):
    obj = Post.objects.get(id=num)      #ここでのobjみたいなのは勝手に名前つけてるだけ？
    if (request.method == 'POST'):
        post = TweetForm(request.POST, instance=obj) ##models.pyのcontentにしたらいいのかpostにしたらいいのかわからん
        post.save()
        return redirect(to='/share')
    params = {
        'title': 'share/edit',
        'id':num,
        'form': obj(instance=obj),           #対応させる？
    }
    return render(request, 'share/edit.html', params)


def delete(request, num):
    content = Post.objects.get(id=num)      
    if (request.method == 'POST'):
        content.delete()
        return redirect(to='/share')
    params = {
        'title': '削除',
        'goto1': 'index',
        'goto2': 'mypage',
        'id':num,
        'obj': content,
    }    
    return render(request,'share/delete.html',params)
