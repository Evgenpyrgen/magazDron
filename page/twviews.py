from .models import Category, Good
from django.core.paginator import Paginator, InvalidPage
from django.views.generic.base import TemplateView

class GoodListView(TemplateView):
    template_name = "page/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        try:
            page_num = self.request.GET["page"]
        except KeyError:
            page_num = 1
        context["cats"] = Category.objects.order_by("name")
        if kwargs["cat_id"] == None:
            context["category"] = Category.objects.first()
        else:
            context["category"] = Category.objects.get(pk = kwargs["cat_id"])
        paginator = Paginator(Good.objects.filter(category = 
                                                  context["category"]).order_by("name"), 2)
        try:
            context["goods"] = paginator.page(page_num)
        except InvalidPage:
            context["goods"] = paginator.page(1)
        return context

class GoodDetailView(TemplateView):
    template_name = "page/good.html"

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        context["cats"] = Category.objects.order_by("name")
        try:
            context["good"] = Good.objects.get(pk = kwargs["good_id"])
        except Good.DoesNotExist:
            raise Http404
        return context