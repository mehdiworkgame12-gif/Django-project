from django.contrib.syndication.views import Feed
from blog.models import Post
from django.urls import reverse

class LatestPostsFeed(Feed):
    title = "Latest Posts"
    link = "/"
    description = "Latest posts"

    def items(self):
        return Post.objects.filter(status=True).order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse("single")
    
    