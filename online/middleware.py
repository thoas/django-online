# -*- coding: utf-8 -*-
from django.utils import importlib

from online import settings


def get_online(backend):
    mod_path, cls_name = backend.rsplit('.', 1)
    mod = importlib.import_module(mod_path)
    return getattr(mod, cls_name)()


online = get_online(settings.ONLINE_BACKEND)


class OnlineMiddleware(object):
    def process_response(self, request, response):
        if hasattr(request, 'user') and request.user.is_authenticated():
            online.add(request.user)

        return response
