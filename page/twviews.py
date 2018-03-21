from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, InvalidPage
from django.views.generic.base import ContextMixin
from .models import Category, Good

class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        return context

class GoodListView(ListView, CategoryListMixin):
    template_name = "page/index.html"
    paginate_by = 3
    cat = None
    
    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"]  == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs["cat_id"])
        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context["category"] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category = self.cat).order_by("name")

class GoodDetailView(DetailView, CategoryListMixin):
    template_name = "page/good.html"
    model = Good
    pk_url_kwarg = "good_id"
    
    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context