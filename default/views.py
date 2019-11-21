from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, RedirectView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import*
from django.urls import reverse

# Create your views here.
def poll_list(req):
    polls= Poll.objects.all()
    return render_to_response('poll_list.html',{'polls':polls})


class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll
    
    def get_context_data(self,**kwarps):
        context = super().get_context_data(**kwarps)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context

## 投票
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1   # 將選項的票數+1
        option.save()       # 儲存至資料庫
        return "/poll/"+str(option.poll_id)+"/"

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']    # 指定要顯示的欄位
    success_url = '/poll/'  # 成功新增後要導向的路徑
    template_name = 'general_form.html' # 要使用的頁面範本

class PollUpdate(UpdateView):
    model = Poll
    fields = ['subject']        # 指定要顯示的欄位
    success_url = '/poll/'      # 成功新增後要導向的路徑
    template_name = 'general_form.html' # 要使用的頁面範本

class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    template_name = 'default/poll.form.html'
    # 成功新增選項後要導向其所屬的投票主題檢視頁面
    def get_success_url(self):
        #return '/poll/'+str(self.kwargs['pid'])+'/'
        #return'/poll/{}/'.format(self)
         return reverse('poll_view',args =[ self.kwargs['pid']])
    # 表單驗證，在此填上選項所屬的投票fromat(s主題 id
    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form.kwags['pid']) 

class OptionEdit(UpdateView):
    model = Option
    template_name = 'default/poll_form.html'
    # 刪除成功後返回其所屬投票主題檢視頁面
    def get_success_url(self):
        return reverse('poll_view', args={ self.object.poll_id})
        
class OptionDelete(DeleteView):
    model = Option
    template_name = "confirm_delete.html"  
    def get_success_url(self):
        return reverse('poll_view', args={ self.object.poll_id})

class PollDelete(DeleteView):
    model = Poll
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        Option.objects.filter(poll_id=self.object.id).delete()
        return reverse('poll_list')
     