from django.urls import re_path
from docs.views import DocsRootView, serve_docs

app_name = 'docs'

urlpatterns = [
    re_path(r'^$', DocsRootView.as_view(permanent=True), name='docs_root'),
    re_path(r'^(?P<path>.*)$', serve_docs, name='docs_files'),
]