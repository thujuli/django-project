from django.views.generic.base import TemplateView
from blogs.views import ArticleLastestEachCategory


class HomeTemplateView(TemplateView, ArticleLastestEachCategory):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        article_list = self.get_lastest_article()
        context = {
            'article_list': article_list
        }
        return context
